import joblib
import pandas as pd

from features import extract_features

# Load trained model
model = joblib.load("phishguard_model.joblib")

print("=== PhishGuard ML ===")

while True:

    url = input("\nEnter URL (or type exit): ").strip()

    if url.lower() == "exit":
        break

    # Automatically add https:// if missing
    if not url.startswith(("http://", "https://")):
        url = "https://" + url

    # Extract features
    features = extract_features(url)

    X = pd.DataFrame([features])

    # Prediction
    prediction = model.predict(X)[0]

    # Confidence
    probability = model.predict_proba(X)[0]
    confidence = max(probability) * 100

    # Display Result
    if prediction == 0:
        print("\n⚠️ PHISHING WEBSITE")
    else:
        print("\n✅ LEGITIMATE WEBSITE")

    print(f"Confidence: {confidence:.2f}%")