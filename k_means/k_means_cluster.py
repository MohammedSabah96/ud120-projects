#!/usr/bin/python3

""" 
    Skeleton code for k-means clustering mini-project.
"""

import joblib
import numpy as np
import matplotlib.pyplot as plt
import sys
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit

def Draw(pred, features, poi, mark_poi=False, name="image.png", f1_name="feature 1", f2_name="feature 2"):
    """ some plotting code designed to help you visualize your clusters """

    # plot each cluster with a different color--add more colors for
    # drawing more than five clusters
    colors = ["b", "c", "k", "m", "g"]
    for ii, pp in enumerate(pred):
        plt.scatter(features[ii][0], features[ii][1], color=colors[pred[ii]])

    # if you like, place red stars over points that are POIs (just for funsies)
    if mark_poi:
        for ii, pp in enumerate(pred):
            if poi[ii]:
                plt.scatter(features[ii][0], features[ii]
                            [1], color="r", marker="*")
    plt.xlabel(f1_name)
    plt.ylabel(f2_name)
    plt.savefig(name)
    plt.show()


# load in the dict of dicts containing all the data on each person in the dataset
data_dict = joblib.load(
    open("../final_project/final_project_dataset.pkl", "rb"))
# there's an outlier--remove it!
data_dict.pop("TOTAL", 0)

exercised_stock_options = []
for person, features in data_dict.items():
    if features['exercised_stock_options'] != 'NaN':
        exercised_stock_options.append(features['exercised_stock_options'])

print(f"Min of exercised_stock_options is: {np.min(exercised_stock_options)}")
print(f"Max of exercised_stock_options is: {np.max(exercised_stock_options)}")

salary = []
for person, features in data_dict.items():
    if features['salary'] != 'NaN':
        salary.append(features['salary'])

print(f"Min of salary is: {np.min(salary)}")
print(f"Max of salary is: {np.max(salary)}")

# the input features we want to use
# can be any key in the person-level dictionary (salary, director_fees, etc.)
feature_1 = "salary"
feature_2 = "exercised_stock_options"
# feature_3="total_payments"
poi = "poi"
features_list = [poi, feature_1, feature_2]
data = featureFormat(data_dict, features_list)
poi, finance_features = targetFeatureSplit(data)


# in the "clustering with 3 features" part of the mini-project,
# you'll want to change this line to
# for f1, f2, _ in finance_features:
# (as it's currently written, the line below assumes 2 features)
for f1, f2 in finance_features:
    plt.scatter(f1, f2)
plt.show()

# cluster here; create predictions of the cluster labels
# for the data and store them to a list called pred
from sklearn.cluster import KMeans
from sklearn.preprocessing import MinMaxScaler

scaler = MinMaxScaler()
rescaled_finance_features=scaler.fit_transform(finance_features)
k_mean = KMeans(n_clusters=2).fit(rescaled_finance_features)

pred = k_mean.labels_

for f1, f2 in rescaled_finance_features:
    plt.scatter(f1, f2)
plt.show()

# rename the "name" parameter when you change the number of features
# so that the figure gets saved to a different file
try:
    Draw(pred, rescaled_finance_features, poi, mark_poi=False,
         name="clusters2.pdf", f1_name=feature_1, f2_name=feature_2)
except NameError:
    print("No predictions object named pred found, no clusters to plot")


salary = 200000
exercised_stock_options = 1000000
rescale_salary = float(salary - 477)/(1111258 - 477)
rescale_exercised_stock_options = float(exercised_stock_options - 3285)/(34348384 - 3285)

print(f"rescaled salary for 200,000$ is: {rescale_salary}")
print(f"rescaled exercised_stock_options for 1,000,000$ is: {rescale_exercised_stock_options}")

