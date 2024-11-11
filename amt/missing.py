import pandas as pd

data = pd.read_csv("movies.csv")
print(data.head())
data["RunTime"] = data["RunTime"].fillna(data["RunTime"].mean())
data["Gross"] = data["Gross"].str.replace("$", "").str.replace("M", "").astype(float)
data["Gross"] = data["Gross"].fillna(data["Gross"].mean())
print(data.head())
