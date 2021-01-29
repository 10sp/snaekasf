import pandas as pd
from sklearn.tree import DecisionTreeClassifier
dataset = pd.read_csv('zoo.csv')
dataset = dataset.drop('animal_name',axis = 1)
No_of_data_samples = 60 

train_features = dataset.iloc[:No_of_data_samples, :-1]
train_labels = dataset.iloc[:No_of_data_samples, -1]

test_features = dataset.iloc[No_of_data_samples:, :-1]
test_labels = dataset.iloc[No_of_data_samples:, -1]

tree_model = DecisionTreeClassifier(criterion = 'entropy')

fit_tree_model= tree_model.fit(train_features, train_labels)

classification = fit_tree_model.predict(test_features)
print("The labels output by model: ", classification)
print("Actual Lable: ", test_labels)

print("The prediction accuracy is: ", fit_tree_model.score(test_features, test_labels)*100, "%")
