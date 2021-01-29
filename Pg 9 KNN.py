from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris
import pandas as pd

dataset=load_iris()

X_train, X_test, y_train, y_test = train_test_split(dataset["data"], dataset["target"], random_state=0, test_size=0.25)
classifier=KNeighborsClassifier(n_neighbors=8,p=3,metric='euclidean')
classifier.fit(X_train,y_train)

#predict the test resuts
y_pred=classifier.predict(X_test)

cm=confusion_matrix(y_test,y_pred)
print('Confusion matrix is as follows\n',cm)
print('Accuracy Metrics')
print(classification_report(y_test,y_pred))
print("Correct predicition",accuracy_score(y_test,y_pred))
print("Worng predicition",(1-accuracy_score(y_test,y_pred)))
