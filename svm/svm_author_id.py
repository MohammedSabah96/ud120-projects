#!/usr/bin/python3

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
    Sara has label 0
    Chris has label 1
"""

from sklearn.metrics import accuracy_score
from sklearn.svm import SVC
import sys
from time import time
sys.path.append("../tools/")


from email_preprocess import preprocess
# features_train and features_test are the features for the training
# and testing datasets, respectively
# labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()


#########################################################
### your code goes here ###

# clf = SVC(kernel="linear")
# clf.fit(features_train, labels_train)

# pred = clf.predict(features_test)

# accuracy = accuracy_score(labels_test, pred)
# print(accuracy)
#########################################################

# t0 = time()
# clf.fit(features_train,labels_train)
# print(f"training time: {time() - t0}")

# t0 = time()
# pred = clf.predict(features_test)
# print(f"predicting time: {time() - t0}")

#########################################################
'''
You'll be Provided similar code in the Quiz
But the Code provided in Quiz has an Indexing issue
The Code Below solves that issue, So use this one
'''

# features_train = features_train[:int(len(features_train)/100)]
# labels_train = labels_train[:int(len(labels_train)/100)]

#########################################################
clf = SVC(C=1,kernel="rbf")
clf.fit(features_train, labels_train)

pred = clf.predict(features_test)

print(pred[10], pred[26], pred[50])

count = 0
i = 0
print(len(pred))
while i < len(pred):
    if pred[i] == 1:
        count += 1

    i += 1

print(count)
accuracy = accuracy_score(labels_test, pred)
print(accuracy)
