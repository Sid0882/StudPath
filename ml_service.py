import joblib
import numpy as np
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

model = joblib.load(os.path.join(BASE_DIR, 'career_rf_model.pkl'))
le = joblib.load(os.path.join(BASE_DIR, 'label_encoder.pkl'))

try:
    scaler = joblib.load(os.path.join(BASE_DIR, 'scaler.pkl'))
except:
    scaler = None


print("🚨 MODEL FEATURES:", model.n_features_in_)  


def predict_top3_from_quiz(quiz_results):

    interest_map = {
        'data': 0,
        'web': 1,
        'security': 2,
        'ai': 3,
        'backend': 4,
        'frontend': 5,
        'devops': 6,
        'design': 7,
        'mobile': 8
    }

    domain = quiz_results.get('dominant_domain', 'backend')

    if domain not in interest_map:
        print("⚠️ UNKNOWN DOMAIN:", domain)

    interest_val = interest_map.get(domain, 0)

    # Analyze quiz results and prepare features for the model
    features = [[
        quiz_results.get('prog_score', 50),
        quiz_results.get('math_score', 50),
        quiz_results.get('anal_score', 50),
        quiz_results.get('comm_score', 50),

        quiz_results.get('problem_solving', 50),
        quiz_results.get('creativity', 50),
        quiz_results.get('leadership', 50),

        interest_val
    ]]

    print("\n===== MODEL DEBUG =====")
    print("Domain:", domain)
    print("Feature length:", len(features[0]))
    print("Features:", features)

    # Apply scaling
    if scaler:
        features = scaler.transform(features)

    # Predict
    probs = model.predict_proba(features)[0]

    print("Probabilities:", probs)

    top3_idx = probs.argsort()[-3:][::-1]

    results = []
    for idx in top3_idx:
        career = le.inverse_transform([idx])[0]
        confidence = round(float(probs[idx]) * 100, 2)

        results.append({
            "career": career,
            "confidence": confidence
        })

    print("Top 3 Results:", results)
    print("========================\n")

    return results