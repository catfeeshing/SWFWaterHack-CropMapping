import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import matplotlib.pyplot as plt
import seaborn as sns


info = pd.read_csv("combined_dataBoth.csv").iloc[:190000]
# mapping = {'X': 0, 'P': 1, 'G': 1, 'F': 1, 'T': 1, 'C':2,'D':2,'V':2,'Y':2}
# info['gen'] = info['CLASS2'].map(mapping)

output = info['CLASS2']
input = info.drop('CLASS2',axis=1).drop('UniqueID',axis=1)
# print(input)
# print(output)
features = list(input.columns)
print(features)
print("Shape of input data:", input.shape)
print("Shape of output data:", output.shape)
# print("Shape of codes data:", codes.shape)

xtrain,xtest,ytrain,ytest = train_test_split(input, output, test_size=.2,random_state=2)

rf = RandomForestClassifier(n_estimators=83, random_state=3, max_depth=15)
print("\nTraining...")
rf.fit(xtrain, ytrain)
print("Done Training\n")
ypred = rf.predict(xtest)
# comparison = pd.DataFrame({'Answers': ytest, 'Predictions': ypred})
# comparison.to_csv("comparison5.csv",index=False)
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

inputPrediction = pd.read_csv("clean2020.csv")
zones = inputPrediction["UniqueID"]
inputPrediction = inputPrediction.drop("UniqueID",axis=1)
predictions = rf.predict(inputPrediction)
outputPrediction = pd.DataFrame({'zones': zones, 'predictions': predictions})
outputPrediction.to_csv("predictions2020.csv", index=False)

# df = info.iloc[2000:5000]
# # Define the colors and markers for each class
# colors = {'X': 'red', 'P': 'blue', 'G': 'green', 'F':'orange', 'T':'purple', 'C':'brown', 'D':'pink', 'V':'gray', 'Y':'olive'}
# markers = {'X': 'x', 'P': 'p', 'G': '.', 'F':'^', 'T':'*', 'C':'o', 'D':'d', 'V':'v', 'Y':'+'}

# # Create the scatterplot
# fig, ax = plt.subplots()
# for class_label in df['CLASS2'].unique():
#     class_data = df[df['CLASS2'] == class_label]
#     ax.scatter(class_data['et'], class_data['srad'], color=colors[class_label], marker=markers[class_label], label=class_label)

# # Add axis labels and legend
# ax.set_xlabel('et')
# ax.set_ylabel('srad')
# ax.legend()

# # Show the plot
# plt.show()
