#!/usr/bin/python3

import joblib
import sys
from matplotlib import pyplot as plt
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit


# read in data dictionary, convert to numpy array
data_dict = joblib.load(
    open("../final_project/final_project_dataset.pkl", "rb"))

data_dict.pop('TOTAL')
features = ["salary", "bonus"]
data = featureFormat(data_dict, features)


# your code below

for point in data:
    salary = point[0]
    bonus = point[1]
    plt.scatter(salary, bonus)

plt.xlabel("salary")
plt.ylabel("bonus")
plt.show()
