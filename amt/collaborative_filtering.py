import pandas as pd
from scipy.sparse import csr_matrix
from sklearn.neighbors import NearestNeighbors

ratings = pd.read_csv("ratings.csv")
movies = pd.read_csv("movies2.csv")

print(ratings.head())
print(movies.head())

movie_mapper = {mid: i for i, mid in enumerate(ratings["movieId"].unique())}
movie_inv = {i: mid for i, mid in enumerate(ratings["movieId"].unique())}
user_mapper = {uid: i for i, uid in enumerate(ratings["userId"].unique())}

movie_idx = ratings["movieId"].map(movie_mapper)
user_idx = ratings["userId"].map(user_mapper)

X = csr_matrix(((ratings["rating"]), (movie_idx, user_idx)), shape=(len(movie_mapper), len(user_mapper)))

movie_titles = dict(zip(movies["movieId"], movies["title"]))
movie_id = 1
k = 10

knn = NearestNeighbors(n_neighbors=k+1, metric="cosine")
knn.fit(X)

neighbors = knn.kneighbors(X[movie_mapper[movie_id]], return_distance=False)
movie_indices = [movie_inv[i] for i in neighbors.flatten()[1:k+1]]
print(f"\nSince you liked {movie_titles[movie_id]}, you might like")
for i in movie_indices:
    print(movie_titles[i])

