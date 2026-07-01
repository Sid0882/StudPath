import os, json
import numpy as np

# This module contains the core logic for career prediction and personalized roadmap generation based on quiz results and user profiles.
CAREERS = [
    {
        "career":  "Data Scientist",
        "weights": {"programming": 0.30, "maths": 0.35, "analysis": 0.25, "communication": 0.10},
        "domains": ["data", "ai"],
        "fields":  ["cs", "science", "engineering", "commerce"],
        "tools":   ["Python", "SQL", "R", "TensorFlow", "PyTorch", "NumPy", "Pandas"],
        "avg_salary": "8–20 LPA",
        "growth": "Very High",
    },
    {
        "career":  "Machine Learning Engineer",
        "weights": {"programming": 0.35, "maths": 0.35, "analysis": 0.20, "communication": 0.10},
        "domains": ["ai", "data"],
        "fields":  ["cs", "engineering", "science"],
        "tools":   ["Python", "TensorFlow", "PyTorch", "Docker", "Git"],
        "avg_salary": "10–25 LPA",
        "growth": "Very High",
    },
    {
        "career":  "Full Stack Developer",
        "weights": {"programming": 0.50, "maths": 0.15, "analysis": 0.20, "communication": 0.15},
        "domains": ["web", "general"],
        "fields":  ["cs", "engineering"],
        "tools":   ["JavaScript", "React", "Node.js", "SQL", "Git", "HTML/CSS"],
        "avg_salary": "6–18 LPA",
        "growth": "High",
    },
    {
        "career":  "Backend Engineer",
        "weights": {"programming": 0.50, "maths": 0.20, "analysis": 0.20, "communication": 0.10},
        "domains": ["web", "security"],
        "fields":  ["cs", "engineering"],
        "tools":   ["Python", "Java", "SQL", "Docker", "Redis", "Git"],
        "avg_salary": "7–20 LPA",
        "growth": "High",
    },
    {
        "career":  "Data Analyst",
        "weights": {"programming": 0.20, "maths": 0.35, "analysis": 0.30, "communication": 0.15},
        "domains": ["data", "general"],
        "fields":  ["cs", "commerce", "science", "arts"],
        "tools":   ["SQL", "Excel", "Python", "Power BI", "Tableau"],
        "avg_salary": "4–12 LPA",
        "growth": "High",
    },
    {
        "career":  "Product Manager",
        "weights": {"programming": 0.10, "maths": 0.20, "analysis": 0.35, "communication": 0.35},
        "domains": ["general", "web"],
        "fields":  ["cs", "commerce", "engineering", "arts"],
        "tools":   ["Jira", "Figma", "Excel", "SQL"],
        "avg_salary": "8–22 LPA",
        "growth": "High",
    },
    {
        "career":  "Cybersecurity Analyst",
        "weights": {"programming": 0.30, "maths": 0.20, "analysis": 0.35, "communication": 0.15},
        "domains": ["security", "general"],
        "fields":  ["cs", "engineering"],
        "tools":   ["Linux", "Python", "Wireshark", "Git"],
        "avg_salary": "6–18 LPA",
        "growth": "Very High",
    },
    {
        "career":  "Business Analyst",
        "weights": {"programming": 0.10, "maths": 0.25, "analysis": 0.40, "communication": 0.25},
        "domains": ["general", "data"],
        "fields":  ["commerce", "arts", "cs", "engineering"],
        "tools":   ["Excel", "SQL", "Power BI", "Jira"],
        "avg_salary": "4–14 LPA",
        "growth": "Moderate",
    },
    {
        "career":  "AI Research Engineer",
        "weights": {"programming": 0.25, "maths": 0.40, "analysis": 0.25, "communication": 0.10},
        "domains": ["ai", "data"],
        "fields":  ["cs", "science", "engineering"],
        "tools":   ["Python", "TensorFlow", "PyTorch", "NumPy", "R"],
        "avg_salary": "12–30 LPA",
        "growth": "Very High",
    },
    {
        "career":  "DevOps / Cloud Engineer",
        "weights": {"programming": 0.35, "maths": 0.15, "analysis": 0.25, "communication": 0.25},
        "domains": ["web", "security"],
        "fields":  ["cs", "engineering"],
        "tools":   ["Docker", "Kubernetes", "Linux", "Git", "AWS", "Python"],
        "avg_salary": "7–22 LPA",
        "growth": "Very High",
    },
]

