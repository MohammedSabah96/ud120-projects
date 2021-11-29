#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """

    cleaned_data = []

    # your code goes here
    i = 0
    while i < len(predictions):
        residual_error = net_worths[i] - predictions[i]
        if residual_error > -31:
            cleaned_data.append((ages[i], net_worths[i], residual_error))
        i += 1
    return cleaned_data
