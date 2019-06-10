
import pandas as pd
import pickle

data = pd.read_csv('result.csv')

feature_names = ['f1','f2','f3','f4','f5','f6','f7','f8','f9','f10','f11','f12','f13','f14','f15','f16','f17','f18','f19','f20','f21','f22','f23','f24','f25','f26']

X = data[feature_names]
y = data['command']

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)

from sklearn.svm import SVC

svm = SVC(gamma='scale', kernel='poly')
svm.fit(X_train, y_train)
print('Accuracy of SVM classifier on training set: {:.2f}'
     .format(svm.score(X_train, y_train)))
print('Accuracy of SVM classifier on test set: {:.2f}'
     .format(svm.score(X_test, y_test)))

# save the model to disk
filename = 'svm.sav'
pickle.dump(svm, open(filename, 'wb'))
