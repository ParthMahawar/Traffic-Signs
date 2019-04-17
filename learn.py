import numpy as np
from image_prepare import getimgvalues
from sklearn.svm import SVC
#from sklearn.svm import LinearSVC                              Long Training Time, Very Quick Predictions, Accuracy 74.4%
#from sklearn.linear_model import PassiveAggressiveClassifier   Accuracy 69.8%
#from sklearn.linear_model import RidgeClassifier               Accuracy 73.8%
#from sklearn.linear_model import SGDClassifier                 Accuracy 69.4%
#from sklearn.neighbors import KNeighborsClassifier             VERY INEFFICIENT, Accuracy about 51%
from pickle import dump

X = getimgvalues("C:/users/Parth/desktop/Std_train/0/", -1)
Y = [0] * len(X)

print(0)

model = SVC()
for i in range(1, 43):
    Xvals = getimgvalues("C:/users/Parth/desktop/Std_train/"+str(i)+"/", -1)
    print(i)
    Yvals = [i] * len(Xvals)
    X = np.concatenate((X, Xvals))
    Y.extend(Yvals)

model.fit(X, Y)
print(model.coef_)

dump(model, open("C:/users/parth/desktop/save.dat", "wb"))