# A more detailed roadmap for each career, which can be further personalized based on specific skill gaps.
DETAILED_ROADMAPS = {
    "Data Scientist": [
        "Phase 1: Master Python/R and Statistics fundamentals.",
        "Phase 2: Data Wrangling with Pandas and Visualization (Power BI/Tableau).",
        "Phase 3: Machine Learning (Regression, Classification) & SQL.",
        "Phase 4: Advanced AI (Deep Learning, NLP) & Cloud Deployment."
    ],
    "Machine Learning Engineer": [
        "Phase 1: Deep dive into Python and Linear Algebra/Calculus.",
        "Phase 2: ML Algorithms & Libraries (Scikit-Learn, XGBoost).",
        "Phase 3: Deep Learning Frameworks (PyTorch/TensorFlow).",
        "Phase 4: MLOps (Docker, Model Deployment, Monitoring)."
    ],
    "Full Stack Developer": [
        "Phase 1: Frontend Fundamentals (HTML5, CSS3, Modern JS).",
        "Phase 2: React.js/Next.js and Responsive Design.",
        "Phase 3: Backend (Node.js/Flask) and Database management (SQL/NoSQL).",
        "Phase 4: Authentication, CI/CD, and Hosting (AWS/Vercel)."
    ],
    "Backend Engineer": [
        "Phase 1: Core Language Mastery (Python/Java/Go) & Data Structures.",
        "Phase 2: Database Design, Optimization, and SQL.",
        "Phase 3: System Design, Microservices, and API Architectures.",
        "Phase 4: Caching (Redis), Message Queues, and Server Security."
    ],
    "Data Analyst": [
        "Phase 1: Excel Mastery (Pivot Tables, VBA) & Statistics.",
        "Phase 2: Intermediate SQL for data extraction.",
        "Phase 3: Visualization tools (Power BI or Tableau).",
        "Phase 4: Python for Automation and basic statistical modeling."
    ],
    "Product Manager": [
        "Phase 1: Agile Methodologies & Project Management tools (Jira).",
        "Phase 2: User Research, UX Wireframing (Figma), and Market Analysis.",
        "Phase 3: Technical Literacy (Understanding APIs & Databases).",
        "Phase 4: Data-Driven Decision Making & Product Strategy."
    ],
    "Cybersecurity Analyst": [
        "Phase 1: Computer Networking (TCP/IP) and OS Fundamentals (Linux).",
        "Phase 2: Security Principles (CIA Triad) and Cryptography.",
        "Phase 3: Vulnerability Assessment & Penetration Testing basics.",
        "Phase 4: Security Information & Event Management (SIEM) tools."
    ],
    "Business Analyst": [
        "Phase 1: Business Communication & Requirement Gathering techniques.",
        "Phase 2: Data Analysis using Excel and SQL.",
        "Phase 3: Process Mapping (BPMN) and Documentation.",
        "Phase 4: Stakeholder Management & BI Reporting."
    ],
    "AI Research Engineer": [
        "Phase 1: Advanced Mathematics (Probability, Optimization).",
        "Phase 2: Reading & Implementing Research Papers in PyTorch.",
        "Phase 3: High-Performance Computing & GPU Optimization.",
        "Phase 4: Publishing Research and Experimental Framework Design."
    ],
    "DevOps / Cloud Engineer": [
        "Phase 1: Linux System Administration & Shell Scripting.",
        "Phase 2: Cloud Foundations (AWS/Azure) & Networking.",
        "Phase 3: Containerization (Docker) & Orchestration (Kubernetes).",
        "Phase 4: Infrastructure as Code (Terraform) & CI/CD Pipelines."
    ]
}

# This function builds a personalized roadmap by combining the standard roadmap for a career with specific skill gaps identified for the student.
def _build_roadmap(career_name: str, gaps: list[str]) -> list[str]:
    """Return a detailed, step-by-step roadmap tailored to career and gaps."""
  
    base_path = DETAILED_ROADMAPS.get(career_name, ["General Computer Science fundamentals"])
    
    
    personalized_steps = []
    
    if gaps:
        gap_string = ", ".join(gaps)
        personalized_steps.append(f"🔴 CRITICAL GAP: Focus immediately on learning {gap_string}.")
    
    full_roadmap = personalized_steps + base_path
    
    full_roadmap.append("Final Step: Build a Capstone project and update your LinkedIn/Portfolio.")
    
    return full_roadmap

# This function implements a simple rule-based scoring mechanism to evaluate how well a student's profile matches the requirements of a given career,
#  based on quiz scores and profile attributes.
def _rule_based_score(career: dict, profile: dict) -> float:
    prog = profile.get("programming", 50)
    math = profile.get("maths", 50)
    anal = profile.get("analysis", 50)
    comm = profile.get("communication", 50)
    w = career["weights"]
    base = (prog * w["programming"] + math * w["maths"] + anal * w["analysis"] + comm * w["communication"])
    bonus = 0.0
    if profile.get("domain") in career["domains"]: bonus += 8
    if profile.get("field") in career["fields"]: bonus += 6
    overlap = len(set(profile.get("tools", [])) & set(career["tools"]))
    bonus += min(overlap * 2, 6)
    return min(round(base + bonus, 1), 100)

# This function computes the skill gaps for a student relative to the requirements of a specific career, which helps in personalizing the learning roadmap. 
def _compute_gaps(career_name: str, student_tools: list[str]) -> list[str]:
    
    career_info = next((c for c in CAREERS if c["career"] == career_name), None)
    if not career_info: return []
    required = career_info["tools"]
    known = {t.lower() for t in student_tools}
    return [s for s in required if s.lower() not in known][:4]

# The main function that takes a student's profile and returns the top 3 career predictions along with their match scores,
#  identified skill gaps, and personalized roadmaps.
def predict_careers(profile: dict) -> list[dict]:
    student_tools = profile.get("tools", [])
    scored = []
    for career in CAREERS:
        match = _rule_based_score(career, profile)
        gaps = _compute_gaps(career["career"], student_tools)
        
       
        roadmap = _build_roadmap(career["career"], gaps)

        scored.append({
            "career":     career["career"],
            "match":      match,
            "gaps":       gaps,
            "roadmap":    roadmap,
            "avg_salary": career["avg_salary"],
            "growth":     career["growth"],
            "source":     "rule_based"
        })

    scored.sort(key=lambda x: x["match"], reverse=True)
    return scored[:3]