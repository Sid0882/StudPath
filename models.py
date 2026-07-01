from database import db
from datetime import datetime

class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    
    name      = db.Column(db.String(120), nullable=False)
    email     = db.Column(db.String(120), unique=True, nullable=False)
    password  = db.Column(db.String(256), nullable=False)
    mobile    = db.Column(db.String(20))
    
    college   = db.Column(db.String(200)) 
    course    = db.Column(db.String(100)) 
    year      = db.Column(db.String(10))
    education = db.Column(db.String(40))
    field     = db.Column(db.String(40))
    
    tools     = db.Column(db.Text, default="[]") 
    interest  = db.Column(db.Text, default="[]") 
    languages = db.Column(db.Text, default="[]")

class QuizSession(db.Model):
    __tablename__ = "quiz_sessions"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)

    # Scores from quiz
    prog_score = db.Column(db.Float)
    math_score = db.Column(db.Float)
    anal_score = db.Column(db.Float)
    comm_score = db.Column(db.Float)

    # Prediction features
    top_career = db.Column(db.String(80))

    # Raw data for debugging
    raw_answers = db.Column(db.Text)

    timestamp = db.Column(db.DateTime, default=datetime.utcnow)