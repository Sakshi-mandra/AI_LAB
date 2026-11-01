"""
Lab 3: Logistic Regression using Gradient Descent for Binary Classification
Aim: Implement binary logistic regression from scratch using NumPy and visualize
     the training loss curve and decision boundary using Matplotlib.
"""

import numpy as np
import matplotlib.pyplot as plt


class LogisticRegressionGD:
    def __init__(self, learning_rate=0.1, n_iterations=1000):
        self.learning_rate = learning_rate
        self.n_iterations = n_iterations
        self.weights = None
        self.bias = None
        self.loss_history = []

    def _sigmoid(self, z):
        """Sigmoid activation function: 1 / (1 + exp(-z))"""
        # Clip z to prevent overflow in np.exp
        z = np.clip(z, -500, 500)
        return 1.0 / (1.0 + np.exp(-z))

    def _compute_loss(self, y_true, y_pred):
        """Binary Cross-Entropy Loss (Log Loss)"""
        epsilon = 1e-15  # Avoid log(0)
        y_pred = np.clip(y_pred, epsilon, 1 - epsilon)
        loss = -np.mean(y_true * np.log(y_pred) + (1 - y_true) * np.log(1 - y_pred))
        return loss

    def fit(self, X, y):
        """
        Train the model parameters using Gradient Descent.
        
        Parameters:
            X (ndarray): Feature matrix of shape (n_samples, n_features)
            y (ndarray): Target vector of shape (n_samples,)
        """
        n_samples, n_features = X.shape

        # 1. Initialize parameters
        self.weights = np.zeros(n_features)
        self.bias = 0.0
        self.loss_history = []

        # 2. Gradient Descent Loop
        for iteration in range(self.n_iterations):
            # Forward pass: linear combination + activation
            linear_model = np.dot(X, self.weights) + self.bias
            y_pred = self._sigmoid(linear_model)

            # Compute gradients
            dw = (1 / n_samples) * np.dot(X.T, (y_pred - y))
            db = (1 / n_samples) * np.sum(y_pred - y)

            # Update parameters
            self.weights -= self.learning_rate * dw
            self.bias -= self.learning_rate * db

            # Record loss
            loss = self._compute_loss(y, y_pred)
            self.loss_history.append(loss)

            # Print loss every 100 iterations
            if (iteration + 1) % 100 == 0 or iteration == 0:
                print(f"Iteration {iteration + 1:4d}/{self.n_iterations} | Loss: {loss:.4f}")

    def predict_proba(self, X):
        """Predict probability estimates for class 1."""
        linear_model = np.dot(X, self.weights) + self.bias
        return self._sigmoid(linear_model)

    def predict(self, X, threshold=0.5):
        """Predict class labels (0 or 1)."""
        y_pred_proba = self.predict_proba(X)
        return (y_pred_proba >= threshold).astype(int)

# MAIN EXECUTION 
if __name__ == "__main__":
    np.random.seed(42)

    # 1. Generate Synthetic 2D Dataset for Classification
    print("=" * 60)
    print("LAB 3: LOGISTIC REGRESSION VIA GRADIENT DESCENT")
    print("=" * 60)

    n_samples = 200
    # Class 0 centered around (-1, -1)
    X_class0 = np.random.randn(n_samples // 2, 2) + np.array([-1.5, -1.5])