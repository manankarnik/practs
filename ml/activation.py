import numpy as np
import matplotlib.pyplot as plt

def tanh(x): return (np.exp(x) - np.exp(-x)) / (np.exp(x) + np.exp(-x))

x = np.linspace(-10, 10, 500)
y = np.tanh(x)

plt.plot(x, y)
plt.axhline(0, color="lightgray", linewidth="0.5")
plt.axvline(0, color="lightgray", linewidth="0.5")
plt.xlabel("x")
plt.ylabel("y")
plt.title("Activation Function")
plt.show()
