#importing the required libraries 
import pandas as pd 
import numpy as np
import statistics as stats

#defining the scripts for different imputation techniques

#1. REMOVE MISSING VALUES
def remove_missing_values(data):
    #Identifying columns with missing values
    missing_cols = [col for col in data.columns if data[col].isnull().any()]
    #Removing columns with missing values
    data = data.drop(missing_cols, axis=1)
    return data

#2. IMPUTE MISSING VALUES
def impute_missing_values(data):
    #Identifying numerical columns with missing values
    missing_cols = [col for col in data.columns if data[col].isnull().any() and data[col].dtype in ["int64" , "float64"]]
    #Calculating mean of the columns with missing values
    means = data[missing_cols].mean()
    #Calculating median of the columns with missing values
    median = data[missing_cols].median()
    #Calculating mode of the columns with missing values (using iloc as mode() returns a series)
    mode = data[missing_cols].mode().iloc[0]
    #data[missing_cols] = data[missing_cols].fillna(mode)
    method = int(input("Choose Imputation Method: 1. Mean 2. Median 3. Mode: "))
    if method == 1:
        #Imputing missing values with mean of the columns
        data[missing_cols] = data[missing_cols].fillna(means)
    elif method == 2:
        #Imputing missing values with median of the columns
        data[missing_cols] = data[missing_cols].fillna(median)
    elif method == 3:
        #Imputing missing values with mode of the columns
        data[missing_cols] = data[missing_cols].fillna(mode)
    else:
        print("Invalid Choice")
        return None
    #Returning the imputed dataframe
    return data

#3. EXTENDED IMPUTE MISSING VALUES
def extended_impute(data):
    #Identifying numerical columns with missing values
    missing_cols = [col for col in data.columns if data[col].isnull().any() and data[col].dtype in ["int64" , "float64"]]
    #Iterating through each column with missing values and creating indicator columns
    for col in missing_cols:
        #Creating a new indicator column for missing values
        data[col + '_was_missing'] = data[col].isnull()
    #Calculating mean of the columns with missing values
    means = data[missing_cols].mean()
        #Calculating median of the columns with missing values
    median = data[missing_cols].median()
    #Calculating mode of the columns with missing values (using iloc as mode() returns a series)
    mode = data[missing_cols].mode().iloc[0]
    #data[missing_cols] = data[missing_cols].fillna(mode)
    method = int(input("Choose Imputation Method: 1. Mean 2. Median 3. Mode: "))
    if method == 1:
        #Imputing missing values with mean of the columns
        data[missing_cols] = data[missing_cols].fillna(means)
    elif method == 2:
        #Imputing missing values with median of the columns
        data[missing_cols] = data[missing_cols].fillna(median)
    elif method == 3:
        #Imputing missing values with mode of the columns
        data[missing_cols] = data[missing_cols].fillna(mode)
    else:
        print("Invalid Choice")
        return None
    #Returning the extended imputed dataframe
    return data

#4. REMOVE ROWS WITH MISSING VALUES (incase of large datasets containing a large number of rows)
def remove_rows_with_missing_values(data):
    #Removing rows with any missing values
    data = data.dropna(axis=0)
    return data

# #Uncomment the following lines to test the functions on a provided dataset
# #loading the sample dataset
# data = pd.read_csv('Sample_data.csv')
# #setting display option to show all columns
# pd.set_option('display.max_columns', None)
# print(data)
# #User input to choose imputation technique
# perform_impute_tech = int(input("Choose Imputation Technique: 1. Remove Missing Values 2. Impute Missing Values 3. Extended Impute Missing Values 4. Remove Rows with Missing Values: "))
# #Performing the chosen imputation technique
# if perform_impute_tech == 1:
#     result = remove_missing_values(data)
# elif perform_impute_tech == 2:
#     result = impute_missing_values(data)
# elif perform_impute_tech == 3:
#     result = extended_impute(data)
# elif perform_impute_tech == 4:
#     result = remove_rows_with_missing_values(data)
# else: 
#     print("Invalid Choice")
#     result = None
# #Displaying the result
# print(result)






