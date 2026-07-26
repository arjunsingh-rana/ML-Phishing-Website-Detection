# 🛡️ PhishGuard - Machine Learning Based Phishing Website Detection

![Python](https://img.shields.io/badge/Python-3.13-blue?logo=python)
![Flask](https://img.shields.io/badge/Flask-Web_App-black?logo=flask)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-Random%20Forest-orange?logo=scikitlearn)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-Completed-success)

A Machine Learning-based web application that detects whether a website URL is **Legitimate** or **Phishing** using **Random Forest Classification** and **URL Feature Engineering**.

---

# 📌 Overview

Phishing attacks trick users into visiting fake websites to steal passwords, banking information, and personal data.

This project uses **Machine Learning** to analyze the lexical characteristics of a URL and predict whether it is:

- ✅ Legitimate Website
- ⚠️ Phishing Website

The application is built using **Python**, **Flask**, **Scikit-learn**, and **Pandas**.

---

# ✨ Features

- URL-based phishing detection
- Machine Learning using Random Forest
- Automatic URL feature extraction
- Confidence score prediction
- Flask web interface
- Fast prediction
- Simple and responsive UI

---

# 🛠️ Tech Stack

| Technology | Purpose |
|------------|---------|
| Python | Programming Language |
| Flask | Web Framework |
| Pandas | Data Processing |
| Scikit-learn | Machine Learning |
| Joblib | Save & Load ML Model |
| HTML/CSS | Frontend |
| VS Code | Development Environment |

---

# 📂 Project Structure

```text
ML-Phishing-Website-Detection
│
├── app.py
├── predictor.py
├── train_model.py
├── prepare_dataset.py
├── load_dataset.py
├── test_features.py
├── features.py
│
├── phishguard_model.joblib
├── PhiUSIIL_Phishing_URL_Dataset.csv
│
├── templates/
│   └── index.html
│
├── static/
│   └── style.css
│
├── screenshots/
│
├── requirements.txt
├── README.md
├── LICENSE
└── .gitignore
```

---

# ⚙️ Working Process

### Step 1: Load Dataset

The PhiUSIIL Phishing URL Dataset is loaded using Pandas.

---

### Step 2: Prepare Dataset

Only the following columns are selected:

- URL
- Label

---

### Step 3: Feature Engineering

Each URL is converted into numerical features such as:

- URL Length
- Hostname Length
- Number of Dots
- Number of Hyphens
- Number of Digits
- HTTPS Usage
- Number of Subdomains
- IP Address Detection
- Suspicious Keywords
- Suspicious Top-Level Domains (TLDs)

---

### Step 4: Train Machine Learning Model

The extracted features are used to train a **Random Forest Classifier**.

The dataset is split into:

- 80% Training Data
- 20% Testing Data

---

### Step 5: Save Model

The trained model is saved using Joblib.

```python
joblib.dump(model, "phishguard_model.joblib")
```

---

### Step 6: Prediction

The Flask application:

1. Accepts a URL
2. Extracts features
3. Loads the trained model
4. Predicts whether the website is phishing or legitimate
5. Displays prediction with confidence score

---

# 🚀 Installation

Clone the repository

```bash
git clone https://github.com/arjunsingh-rana/ML-Phishing-Website-Detection.git
```

Move into the project folder

```bash
cd ML-Phishing-Website-Detection
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
python app.py
```

Open in your browser

```text
http://127.0.0.1:5000
```

---

# 📊 Example

### Input

```text
https://google.com
```

### Output

```text
✅ Legitimate Website
Confidence: 99.81%
```

---

### Input

```text
http://paypal-secure-login.xyz/update.php
```

### Output

```text
⚠️ Phishing Website
Confidence: 98.74%
```

---

# 📷 Screenshots

## Home Page

> Add screenshot here

```
screenshots/home.png
```

---

## Legitimate Website Prediction

> Add screenshot here

```
screenshots/legitimate-result.png
```

---

## Phishing Website Prediction

> Add screenshot here

```
screenshots/phishing-result.png
```

---

# 📈 Machine Learning Model

**Algorithm Used**

- Random Forest Classifier

### Why Random Forest?

- High Accuracy
- Handles Classification Problems Efficiently
- Reduces Overfitting
- Works Well with Structured Data

---

# 🔮 Future Improvements

- Domain Age Verification
- SSL Certificate Validation
- WHOIS Lookup
- DNS Analysis
- HTML Content Analysis
- JavaScript Analysis
- Browser Extension
- Real-Time Threat Intelligence Integration

---

# 👨‍💻 Author

**Arjun Singh**

B.Tech Computer Science Engineering

UPES Dehradun

GitHub: https://github.com/arjunsingh-rana

---

# ⭐ Support

If you found this project useful, please consider giving it a ⭐ on GitHub.

---

# 📄 License

This project is licensed under the MIT License.
