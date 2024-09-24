from sklearn.datasets import load_iris
iris_dataset = load_iris()

print("Key of iris_dataset: \n{}".format(iris_dataset.keys()))
print(iris_dataset['DESCR'][:193] + "\n...")

print("Target name: {}".format(iris_dataset['target_names']))
print("Feature name: \n{}".format(iris_dataset['feature_names']))
print("Shape of data: {}".format(iris_dataset['data'].shape))

print("First five columns of data: \n{}".format(iris_dataset['data'][:5]))
print("Shape of target: {}".format(iris_dataset['target'].shape))
print("Target: \n{}".format(iris_dataset['target']))