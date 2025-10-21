#importing the required libraries 
import pandas as pd 
import numpy as np

#defining the scripts for different categorical encoding 
# 1. ORDINAL ENCODING
#function requires two arguments: dataframe and low cardinality threshold (by default set to 7)
def ordinal_encode(data, low_cardinality=7):
    #Identifying categorical columns
    object_cols = [col for col in data.columns if data[col].dtype == 'object']
    #Filtering categorical columns with low cardinality
    low_cardinality_cols = [col for col in data.columns if data[col].dtype == 'category']
    #Defining an ordinal mapping dictionary
    ordinal_mapping = {}
    #Iterating through each object column
    for col in object_cols:
        #Checking for low cardinality
        if data[col].nunique() < low_cardinality:
            #Adding to categorical columns list
            low_cardinality_cols.append(col)
    #Iterating through each categorical column for ordinal encoding
    for col in low_cardinality_cols:
        #Resetting the ordinal mapping dictionary for each column
        ordinal_mapping = {}
        #Getting unique categories in the column
        unique_cats = data[col].unique()
        #Creating a mapping for ordinal encoding
        i = 0
        for cat in unique_cats:
            ordinal_mapping[cat] = i
            i = i+1
        #Applying ordinal encoding based on the mapping dictionary
        data[col] = data[col].map(ordinal_mapping)
    #Returning the ordinal encoded dataframe
    return data

#2. ONE-HOT ENCODING
#function requires two arguments: dataframe and low cardinality threshold (by default set to 7)
def one_hot_encode(data, low_cardinality=7):
    #Identifying categorical columns
    object_cols = [col for col in data.columns if data[col].dtype == 'object']
    #Filtering categorical columns with low cardinality
    low_cardinality_cols = [col for col in data.columns if data[col].dtype == 'category']
    #Iterating through each object column
    for col in object_cols:
        #Checking for low cardinality
        if data[col].nunique() < low_cardinality:
            #Adding to low cardinality columns list
            low_cardinality_cols.append(col)
    #Iterating through each categorical column for one hot encoding
    for col in low_cardinality_cols:
        #Getting unique categories in the column
        unique_cats = data[col].unique()
        #Creating one hot encoded columns
        for cat in unique_cats:
            #creating a new column for each category
            cat_value = []
            for value in data[col]:
                if value == cat:
                    cat_value.append(1) 
                else: 
                    cat_value.append(0)
            data[cat] = cat_value

    #Removing the original categorical column
    data = data.drop(low_cardinality_cols, axis=1)
    #Returning the one-hot encoded dataframe
    return data

# #Uncomment the following lines to test the functions on a provided dataset
# #loading the sample dataset
# data = pd.read_csv('Sample_data.csv')
# #setting display option to show all columns
# pd.set_option('display.max_columns', None)
# #user input to choose encoding technique
# perform_encoding_tech = int(input("Choose Encoding Technique: 1. Ordinal Encoding 2. One-Hot Encoding : ")  )
# #performing the chosen encoding technique
# if perform_encoding_tech == 1:
#     result = ordinal_encode(data)       
# elif perform_encoding_tech == 2:
#     result = one_hot_encode(data)
# else:
#     print("Invalid Choice")
#     result = None
# #displaying the result
# print(result)


