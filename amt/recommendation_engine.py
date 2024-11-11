import pandas as pd

df = pd.read_csv("movies_metadata.csv")

C = df["vote_average"].mean()
m = df["vote_count"].quantile(0.9)


def weighted_rating(x, m=m, C=C):
    v = x["vote_count"]
    R = x["vote_average"]

    return (v/(v+m) * R) + (m/(v+m) * C)


q_mov = df.query(f"vote_count >= {m}")
q_mov["score"] = df.apply(weighted_rating, axis=1)
q_mov = q_mov.sort_values("score", ascending=False)
print(q_mov[["title", "score"]].head(20))
