from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
# Load the dataset
from sklearn.datasets import load_iris
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

iris = load_iris()

print("\nShape of iris data:", iris.data.shape)
print("Number of feature names:", len(iris.feature_names))
print(iris.data)
print(iris.target)
X = iris.data
y = iris.target
# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=0)

# Create a random forest classifier
rf = RandomForestClassifier(n_estimators=120, random_state=0)
# Train the random forest classifier
print("\nTraining...")
rf.fit(X_train, y_train)
print("Done Training\n")
# Predict the labels of the testing set
y_pred = rf.predict(X_test)
# Evaluate the performance of the classifier
from sklearn.metrics import accuracy_score
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
feature_names = df.columns                                                          # Get the feature names from the dataset
importances_df = pd.DataFrame({'feature': feature_names, 'importance': rf.feature_importances_})# Create a dataframe with the feature importances and names
importances_df = importances_df.sort_values('importance', ascending=False)          # Sort the dataframe by descending importance

print("Feature Importances")
print(importances_df)
# Create a heatmap of the feature importances
plt.figure(figsize=(8, 5))
sns.heatmap(importances_df.pivot(index='feature', columns='importance', values='importance'), cmap='Blues', annot=True, fmt='.2f')
plt.title('Feature importances')
plt.show()

from sklearn.tree import plot_tree

# Visualize the first decision tree in the random forest
plt.figure(figsize=(10,3))
plot_tree(rf.estimators_[0], filled=True)
plt.show()