import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.cluster import DBSCAN, Birch
from sklearn.metrics import silhouette_score


df = pd.read_csv("fish_data.csv")
df = df.drop(columns=["species"])
x = StandardScaler().fit_transform(df)
x = PCA(n_components=2).fit_transform(df)

dbscan = DBSCAN(eps=0.2, min_samples=8)
db_clusters = dbscan.fit_predict(x)
sil = silhouette_score(x, db_clusters)
print("DBSCAN Silhouette Score:", sil)
plt.scatter(x[:, 0], x[:, 1], c=db_clusters)
plt.title("DBSCAN Clustering")
plt.xlabel("Principal Component 1")
plt.xlabel("Principal Component 2")
plt.show()

birch = Birch(branching_factor=100, n_clusters=8, threshold=1)
birch_clusters = birch.fit_predict(x)
sil = silhouette_score(x, birch_clusters)
print("Birch Silhouette Score:", sil)
plt.scatter(x[:, 0], x[:, 1], c=birch_clusters)
plt.title("Birch Clustering")
plt.xlabel("Principal Component 1")
plt.xlabel("Principal Component 2")
plt.show()
