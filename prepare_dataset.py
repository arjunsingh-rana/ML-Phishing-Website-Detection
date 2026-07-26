import pandas as pd

# Load dataset
df = pd.read_csv("PhiUSIIL_Phishing_URL_Dataset.csv")

# Keep only URL and label
df = df[["URL", "label"]]

# Display information
print(df.head())

print("\nShape:", df.shape)

print("\nMissing Values:")
print(df.isnull().sum())

print("\nLabel Distribution:")
print(df["label"].value_counts())