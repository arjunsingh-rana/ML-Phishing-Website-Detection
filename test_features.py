from features import extract_features

url = "https://paypal-secure-login.xyz/update.php"

features = extract_features(url)

for key, value in features.items():
    print(f"{key}: {value}")