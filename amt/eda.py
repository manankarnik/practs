import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv("movies.csv")
df = df.dropna()
df["Gross"] = df["Gross"].str.replace("$", "").str.replace("M", "").astype(float)
df["RunTime"] = df["RunTime"].astype(float)
df["VOTES"] = df["VOTES"].str.replace(",", "").astype(int)
print(df)

# corr = df[["RATING", "VOTES", "Gross", "RunTime"]].corr().round(2)
# sns.heatmap(corr, annot=True)
# plt.title("Heatmap")


# plt.scatter(df["RunTime"], df["Gross"])
# plt.xlabel("RunTime")
# plt.ylabel("Gross")
# plt.title("RunTime vs Gross")

# genres = df["GENRE"].str.strip().str.split(", ")
# print(genres)
# plt.pie(genres.value_counts(), labels=genres.value_counts().index, autopct="%1.1f%%")
# plt.show()
# genres = df["GENRE"].str.strip().str.split(", ").explode()
# print(genres)
# plt.pie(genres.value_counts(), labels=genres.value_counts().index, autopct="%1.1f%%")

# plt.hist(df["Gross"], bins=10, edgecolor="black")


# df_highest = df.query("RATING > 8.5")
# df_lowest = df.query("RATING <= 8.5")
# df_highest_genres = df_highest["GENRE"].str.strip().str.split(", ").explode()
# df_lowest_genres = df_lowest["GENRE"].str.strip().str.split(", ").explode()
#
# plt.figure(figsize=(10, 5))
# plt.subplot(1, 2, 1)
# plt.pie(df_highest_genres.value_counts(), labels=df_highest_genres.value_counts().index, autopct="%1.1f%%")
# plt.title("Highest")
# print(df_highest_genres)
# plt.subplot(1, 2, 2)
# plt.pie(df_lowest_genres.value_counts(), labels=df_lowest_genres.value_counts().index, autopct="%1.1f%%")
# plt.title("Lowest")


# genres = df["GENRE"].str.strip().str.split(", ").apply(lambda x: x[0])
# gen_year_counts = pd.crosstab(df["YEAR"], genres)
# gen_year_counts.plot(kind="bar", stacked=True, figsize=(12, 6))

ax = plt.axes(projection="3d")
ax.scatter3D(df["RunTime"], df["Gross"], df["VOTES"])
ax.set_xlabel("RT")
ax.set_ylabel("G")
ax.set_zlabel("V")
plt.title("3D")
plt.show()
