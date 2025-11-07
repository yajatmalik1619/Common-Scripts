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

    # Uncomment the following block to use pandas inherent functions for imputation (or vice versa)
    # #Using pandas functions for mean, median and mode calculations
    # #Calculating mean of the columns with missing values
    # means = data[missing_cols].mean() #uncomment this line to use pandas mean() function
    # #Calculating median of the columns with missing values
    # median = data[missing_cols].median()
    # #Calculating mode of the columns with missing values (using iloc as mode() returns a dataframe and not a series)
    # mode = data[missing_cols].mode().iloc[0]
    # #Imputation method selection by user using inherent pandas functions
    # method = int(input("Choose Imputation Method: 1. Mean 2. Median 3. Mode: "))
    # if method == 1:
    #     #Imputing missing values with mean of the columns
    #     data[missing_cols] = data[missing_cols].fillna(means)
    # elif method == 2:
    #     #Imputing missing values with median of the columns
    #     data[missing_cols] = data[missing_cols].fillna(median)
    # elif method == 3:
    #     #Imputing missing values with mode of the columns
    #     data[missing_cols] = data[missing_cols].fillna(mode)
    # else:
    #     print("Invalid Choice")
    #     return None

    # Comment the block below to use pandas inherent functions for imputation (or vice versa)
    #Using custom functions for mean, median and mode calculations as well as inputting missing values
    #calculating mean using custom function
    means_list = []  
    for col in missing_cols:
        total = data[col].sum()
        count = data[col].count()
        mean = total / count
        means_list.append(mean)
    means = pd.Series(means_list, index=missing_cols)
    
    #calculating median using custom function
    median_list = []
    for col in missing_cols:
        nan_removed = [val for val in data[col] if not np.isnan(val)]
        sorted_list = sorted(nan_removed)
        n = len(sorted_list)
        if n % 2 == 0:
            median_val = (sorted_list[n//2 - 1] + sorted_list[n//2]) / 2
        else:
            median_val = sorted_list[n//2]
        median_list.append(median_val)
    median = pd.Series(median_list, index=missing_cols)
    #calculating mode using custom function
    mode_list = []
    for col in missing_cols:
        demo_dict = {}
        nan_removed = [val for val in data[col] if not np.isnan(val)]
        for val in nan_removed:
            if val in demo_dict:
                demo_dict[val] += 1
            else:
                demo_dict[val] = 1
        if not demo_dict:
            mode_list.append(np.nan)
            continue
        else:
            key = demo_dict.keys()
            max_val = -1
            mode_val = None
            for k in key:
                if demo_dict[k] > max_val:
                    max_val = demo_dict[k]
                    mode_val = k
            mode_list.append(mode_val)
    mode = pd.Series(mode_list, index=missing_cols)
    method = int(input("Choose Imputation Method: 1. Mean 2. Median 3. Mode: "))
    if method == 1:
        #Imputing missing values with mean of the columns
        for col in missing_cols:
            i = 0
            for val in data[col]:
                if np.isnan(val):
                    data.at[i, col] = means[col]
                i += 1
    elif method == 2:
        #Imputing missing values with median of the columns
        for col in missing_cols:
            i = 0
            for val in data[col]:
                if np.isnan(val):
                    data.at[i, col] = median[col]
                i += 1
    elif method == 3:
        #Imputing missing values with mode of the columns
        for col in missing_cols:
            i = 0
            for val in data[col]:
                if np.isnan(val):
                    data.at[i, col] = mode[col]
                i += 1
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
        
    # Uncomment the following block to use pandas inherent functions for imputation (or vice versa)
    # #Using pandas functions for mean, median and mode calculations
    # #Calculating mean of the columns with missing values
    # means = data[missing_cols].mean() #uncomment this line to use pandas mean() function
    # #Calculating median of the columns with missing values
    # median = data[missing_cols].median()
    # #Calculating mode of the columns with missing values (using iloc as mode() returns a dataframe and not a series)
    # mode = data[missing_cols].mode().iloc[0]
    # #Imputation method selection by user using inherent pandas functions
    # method = int(input("Choose Imputation Method: 1. Mean 2. Median 3. Mode: "))
    # if method == 1:
    #     #Imputing missing values with mean of the columns
    #     data[missing_cols] = data[missing_cols].fillna(means)
    # elif method == 2:
    #     #Imputing missing values with median of the columns
    #     data[missing_cols] = data[missing_cols].fillna(median)
    # elif method == 3:
    #     #Imputing missing values with mode of the columns
    #     data[missing_cols] = data[missing_cols].fillna(mode)
    # else:
    #     print("Invalid Choice")
    #     return None

    # Comment the block below to use pandas inherent functions for imputation (or vice versa)
    #Using custom functions for mean, median and mode calculations as well as inputting missing values
    #calculating mean using custom function
    means_list = []  
    for col in missing_cols:
        total = data[col].sum()
        count = data[col].count()
        mean = total / count
        means_list.append(mean)
    means = pd.Series(means_list, index=missing_cols)
    
    #calculating median using custom function
    median_list = []
    for col in missing_cols:
        nan_removed = [val for val in data[col] if not np.isnan(val)]
        sorted_list = sorted(nan_removed)
        n = len(sorted_list)
        if n % 2 == 0:
            median_val = (sorted_list[n//2 - 1] + sorted_list[n//2]) / 2
        else:
            median_val = sorted_list[n//2]
        median_list.append(median_val)
    median = pd.Series(median_list, index=missing_cols)
    #calculating mode using custom function
    mode_list = []
    for col in missing_cols:
        demo_dict = {}
        nan_removed = [val for val in data[col] if not np.isnan(val)]
        for val in nan_removed:
            if val in demo_dict:
                demo_dict[val] += 1
            else:
                demo_dict[val] = 1
        if not demo_dict:
            mode_list.append(np.nan)
            continue
        else:
            key = demo_dict.keys()
            max_val = -1
            mode_val = None
            for k in key:
                if demo_dict[k] > max_val:
                    max_val = demo_dict[k]
                    mode_val = k
            mode_list.append(mode_val)
    mode = pd.Series(mode_list, index=missing_cols)
    method = int(input("Choose Imputation Method: 1. Mean 2. Median 3. Mode: "))
    if method == 1:
        #Imputing missing values with mean of the columns
        for col in missing_cols:
            i = 0
            for val in data[col]:
                if np.isnan(val):
                    data.at[i, col] = means[col]
                i += 1
    elif method == 2:
        #Imputing missing values with median of the columns
        for col in missing_cols:
            i = 0
            for val in data[col]:
                if np.isnan(val):
                    data.at[i, col] = median[col]
                i += 1
    elif method == 3:
        #Imputing missing values with mode of the columns
        for col in missing_cols:
            i = 0
            for val in data[col]:
                if np.isnan(val):
                    data.at[i, col] = mode[col]
                i += 1
    else:
        print("Invalid Choice")
        return None
    #Returning the imputed dataframe
    return data

#4. REMOVE ROWS WITH MISSING VALUES (incase of large datasets containing a large number of rows)
def remove_rows_with_missing_values(data):
    #Removing rows with any missing values
    data = data.dropna(axis=0)
    return data

# #Uncomment the following lines to test the functions on a provided dataset
# #loading the sample dataset
data = pd.read_csv('C:\\Users\\Kanishka\\Code\\Common-Scripts\\Sample_data.csv')
#setting display option to show all columns
pd.set_option('display.max_columns', None)
print(data)
#User input to choose imputation technique
perform_impute_tech = int(input("Choose Imputation Technique: 1. Remove Missing Values 2. Impute Missing Values 3. Extended Impute Missing Values 4. Remove Rows with Missing Values: "))
#Performing the chosen imputation technique
if perform_impute_tech == 1:
    result = remove_missing_values(data)
elif perform_impute_tech == 2:
    result = impute_missing_values(data)
elif perform_impute_tech == 3:
    result = extended_impute(data)
elif perform_impute_tech == 4:
    result = remove_rows_with_missing_values(data)
else: 
    print("Invalid Choice")
    result = None
#Displaying the result
print(result)






