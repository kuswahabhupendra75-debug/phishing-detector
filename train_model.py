# ============================================================
#   CyberShield Pro - Model Training Script
#   Developed by: Hack Shastra
#   Version: 2.0
# ============================================================

import sys
import io

# Force UTF-8 output so emoji/box chars work on Windows
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
import pickle

print("")
print("=" * 52)
print("   CYBERSHIELD PRO  -  AI TRAINING ENGINE")
print("         Developed by Hack Shastra")
print("=" * 52)
print("")

print("[1/4] Loading phishing dataset...")
df = pd.read_csv("phishing_dataset.csv")
print(f"      OK - {len(df)} records loaded.\n")

X = df[["url_length", "dot_count", "has_at", "has_https", "has_hyphen"]]
y = df["label"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print("[2/4] Training Random Forest Classifier...")
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)
print("      OK - Model trained successfully.\n")

print("[3/4] Evaluating model performance...")
y_pred = model.predict(X_test)
acc = accuracy_score(y_test, y_pred)
print(f"      Test Accuracy : {acc * 100:.2f}%")
print("")
print("      Classification Report:")
print(classification_report(y_test, y_pred, target_names=["Safe", "Phishing"]))

print("[4/4] Saving model to model.pkl...")
with open("model.pkl", "wb") as f:
    pickle.dump(model, f)
print("      OK - model.pkl saved successfully!\n")

print("=" * 52)
print("  DONE! Run app: py -m streamlit run app.py")
print("  -- Hack Shastra (C) 2026")
print("=" * 52)
print("")
