from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_breast_cancer
from sklearn.tree import export_graphviz
import graphviz
import os

os.environ["PATH"] += os.pathsep + '/opt/homebrew/bin'
# load data
cancer = load_breast_cancer()
X_train, X_test, y_train, y_test = train_test_split(
    cancer.data, cancer.target, stratify=cancer.target, random_state=42)

tree = DecisionTreeClassifier(max_depth=4, random_state=0)
tree.fit(X_train, y_train)
print("Accuracy on training set: {:.3f}".format(tree.score(X_train, y_train)))
print("Accuracy on test set: {:.3f}".format(tree.score(X_test, y_test)))
print(os.environ['PATH'])

dot_data = export_graphviz(tree, out_file=None, class_names=["malignant", "benign"],
                feature_names=cancer.feature_names, impurity=False, filled=True)

graph = graphviz.Source(dot_data)
graph.render("decision_tree")

