import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import Perceptron

dataset = pd.read_csv('/content/extracted.csv')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 64].values

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.40, random_state = 0)
print(len(X_train))
print(len(X_test))
print(len(y_train))
print(len(y_test))

per = Perceptron()
per.fit(X_train,y_train)

pred = per.predict(X_test)
print(pred)

a=y_test
count = 0
for i in range(len(pred)):
  if pred[i]==a[i]:
    count=count+1
print(count)

from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test,pred)
print(cm)


#8
print("Training score : " + str(per.score(X_train,y_train)))
print("Test Score : " + str(per.score(X_test,y_test)))