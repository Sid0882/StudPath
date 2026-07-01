import json
from flask import Blueprint, render_template, session, redirect

from models import QuizSession
from predictor import CAREERS, DETAILED_ROADMAPS
from roadmap_data import RICH_ROADMAPS, CAREER_MILESTONES

roadmap_bp = Blueprint('roadmap_bp', __name__)

# This maps the simple names from manual.html to the detailed names in roadmap_data.py
MANUAL_TO_RICH_MAP = {
    "Data Scientist": "Data Scientist / ML Engineer",
    "Web Developer": "Full Stack Developer",
    "Cyber Security": "Cybersecurity / DevSecOps Engineer",
    "UI/UX Designer": "Frontend / UI Engineer",
    "App Developer": "Mobile App Developer"
}

@roadmap_bp.route("/roadmap/<path:career_name>")
def roadmap(career_name):
    if "user_id" not in session:
        return redirect("/login")

    formatted_name = career_name.replace("%20", " ")
    
    mapped_name = MANUAL_TO_RICH_MAP.get(formatted_name, formatted_name)

    match_score = None
    gaps = []
    try:
        latest = QuizSession.query.filter_by(user_id=session["user_id"]).order_by(QuizSession.id.desc()).first()
        if latest and latest.predictions:
            preds = json.loads(latest.predictions)
            for p in preds:
                if p.get("career") == formatted_name or p.get("career") == mapped_name:
                    match_score = p.get("match")
                    gaps = p.get("gaps", [])
                    break
    except Exception:
        pass

    # Build career_info from predictor's CAREERS list (Fallback)
    career_info = next((c for c in CAREERS if c["career"] == mapped_name or c["career"] == formatted_name), None)

    # Safely try to import CAREER_CLUSTERS from quiz data
    cluster_data = None
    try:
        from quiz_data import CAREER_CLUSTERS
        for k, v in CAREER_CLUSTERS.items():
            if v["title"] == mapped_name or v["title"] == formatted_name:
                cluster_data = v
                break
    except ImportError:
        pass 

    if cluster_data and "skills" in cluster_data:
        skills_list = cluster_data["skills"]
    elif career_info and "tools" in career_info:
        skills_list = career_info["tools"]
    else:
        skills_list = ["Problem Solving", "Communication", "Technical Writing", "Critical Thinking"]

    if cluster_data:
        description = cluster_data.get("description", "")
        icon = cluster_data.get("icon", "💻")
    else:
        description = career_info.get("description", f"Explore the detailed path to becoming a {mapped_name}.") if career_info else f"Explore the detailed path to becoming a {mapped_name}."
        icon = career_info.get("icon", "💻") if career_info else "💻"

    SALARY_MAP = {
        "Frontend / UI Engineer":              "₹6–18 LPA",
        "Backend / Systems Engineer":          "₹8–25 LPA",
        "Full Stack Developer":                "₹8–22 LPA",
        "Data Scientist / ML Engineer":        "₹10–30 LPA",
        "DevOps / Cloud Engineer":             "₹10–28 LPA",
        "Cybersecurity / DevSecOps Engineer":  "₹10–30 LPA",
        "AI / ML Research Engineer":           "₹12–40 LPA",
        "Product Manager / Tech Lead":         "₹12–35 LPA",
        "Mobile App Developer":                "₹6–20 LPA",
        "Data Analyst / Business Intelligence":"₹5–18 LPA",
    }
    
    avg_salary = SALARY_MAP.get(mapped_name)
    if not avg_salary:
        avg_salary = career_info.get("avg_salary", "Varies") if career_info else "Varies"

    career_obj = {
        "career":      mapped_name if mapped_name in RICH_ROADMAPS else formatted_name,
        "icon":        icon,
        "description": description,
        "avg_salary":  avg_salary,
        "growth":      career_info.get("growth", "High") if career_info else "High",
        "match":       match_score,
        "tools":       skills_list,
    }

    phases = RICH_ROADMAPS.get(mapped_name)
    
    if not phases:
        old_phases = DETAILED_ROADMAPS.get(formatted_name, DETAILED_ROADMAPS.get(mapped_name, [
            "Phase 1: Master the fundamentals of logic and programming.",
            "Phase 2: Learn the core tools and frameworks for this field.",
            "Phase 3: Build real-world projects to apply your knowledge.",
            "Phase 4: Prepare for interviews and specialize in a sub-domain.",
        ]))
        phase_titles = ["Foundation", "Skill Building", "Projects", "Job Prep"]
        phase_durations = ["Month 1–2", "Month 3–5", "Month 6–9", "Month 10–12"]
        phases = []
        for i, p in enumerate(old_phases[:4]):
            desc = p.split(":", 1)[1].strip() if ":" in p else p
            phases.append({
                "title": phase_titles[i] if i < len(phase_titles) else f"Phase {i+1}",
                "duration": phase_durations[i] if i < len(phase_durations) else "",
                "description": desc,
                "learn": skills_list[:4] if skills_list else ["Core concepts", "Best practices"],
                "resources": [
                    {"icon": "📺", "name": "YouTube tutorials"},
                    {"icon": "📘", "name": "Official documentation"},
                    {"icon": "🎯", "name": "Practice projects"},
                ],
                "project": {"name": f"Phase {i+1} Project", "desc": desc, "tag": ["Beginner","Intermediate","Advanced","Portfolio"][i] if i < 4 else "Project"}
            })

    milestones = CAREER_MILESTONES.get(mapped_name, CAREER_MILESTONES["default"])

    return render_template("roadmap.html",
                           career=career_obj,
                           skills=skills_list,
                           gaps=gaps,
                           phases=phases,
                           milestones=milestones)