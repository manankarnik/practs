import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pyclustering.cluster.cure import cure
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.metrics import silhouette_score

df = pd.read_csv("fish_data.csv")
df = df.drop(columns=["species"])
x = StandardScaler().fit_transform(df)
x = PCA(n_components=2).fit_transform(x)

c = cure(x, 8)
c.process()
clusters = c.get_clusters()

labels = np.zeros(x.shape[0])
for i, cluster in enumerate(clusters):
  labels[cluster] = i

plt.scatter(x[:, 0], x[:, 1], c=labels)
sil = silhouette_score(x, labels)
print("Silhouette Score:", sil)
plt.title("CURE Clustering")
plt.xlabel("Principal Component 1")
plt.xlabel("Principal Component 2")
plt.show()
