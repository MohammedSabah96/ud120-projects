#!/usr/bin/python

from sklearn.ensemble import AdaBoostClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt
from prep_terrain_data import makeTerrainData
from class_vis import prettyPicture

features_train, labels_train, features_test, labels_test = makeTerrainData()


# the training data (features_train, labels_train) have both "fast" and "slow"
# points mixed together--separate them so we can give them different colors
# in the scatterplot and identify them visually
grade_fast = [features_train[ii][0]
              for ii in range(0, len(features_train)) if labels_train[ii] == 0]
bumpy_fast = [features_train[ii][1]
              for ii in range(0, len(features_train)) if labels_train[ii] == 0]
grade_slow = [features_train[ii][0]
              for ii in range(0, len(features_train)) if labels_train[ii] == 1]
bumpy_slow = [features_train[ii][1]
              for ii in range(0, len(features_train)) if labels_train[ii] == 1]


# initial visualization
# plt.xlim(0.0, 1.0)
# plt.ylim(0.0, 1.0)
# plt.scatter(bumpy_fast, grade_fast, color="b", label="fast")
# plt.scatter(grade_slow, bumpy_slow, color="r", label="slow")
# plt.legend()
# plt.xlabel("bumpiness")
# plt.ylabel("grade")
# plt.show()
################################################################################


# your code here!  name your classifier object clf if you want the
# visualization code (prettyPicture) to show you the decision boundary

"""
First let's use KNN algorithm and let's see
with k=18 or k=16 we got accuracy 94%
with k=8 we got accuracy 94.4%
and with default we got 92%
"""
clf = KNeighborsClassifier(n_neighbors=8)
"""
Second let's use Random Forect algorithm and let's see    
accuracy 92.4% with n_estimators=150, min_samples_split=50
"""
# clf = RandomForestClassifier(n_estimators=150, min_samples_split=50)

"""
Third let's use AdaBoost algorithm and let's see
accuracy 92.8% with n_estimators=100,learning_rate=0.19
"""
# clf = AdaBoostClassifier(n_estimators=100,learning_rate=0.19)

clf.fit(features_train, labels_train)
pred = clf.predict(features_test)

accuracy = accuracy_score(labels_test, pred)
print(accuracy)


try:
    prettyPicture(clf, features_test, labels_test)
except NameError:
    pass
