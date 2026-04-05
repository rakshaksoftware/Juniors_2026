# solve.py
# Students must complete the TODO sections

import numpy as np

# ============================================================
# OLS IMPLEMENTATIONS
# ============================================================

def ols_with_intercept(X, y):
    """
    Ordinary Least Squares WITH intercept.

    Parameters
    ----------
    X : numpy array (N,d)
        Feature matrix

    y : numpy array (N,)
        Target values

    Returns
    -------
    w  : slope vector (d,)
    w0 : intercept scalar
    """

    # TODO:
    # Step 1: Add a column of ones to X to represent intercept
    ones = np.ones((X.shape[0],1))
    Xi = np.hstack((ones,X))
    
    # Step 2: Use the normal equation
    #
    #        w = (X^T X)^(-1) X^T y
    w = (np.linalg.inv(Xi.T@ Xi))@(Xi.T)@y
    #
    # Step 3: Separate intercept from weight vector
    w0 = w[0]
    wt = w[1:]
    return wt,w0

    raise NotImplementedError


def ols_no_intercept(X, y):
    """
    OLS WITHOUT intercept.

    Use the normal equation:

        w = (X^T X)^(-1) X^T y
    """

    # TODO:
    w = (np.linalg.inv(X.T@ X))@(X.T)@y
    return w
    # Implement closed-form solution

    raise NotImplementedError


# ============================================================
# PREDICTION FUNCTIONS
# ============================================================

def predict_with_intercept(X, w, w0):
    """
    Predict y = Xw + w0
    """

    # TODO:
    y = X@w + w0
    return y
    # return predicted values

    raise NotImplementedError


def predict_no_intercept(X, w):
    """
    Predict y = Xw
    """

    # TODO
    y = X@w
    return y

    raise NotImplementedError


# ============================================================
# METRICS
# ============================================================

def compute_metrics(y, y_hat):
    """
    Compute the following metrics:

    1. Mean Squared Error (MSE)

        MSE = mean((y - y_hat)^2)

    2. Correlation

    3. Squared Correlation

    4. R^2 score
    """

    # TODO
    #1
    MSE = np.mean((y - y_hat)**2)

    #2
    #correl = np.corrcoef(y,y_hat)
    ym = y.mean()
    yhm = y_hat.mean()
    correl = np.sum((y-ym)*(y_hat-yhm)) / ((np.sum((y-ym)**2)*(np.sum((y_hat-yhm)**2)))**(1/2))

    #3
    sq_correl = correl**2

    #4
    ss_res = np.sum((y-y_hat)**2)
    ss_tot = np.sum((y - ym)**2)
    r2 = 1 - (ss_res/ss_tot)

    return {"MSE":MSE, "Correlation":correl, "Squared Corr": sq_correl, "R2 score":r2}
    raise NotImplementedError


# ============================================================
# DATA LOADING
# ============================================================

def load_data():
    """
    Load dataset from CSV files.

    CSV format:

    size,bedrooms,age,distance,price

    First 4 columns = features
    Last column = target
    """

    train = np.loadtxt("train.csv", delimiter=",", skiprows=1)
    test = np.loadtxt("test.csv", delimiter=",", skiprows=1)

    # TODO:
    # Separate X and y
    x = train[:,:-1]
    y = train[:,-1]
    X_test = test[:,:-1]
    y_test = test[:,-1]

    return x,y,X_test,y_test

    raise NotImplementedError