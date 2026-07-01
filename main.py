import os
import json
from flask import Flask, jsonify, render_template, request, redirect, url_for, session
from werkzeug.security import generate_password_hash, check_password_hash
from dotenv import load_dotenv
from ai_service import ask_ai, generate_ai_roadmap, ask_ai_roadmap_chat
from quiz_scorer import enrich_and_score
from ml_service import predict_top3_from_quiz   
from models import QuizSession, User
from quiz_data import QUIZ_QUESTIONS
from predictor import CAREERS, DETAILED_ROADMAPS
from database import db
from roadmap_routes import roadmap_bp

app = Flask(__name__)

app.register_blueprint(roadmap_bp)

basedir = os.path.abspath(os.path.dirname(__file__))
db_path = os.path.join(basedir, "instance", "database.db")

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + db_path
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY", "dev_secret")

db.init_app(app)

with app.app_context():
    os.makedirs(os.path.dirname(db_path), exist_ok=True)
    db.create_all()
    print(f"\n DATABASE CONNECTED AT: {db_path}\n")


@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        user = User(
            name=f"{request.form.get('first_name', '')} {request.form.get('last_name', '')}",
            email=request.form.get("email"),
            mobile=request.form.get("mobile", ""),    
            password=generate_password_hash(request.form.get("password")),
            college=request.form.get("college", ""),  
            course=request.form.get("course", ""),    
            year=request.form.get("year", ""),         
            interest=",".join(request.form.getlist("interest")),
            languages=",".join(request.form.getlist("languages"))
        )
        db.session.add(user)
        db.session.commit()
        return redirect("/login")

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        user = User.query.filter_by(email=request.form["email"]).first()

        if user and check_password_hash(user.password, request.form["password"]):
            session["user_id"] = user.id
            return redirect("/dashboard")

        return "Invalid Email or Password"

    return render_template("login.html")

@app.route("/forgot-password", methods=["GET", "POST"])
def forgot_password():
    if request.method == "POST":
        email = request.form.get("email")
        # to verify if email exists in our user base before sending reset link
        user = User.query.filter_by(email=email).first()
        
        if user:
            print(f"[SYSTEM] Password reset link requested for: {email}")
            return "SUCCESS: A reset link has been dispatched to your email."
        
        return "ERROR: Email identifier not found in our nodes."

    return render_template("forgot-password.html")

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/login")


@app.route("/manual", methods=["GET", "POST"])
def manual():
    if "user_id" not in session:
        return redirect("/login")

    if request.method == "POST":
        selected = request.form.get("career")
        other = request.form.get("other_career")
        career = other if selected == "Other" and other else selected

        if career:
            session["chosen_career"] = career
            return redirect(url_for("roadmap_bp.roadmap", career_name=career))

    return render_template("manual.html")


@app.route("/dashboard")
def dashboard():
    if "user_id" not in session:
        return redirect("/login")

    user = User.query.get(session["user_id"])
    
    top_career = None
    if "chosen_career" in session:
        from roadmap_routes import MANUAL_TO_RICH_MAP
        raw_choice = session["chosen_career"]
        top_career = MANUAL_TO_RICH_MAP.get(raw_choice, raw_choice)
    else:
        latest_session = QuizSession.query.filter_by(user_id=user.id).order_by(QuizSession.id.desc()).first()
        if latest_session:
            top_career = latest_session.top_career

    from roadmap_data import RICH_ROADMAPS
    user_roadmap = RICH_ROADMAPS.get(top_career, []) if top_career else []
    
    career_stats = {"salary": "₹6–20 LPA", "growth": "High", "match": 65, "jobs": "Active"}
    career_skills = ["Logic", "Algorithms", "Data Structures", "System Design", "Databases"]
    
    if top_career:
        SALARY_MAP = {
            "Data Scientist / ML Engineer": {"salary": "₹10–30 LPA", "jobs": "High Demand", "growth": "32%", "match": 88},
            "Full Stack Developer": {"salary": "₹8–22 LPA", "jobs": "Very High", "growth": "25%", "match": 92},
            "Cybersecurity / DevSecOps Engineer": {"salary": "₹10–30 LPA", "jobs": "Critical Need", "growth": "35%", "match": 80},
            "Frontend / UI Engineer": {"salary": "₹6–18 LPA", "jobs": "High Demand", "growth": "20%", "match": 85},
            "Backend / Systems Engineer": {"salary": "₹8–25 LPA", "jobs": "Steady", "growth": "22%", "match": 84},
            "Mobile App Developer": {"salary": "₹6–20 LPA", "jobs": "Growing", "growth": "18%", "match": 78},
            "Data Analyst / Business Intelligence": {"salary": "₹5–18 LPA", "jobs": "Surging", "growth": "28%", "match": 82},
            "Product Manager / Tech Lead": {"salary": "₹12–35 LPA", "jobs": "Competitive", "growth": "20%", "match": 75},
        }
        career_stats.update(SALARY_MAP.get(top_career, {}))

        from predictor import CAREERS
        career_info = next((c for c in CAREERS if c["career"] == top_career), None)
        if career_info and "tools" in career_info:
            career_skills = career_info["tools"][:6] 

    return render_template("dashboard.html", 
                           user=user, 
                           top_career=top_career, 
                           user_roadmap=user_roadmap,
                           career_stats=career_stats,
                           career_skills=json.dumps(career_skills))


