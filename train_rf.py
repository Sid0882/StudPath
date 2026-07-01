import pandas as pd
import joblib
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report

df = pd.read_csv('tranning_data.csv')

interest_map = {
    'data': 0,
    'web': 1,
    'security': 2,
    'ai': 3,
    'backend': 4,
    'frontend': 5,
    'devops': 6,
    'design': 7,
    'mobile': 8,
    'game': 9,
    'hardware': 10,
    'testing': 11,
    'product': 12
}

df['interest'] = df['interest'].map(interest_map)

df['interest'] = df['interest'].fillna(0)

le = LabelEncoder()
df['career_encoded'] = le.fit_transform(df['career'])

X = df[[
    'programming',
    'math',
    'analytics',
    'communication',   
    'problem_solving', 
    'creativity',     
    'leadership',      
    'interest'
]]

y = df['career_encoded']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

model = RandomForestClassifier(
    n_estimators=200,
    max_depth=12,
    random_state=42
)

model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print("\n===== MODEL EVALUATION =====")
print("Accuracy:", accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred))
print("============================\n")


joblib.dump(model, 'career_rf_model.pkl')
joblib.dump(le, 'label_encoder.pkl')
joblib.dump(scaler, 'scaler.pkl')

print("✅ Model, Encoder, Scaler saved successfully.")