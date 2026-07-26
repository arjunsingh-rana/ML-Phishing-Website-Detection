from flask import Flask, render_template, request
import joblib
import pandas as pd

from features import extract_features

app = Flask(__name__)

# Load trained model
model = joblib.load("phishguard_model.joblib")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():

    # Get URL from form
    url = request.form["url"].strip()

    # Automatically add https:// if user enters only domain name
    if not url.startswith(("http://", "https://")):
        url = "https://" + url

    # Extract features
    features = extract_features(url)

    # Convert to DataFrame
    X = pd.DataFrame([features])

    # Predict
    prediction = model.predict(X)[0]

    # Confidence
    probability = model.predict_proba(X)[0]
    confidence = round(max(probability) * 100, 2)
    
    # 0 = PHISHING
    # 1 = LEGITIMATE

    if prediction == 0:
        result = "⚠️ PHISHING WEBSITE"
        color = "red"
    else:
        result = "✅ LEGITIMATE WEBSITE"
        color = "green"

    return render_template(
        "index.html",
        url=url,
        result=result,
        confidence=confidence,
        color=color,
    )


if __name__ == "__main__":
    app.run(debug=True)