#importing the required libraries 
import pandas as pd 
import numpy as np

#defining the scripts for different imputation techniques
def remove_missing_values(data):
    #Identifying columns with missing values
    missing_cols = [col for col in data.columns if data[col].isnull().any()]
    #Removing columns with missing values
    data = data.drop(missing_cols, axis=1)
    return data

def impute_missing_values(data):
    #Identifying columns with missing values
    missing_cols = [col for col in data.columns if data[col].isnull().any()]
    #Calculating mean of the columns with missing values
    means = data[missing_cols].mean()
    #Imputing missing values with mean of the columns
    data[missing_cols] = data[missing_cols].fillna(means)
    #Returning the imputed dataframe
    return data

def extended_impute(data):
    #Identifying columns with missing values
    missing_cols = [col for col in data.columns if data[col].isnull().any()]
    #Iterating through each column with missing values and creating indicator columns
    for col in missing_cols:
        #Creating a new indicator column for missing values
        data[col + '_was_missing'] = data[col].isnull()
    #Calculating mean of the columns with missing values
    means = data[missing_cols].mean()
    #Imputing missing values with mean of the columns
    data[missing_cols] = data[missing_cols].fillna(means)
    #Returning the extended imputed dataframe
    return data

# Uncomment the following lines to test the functions
# #loading the sample dataset
# data = pd.read_csv('C:/Users/yajat/Downloads/Sample_data.csv')
# print(data)

# #User input to choose imputation technique
# perform_impute_tech = int(input("Choose Imputation Technique: 1. Remove Missing Values 2. Impute Missing Values 3. Extended Impute Missing Values : "))
# #Performing the chosen imputation technique
# if perform_impute_tech == 1:
#     result = remove_missing_values(data)
# elif perform_impute_tech == 2:
#     result = impute_missing_values(data)
# elif perform_impute_tech == 3:
#     result = extended_impute(data)
# else: 
#     print("Invalid Choice")
#     result = None
# #Displaying the result
# print(result)





