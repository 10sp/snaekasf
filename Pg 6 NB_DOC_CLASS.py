import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, cohen_kappa_score, confusion_matrix
from sklearn.feature_extraction.text import TfidfVectorizer

data = pd.read_csv('BBC.csv')
x = data['news'].tolist()
y = data['type'].tolist()

vect = TfidfVectorizer(stop_words='english',min_df=2)
X = vect.fit_transform(x)
Y = np.array(y)

X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.20, random_state=42)

model = MultinomialNB()
model.fit(X_train, y_train) 
y_pred = model.predict(X_test)

c_mat = confusion_matrix(y_test,y_pred)
kappa = cohen_kappa_score(y_test,y_pred)
acc = accuracy_score(y_test,y_pred)
print("Confusion Matrix:\n", c_mat)
print("\nKappa: ",kappa)
print("\nAccuracy: ",acc)
