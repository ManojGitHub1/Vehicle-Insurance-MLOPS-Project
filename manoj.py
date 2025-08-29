import pickle
from sklearn import tree

# Load pickle file
with open("artifact/08_29_2025_16_43_30/model_trainer/trained_model/model.pkl", "rb") as f:
    model = pickle.load(f)

print(type(model))  # To see the type of object
print(model)        # Sometimes prints details (e.g., sklearn model)

print(dir(model))  # List all attributes and methods of MyModel
rf = model.trained_model_object # or model.estimator, depending on your wrapper
print(rf.__class__)     # Should show RandomForestClassifier
print(rf.get_params())  # Hyperparameters
print(len(rf.estimators_))       # Number of trees
print(rf.estimators_[0])         # First decision tree
print(rf.estimators_[0].tree_)   # Underlying tree object
print(tree.export_text(rf.estimators_[0]))
tree_ = rf.estimators_[0].tree_
print(tree_.feature)      # which features are used at each node
print(tree_.threshold)    # thresholds
print(tree_.value)        # class counts at leaves
