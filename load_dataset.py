import pandas as pd
df = pd.read_csv("PhiUSIIL_Phishing_URL_Dataset.csv")
print(df.head())
print("\nShape:", df.shape)
print("\nColumns:")
print(df.columns)