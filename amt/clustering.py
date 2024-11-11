import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.metrics import silhouette_score
from sklearn.cluster import KMeans, AgglomerativeClustering
from scipy.cluster.hierarchy import dendrogram, linkage


df = pd.read_csv("fish_data.csv")
df = df.drop(columns=["species"])
x = StandardScaler().fit_transform(df)
x = PCA(n_components=2).fit_transform(x)


wss = []
for k in range(1, 16):
    km = KMeans(n_clusters=k)
    wss.append(km.fit(x).inertia_)
plt.plot(range(1, 16), wss, marker="o")
plt.xlabel("Number of Clusters")
plt.ylabel("WSS Error")
plt.title("Elbow Plot for K-means Clustering")
plt.show()


km = KMeans(n_clusters=3)
km_clusters = km.fit_predict(x)
sil = silhouette_score(x, km_clusters)
print("K-means Silhouette Score:", sil)
plt.scatter(x[:, 0], x[:, 1], c=km_clusters)
plt.xlabel("Principal Component 1")
plt.ylabel("Principal Component 2")
plt.title("K-means Clustering")
plt.show()


linkage_matrix = linkage(x, method="ward")
dendrogram(linkage_matrix)
plt.title("Dendrogram")
plt.show()


agglomerative = AgglomerativeClustering(n_clusters=8)
agglomerative_clusters = agglomerative.fit_predict(x)
sil = silhouette_score(x, agglomerative_clusters)
print("Agglomerative Silhouette Score:", sil)
plt.scatter(x[:, 0], x[:, 1], c=agglomerative_clusters)
plt.xlabel("Principal Component 1")
plt.ylabel("Principal Component 2")
plt.title("Agglomerative Clustering")
plt.show()


plt.scatter(df["length"], df["w_l_ratio"], c=agglomerative_clusters)
plt.xlabel("Length")
plt.ylabel("Weight Length Ratio")
plt.title("Agglomerative Clustering")
plt.show()
