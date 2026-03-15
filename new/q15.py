import numpy as np
import matplotlib.pyplot as plt

# -------- Line Plot --------
x = np.linspace(-10, 10, 100)
y = x**2

plt.figure()
plt.plot(x, y)
plt.title("Line Plot of f(x) = x^2")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.show()


# -------- Scatter Plot --------
x_scatter = np.random.uniform(0, 1, 100)
y_scatter = np.random.normal(0.5, 0.1, 100)

plt.figure()
plt.scatter(x_scatter, y_scatter)
plt.title("Scatter Plot of Random Points")
plt.xlabel("X values")
plt.ylabel("Y values")
plt.show()


# -------- Histogram --------
data = np.random.exponential(scale=1, size=500)

plt.figure()
plt.hist(data, bins=30)
plt.title("Histogram of Exponential Distribution")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.show()