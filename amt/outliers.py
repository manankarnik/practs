import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("movies.csv")
df = df.dropna()
Q1 = df["RunTime"].quantile(0.25)
Q3 = df["RunTime"].quantile(0.75)

IQR = Q3 - Q1
lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR

print("Outliers: ")
out_indices = (df["RunTime"] < lower) | (df["RunTime"] > upper)
print(df[out_indices])

df["RunTime"].plot(kind="box")
plt.show()
