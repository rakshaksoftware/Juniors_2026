import numpy as np
import pandas as pd
from ridge import RidgeRegression

# Load data
data = pd.read_csv("data.csv")

X = data.iloc[:, :-1].values
y = data.iloc[:, -1].values

X_mean = X.mean(axis=0)
X_std = X.std(axis=0)
X_std[X_std == 0] = 1
X = (X - X_mean) / X_std

y_mean = np.mean(y)
y_std = np.std(y)
y_scaled = (y - y_mean) / y_std
#y = (y - y_mean) / y_std

# Add bias term (optional)
X = np.hstack([np.ones((X.shape[0], 1)), X])

# Train model
model = RidgeRegression(lr=0.01, max_iter=500, lam=0.1)
model.fit(X, y_scaled)

# Predictions
y_pred = (y_std*model.predict(X)) + y_mean

# Print results
print("Final Weights:", model.w)
print("Final Loss:", model.loss_history[-1])

# Optional: print loss curve
import matplotlib.pyplot as plt
plt.plot(model.loss_history)
plt.title("Loss vs Iterations")
plt.xlabel("Iterations")
plt.ylabel("Loss")
plt.show()