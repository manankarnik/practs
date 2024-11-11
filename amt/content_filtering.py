import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

df = pd.read_csv("movies_metadata.csv").head(20000)
df["overview"] = df["overview"].fillna("")


tfmat = TfidfVectorizer().fit_transform(df["overview"])
cosine = cosine_similarity(tfmat, tfmat)
indices = pd.Series(df.index, index=df["original_title"])
print(indices)


def recommend(title, cosine=cosine):
    idx = indices[title]
    sim = list(enumerate(cosine[idx]))
    sim = sorted(sim, key=lambda x: x[1], reverse=True)
    sim = sim[1:11]
    print(sim)
    idxs = [s[0] for s in sim]
    scores = [s[1] for s in sim]
    return pd.DataFrame({
        "title": df["original_title"].iloc[idxs],
        "score": scores,
    })

print(recommend("Toy Story"))
