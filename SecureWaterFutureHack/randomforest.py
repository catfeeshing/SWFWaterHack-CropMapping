import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import matplotlib.pyplot as plt
import seaborn as sns


info = pd.read_csv("combined_data.csv")
input = info.iloc[:, 1:-1]
mapping = {'X': 'X', 'P': 'A', 'G': 'A', 'F': 'A', 'T': 'A', 'C':'P','D':'P','V':'P','Y':'P'}
output = info['CLASS2'].map(mapping)
features = list(input.columns)
print(features)
print("Shape of input data:", input.shape)
print("Shape of output data:", output.shape)
# print("Shape of codes data:", codes.shape)

xtrain,xtest,ytrain,ytest = train_test_split(input, output, test_size=.20,random_state=0)

# for i in range(20):
#     rf = RandomForestClassifier(n_estimators=20, random_state=0, max_depth=5+i)
#     rf.fit(xtrain, ytrain)
#     ypred = rf.predict(xtest)
#     # Evaluate the performance of the classifier
#     from sklearn.metrics import accuracy_score
#     accuracy = accuracy_score(ytest, ypred)
#     print("Max_Depth:",i+5," | Accuracy:", accuracy)

rf = RandomForestClassifier(n_estimators=100, random_state=0, max_depth=20)
print("\nTraining...")
rf.fit(xtrain, ytrain)
print("Done Training\n")
ypred = rf.predict(xtest)
# Evaluate the performance of the classifier
from sklearn.metrics import accuracy_score
accuracy = accuracy_score(ytest, ypred)
print("Depth:", rf.max_depth," | Accuracy:",accuracy)

from sklearn.metrics import classification_report
print(classification_report(ytest, ypred))

# print(f"OOB Error: {1 - rf.oob_score_:.4f}")

# from sklearn.tree import plot_tree
# Visualize the first decision tree in the random forest
# plt.figure(figsize=(10,8))
# plot_tree(rf.estimators_[0],max_depth=3)
# plt.show()

df = pd.DataFrame(data=input, columns=features)
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
