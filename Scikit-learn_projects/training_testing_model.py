import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import mglearn

from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris
iris_dataset = load_iris()

X_train, X_test, y_train, y_test = train_test_split(
    iris_dataset['data'], iris_dataset['target'], random_state=0)

print("X_train shape: {}".format(X_train.shape))
print("Y_train shape: {}".format(y_train.shape))

print("X_test shape: {}".format(X_test.shape))
print("Y_test shape: {}".format(y_test.shape))

# create dataframe from data in X_train
# label the columns using the strings in iris_dataset.feature_name
iris_dataframe = pd.DataFrame(X_train, columns=iris_dataset.feature_name)
# create a scatter matrix from the dataframe, color by y_train
grr = pd.scatter_matrix(iris_dataframe, c=y_train, figsize=(15, 15), marker='o',
                        hist_kwds={'blin': 20}, s=60, alpha=.8, cmap=mglearn.cm3)
