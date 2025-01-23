"""
debugging_test_linear_regression.py

This script demonstrates a correct minimal example of:
- Creating a small synthetic dataset
- Splitting data into training and test sets
- Training a LinearRegression model using scikit-learn
- Evaluating the model with Mean Squared Error (MSE)
"""

import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

def train_and_evaluate_model():
    """
    Trains a Linear Regression model on a synthetic dataset and evaluates it.
    return: Mean Squared Error (MSE) of the model
    """


    # 1. Create a small synthetic dataset
    # We'll create a simple linear relationship: y = 2 * x + 1 with some noise
    X = np.array([[i] for i in range(1, 11)])   # [[1], [2], [3], ..., [10]]
    y = 2 * X.squeeze() + 1 + np.random.randn(10) * 0.5

    # 2. Split data into training and test sets (70-30 split)

    # 3. Create and train the Linear Regression model

    # 4. Predict on the test set

    # 5. Evaluate the model using Mean Squared Error

    mse = 4.0 # Placeholder value
    
    return mse

if __name__ == "__main__":
    mse_value = train_and_evaluate_model()
    
    # 6. Minimal check: If MSE is below some threshold, consider it a success
    # (This threshold is arbitrary for demonstration purposes)
    if mse_value < 2.0:
        print("Success: Model MSE is reasonably low.")
    else:
        print("Warning: Model MSE is higher than expected.")