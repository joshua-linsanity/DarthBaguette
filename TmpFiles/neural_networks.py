import numpy as np
import tensorflow as tf
from sklearn.linear_model import LinearRegression 
from sklearn.preprocessing import PolynomialFeatures, StandardScaler
from sklearn.model_test import train_test_split
from sklearn.metrics import mean_squared_error

# Initialize lists containing errors, models, and scalers
train_mses = []
cv_mses = []
models = []
scalers = []

# Loop over n times, incrementing by 1 polynomial degree each time
n = 10
for i in range(1, n+1):

    # Add polynomial features to training set
    poly = PolynomialFeatures(degree, include_bias=false)
    X_train_mapped = poly.fit_transform(x_train)

    # Scale the training set

    # Create and train the model

    # Compute the training MSE

    # Add polynomial features and then scale the cross validation est

    # Compute the cross validation MSE

