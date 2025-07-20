import pytest
import pandas as pd
import numpy as np
import train_model
from sklearn.ensemble import RandomForestClassifier

df = pd.read.csv("data/census.csv")

def test_data_shape(df):
    """
    # Test that data has no null values
    """
    assert df.shape==df.dropna().shape, "Dropping nulls changes shape"

def test_random_forest():
    """
    # Test the models algorithm
    """
    X = np.array([[1, 2], [3, 4]])
    y = np.arry([0,1])

    model = train_model(X,y)

    assert isinstance(model, RandomForestClassifier)


# TODO: implement the third test. Change the function name and input as needed
def test_three():
    """
    # add description for the third test
    """
    # Your code here
    pass
