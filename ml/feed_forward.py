import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Input, Dense
from tensorflow.keras.losses import SparseCategoricalCrossentropy
from tensorflow.keras.metrics import SparseCategoricalAccuracy

data = pd.read_csv("SAHeart.csv")
data = data.drop(columns=["row.names"])
data["famhist"] = data["famhist"] == "Present"
data["chd"] = data["chd"] == 1

x = data.drop(columns=["chd"])
y = data["chd"]

x_scaled = StandardScaler().fit_transform(x)
x_train, x_test, y_train, y_test = train_test_split(x_scaled, y, test_size=0.2)

model = Sequential([
    Input((x_train.shape[1],)),
    Dense(64, activation="relu"),
    Dense(128, activation="relu"),
    Dense(2, activation="softmax"),
])

model.compile(optimizer=Adam(), loss=SparseCategoricalCrossentropy(), metrics=[SparseCategoricalAccuracy])

history = model.fit(x_train, y_train, epochs=20)

loss, acc = model.evaluate(x_test, y_test)

print("Acc:", acc)

plt.plot(history.history["loss"])
plt.xlabel("Epochs")
plt.ylabel("Loss")
plt.title("Loss Over Time")
plt.show()
