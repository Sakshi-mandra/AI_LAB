import numpy as np 

# Training data
X = np.array([
    [1000, 2],
    [1500, 3],
    [2000, 4],
    [2500, 4],
    [3000, 5]
], dtype=float)

y = np.array([200, 300, 400, 500, 600], dtype=float)

# Feature Scaling (Normalization) to prevent exploding gradients
X_mean = np.mean(X, axis=0)
X_std = np.std(X, axis=0)
X_scaled = (X - X_mean) / X_std

# Number of training examples 
m = len(y)

# Initialize parameters
w1 = 0.0
w2 = 0.0
b = 0.0

# Learning rate (can be larger now that features are scaled)
alpha = 0.01

# Number of iterations
iterations = 10000

for i in range(iterations):
    # Prediction using scaled features
    y_pred = b + w1 * X_scaled[:, 0] + w2 * X_scaled[:, 1]
    
    # Error & Cost
    error = y_pred - y
    cost = (1 / (2 * m)) * np.sum(error**2)
    
    # Gradients
    dw1 = (1 / m) * np.sum(error * X_scaled[:, 0])
    dw2 = (1 / m) * np.sum(error * X_scaled[:, 1])  # FIXED: dw2 instead of dw1
    db = (1 / m) * np.sum(error)
    
    # Parameter updates (FIXED: spelling of alpha)
    w1 = w1 - alpha * dw1
    w2 = w2 - alpha * dw2
    b = b - alpha * db
    
    # Display cost periodically
    if i % 1000 == 0:
        print(f"Iteration: {i} | Cost: {cost:.4f}")

# Moved outside the loop so it only prints once at the end
print("\nFinal Parameters:")
print("w1 =", w1)
print("w2 =", w2)
print("b =", b)