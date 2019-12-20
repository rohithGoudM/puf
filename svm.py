import timeit
start = timeit.default_timer()

#1
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#2
dataset = pd.read_csv('data/features.csv')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 64].values

#3
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.40, random_state = 0)

#5
from sklearn.svm import SVC
classifier = SVC(kernel = 'rbf',gamma = 0.001, random_state = 0,decision_function_shape='ovo')
classifier.fit(X_train,y_train)

#6
y_pred = classifier.predict(X_test)


#7
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test,y_pred)
print(cm)

#8
print("Training score : " + str(classifier.score(X_train,y_train)))
print("Test Score : " + str(classifier.score(X_test,y_test)))

#Your statements here

stop = timeit.default_timer()
print('Time: ', stop - start) 