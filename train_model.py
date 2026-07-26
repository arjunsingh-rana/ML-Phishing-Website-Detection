import pandas as pd
from features import extract_features

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import joblib

# Load dataset
df = pd.read_csv("PhiUSIIL_Phishing_URL_Dataset.csv")

# Keep only required columns
df = df[["URL", "label"]]

print("Extracting features...")

# Convert every URL into features
X = df["URL"].apply(extract_features)

# Convert dictionaries to DataFrame
X = pd.DataFrame(X.tolist())

# Labels
y = df["label"]

print("\nFeature Matrix Shape:", X.shape)
print("Labels Shape:", y.shape)

# Train/Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

print("\nTraining Random Forest...")

# Model
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)

print("Training Complete!")

# Prediction
y_pred = model.predict(X_test)

print("\nAccuracy:", accuracy_score(y_test, y_pred))

print("\nClassification Report\n")
print(classification_report(y_test, y_pred))

# Save model
joblib.dump(model, "phishguard_model.joblib")

print("\nModel saved successfully!")