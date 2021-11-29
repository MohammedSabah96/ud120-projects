#!/usr/bin/python3

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import joblib

enron_data = joblib.load(
    open("../final_project/final_project_dataset.pkl", "rb"))

# print(f"how many people in our dataset: {len(enron_data)}")
# print(f"How many features each person has: {len(enron_data['METTS MARK'])}")

# count = 0
# for person, features in enron_data.items():
#     if features['poi'] == True:
#         count += 1


# print(f"how many people have POI (people of interest) == 1 or True: {count}")

# print(f"total stock value for  PRENTICE JAMES:  {enron_data['PRENTICE JAMES']['total_stock_value']}")
# print(f"from COLWELL WESLEY to POI: {enron_data['COLWELL WESLEY']['from_this_person_to_poi']}")
# print(f"exercised_stock_options for SKILLING JEFFREY K: {enron_data['SKILLING JEFFREY K']['exercised_stock_options']}")
# print(f"total_payments for SKILLING JEFFREY K : {enron_data['SKILLING JEFFREY K']['total_payments']}")
# print(f"total_payments for LAY KENNETH L : {enron_data['LAY KENNETH L']['total_payments']}")
# print(f"total_payments for FASTOW ANDREW S : {enron_data['FASTOW ANDREW S']['total_payments']}")

# salary_count = 0
# email_address_count = 0
# for person, features in enron_data.items():
#     if features['salary'] != 'NaN':
#         salary_count += 1
#     if features['email_address'] != 'NaN':
#         email_address_count+=1


# print(salary_count)
# print(email_address_count)

# count_NaN = 0
# count_poi = 0
# for person, features in enron_data.items():
#     if features['total_payments'] == 'NaN':
#         count_NaN += 1
#         if features['poi'] == True:
#             count_poi += 1


# print(count_NaN)
# print(f"{(count_poi/len(enron_data))*100}%")
