import numpy as np

class RidgeRegression:
    """
    Ridge Regression using Gradient Descent.

    Parameters:
    lr : learning rate
    max_iter : number of iterations
    tol : stopping tolerance
    lam : regularization strength (lambda)
    """

    def __init__(self, lr=0.01, max_iter=1000, tol=1e-6, lam=0.1):
        self.lr = lr
        self.max_iter = max_iter
        self.tol = tol
        self.lam = lam
        self.w = None
        self.loss_history = []

    def compute_mse_loss(self, w, X, y):
        """
        TODO:
        Compute MSE + Ridge regularization loss

        Steps:
        1. Compute predictions: X @ w
        2. Compute squared error
        3. Take mean
        4. Add lambda * ||w||^2
        """
        pred = X @ w
        sqerr = np.sum((pred - y)**2)
        msqe = sqerr / len(y)
        rrloss = self.lam * np.sum((w**2))
        return (msqe + rrloss)
        pass

    def linear_gradient(self, w, X, y):
        """
        TODO:
        Compute gradient of Ridge loss

        Steps:
        1. Compute residual: (Xw - y)
        2. Compute gradient of MSE: (X.T @ residual)/N
        3. Add regularization gradient: lambda * w
        """
        res = X @ w - y
        grad = ((X.T) @ res) / len(y)  + self.lam * w
        return 2*grad
        #rgrad = self.lam * w
        #return 2 * (grad + rgrad)
         
        pass

    def fit(self, X, y):
        """
        TODO:
        Train using gradient descent

        Steps:
        1. Initialize weights to zeros
        2. Loop:
            - Compute loss
            - Store loss
            - Compute gradient
            - Update weights
        3. Stop when tolerance satisfied
        """
        self.w = np.zeros(X.shape[1])
        for i in range(self.max_iter):
            loss = self.compute_mse_loss(self.w, X, y)
            self.loss_history.append(loss)
            grad = self.linear_gradient(self.w, X, y)
            if np.linalg.norm(grad) < self.tol:
                break
            else:
                self.w = self.w - (self.lr*grad)
        pass

    def predict(self, X):
        """
        TODO:
        Return predictions X @ w
        """
        pred = X @ self.w
        return pred
        pass