@app.route("/choice")
def choice():
    if "user_id" not in session:
        return redirect("/login")
    return render_template("choice.html")

@app.route("/assessment")
def assessment():
    if "user_id" not in session:
        return redirect("/login")

    return render_template("quiz.html", questions_json=json.dumps(QUIZ_QUESTIONS))

@app.route("/submit_quiz", methods=["POST"])
def submit_quiz():
    
    if "user_id" not in session:
        return redirect("/login")

    raw_json = request.form.get("answers_json", "[]")
    print(f"\n[FRONTEND ALERT] The browser sent us: {raw_json}\n")

    answers = json.loads(request.form.get("answers_json", "[]"))

    result = enrich_and_score(answers)

    print("DEBUG INPUT:", {
    "prog": result["prog_score"],
    "math": result["math_score"],
    "anal": result["anal_score"],
    "comm": result["comm_score"],
    "problem": result.get("problem_solving"),
    "creativity": result.get("creativity"),
    "leadership": result.get("leadership"),
    "domain": result["domain"]
    })

    top3 = predict_top3_from_quiz({
    "prog_score": result["prog_score"],
    "math_score": result["math_score"],
    "anal_score": result["anal_score"],
    "comm_score": result["comm_score"],

    "problem_solving": result.get("problem_solving", 50),
    "creativity": result.get("creativity", 50),
    "leadership": result.get("leadership", 50),

    "dominant_domain": result["domain"]
    })

    print("TOP 3 PREDICTIONS:", top3)  

    best_career = top3[0]["career"] if top3 else "Unknown"

    db.session.add(QuizSession(
        user_id=session["user_id"],
        prog_score=result["prog_score"],
        math_score=result["math_score"],
        anal_score=result["anal_score"],
        comm_score=result["comm_score"],
        top_career=best_career,
        raw_answers=json.dumps(answers)
    ))
    db.session.commit()

    results = []

    for i, item in enumerate(top3):
        career_name = item["career"]

        results.append({
            "rank": i + 1,  
            "career": career_name,
            "match": round(item["confidence"], 1),
            "growth": "High",
            "avg_salary": "₹6–20 LPA",
            "gaps": [],
            "roles": [career_name],
            "roadmap": DETAILED_ROADMAPS.get(career_name, [])
        })

    return render_template("result.html", results=results)

@app.route("/chatbot", methods=["POST"])
def chatbot():
    if "user_id" not in session:
        return jsonify({"reply": "Login first"})

    user = User.query.get(session["user_id"])
    message = request.json.get("message")

    return jsonify({"reply": ask_ai(message, user)})

@app.route("/roadmap_chat", methods=["POST"])
def roadmap_chat_route():
    if "user_id" not in session:
        return jsonify({"reply": "Please login first."})

    data = request.get_json()
    message = data.get("message", "").strip()
    career_name = data.get("career", "Tech Career")

    user = User.query.get(session["user_id"])

    reply = ask_ai_roadmap_chat(message, career_name, user)
    
    return jsonify({"reply": reply})

@app.route("/upload_resume", methods=["POST"])
def upload_resume():
    if "user_id" not in session:
        return redirect("/login")

    user = User.query.get(session["user_id"])
    results = {"message": "Resume analysis coming soon"}

    return render_template("dashboard.html", user=user, results=results)

@app.after_request
def add_header(response):
    """
    Forces the browser to not cache pages. 
    Prevents the user from hitting the 'back' button after logging out.
    """
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Pragma"] = "no-cache"
    response.headers["Expires"] = "0"
    return response


if __name__ == "__main__":
    app.run(debug=True, port=5001)