import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, f1_score, recall_score, confusion_matrix


class Perceptron:
    @staticmethod
    def activate(x): return np.where(x >= 0, 1, 0)
    
    def __init__(self, learning_rate=0.1, epochs=20):
        self.learning_rate = learning_rate
        self.epochs = epochs
        self.bias = 0
        self.weights = []

    def fit(self, x, y):
        self.weights = np.zeros(x.shape[1])

        for _ in range(self.epochs):
            for i, xi in enumerate(x):
                y_pred = self.activate(np.dot(xi, self.weights) + self.bias)

                error = self.learning_rate * (y[i] - y_pred)
                self.weights += error * xi
                self.bias += error

    def predict(self, x): return self.activate(np.dot(x, self.weights) + self.bias)


data = pd.read_csv("SAHeart.csv")
data = data.drop(columns=["row.names"])
data["famhist"] = data["famhist"] == "Present"

x = data.drop(columns=["chd"])
y = data["chd"].astype(int).values

x_scaled = StandardScaler().fit_transform(x)
x_train, x_test, y_train, y_test = train_test_split(x_scaled, y, test_size=0.2)

perceptron = Perceptron()
perceptron.fit(x_train, y_train)
y_pred = perceptron.predict(x_test)

accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)
cf = confusion_matrix(y_test, y_pred)

print(f"Accuracy: {accuracy:.2f}", f"Precision: {precision:.2f}", f"Recall: {recall:.2f}", f"F1 Score: {f1:.2f}", f"\nConfusion Matrix:\n{cf}", sep="\n")

