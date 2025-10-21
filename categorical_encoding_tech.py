#importing the required libraries 
import pandas as pd 
import numpy as np

#defining the scripts for different ordinal encoding 
def ordinal_encode(data):
    #Identifying categorical columns
    object_cols = [col for col in data.columns if data[col].dtype == 'object']
    #Creating a copy of the original dataframe to perform ordinal encoding
    x_ordinal = data.copy()
    #Filtering categorical columns with low cardinality
    categorical_cols = []
    #Taking input to set as the threshold for low cardinality
    low_cardinality = int(input("Set threshold for low cardinality: "))
    #Defining an ordinal mapping dictionary
    ordinal_mapping = {}
    #Iterating through each object column
    for col in object_cols:
        #Checking for low cardinality
        if data[col].nunique() < low_cardinality:
            #Adding to categorical columns list
            categorical_cols.append(col)
    #Iterating through each categorical column for ordinal encoding
    for col in categorical_cols:
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
        x_ordinal[col] = x_ordinal[col].map(ordinal_mapping)
    #Returning the ordinal encoded dataframe
    return x_ordinal

def one_hot_encode(data):
    #Identifying categorical columns
    object_cols = [col for col in data.columns if data[col].dtype == 'object']
    #Creating a copy of the original dataframe to perform one-hot encoding
    x_one_hot = data.copy()
    #Filtering categorical columns with low cardinality
    low_cardinality_cols = []
    #Taking input to set as the threshold for low cardinality
    low_cardinality = int(input("Set threshold for low cardinality: "))
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
            for value in x_one_hot[col]:
                if value == cat:
                    cat_value.append(1) 
                else: 
                    cat_value.append(0)
            x_one_hot[cat] = cat_value

    #Removing the original categorical column
    x_one_hot = x_one_hot.drop(low_cardinality_cols, axis=1)
    #Returning the one-hot encoded dataframe
    return x_one_hot

#loading the sample dataset
data = pd.read_csv('C:/Users/yajat/Downloads/Sample_data.csv')

#user input to choose encoding technique
perform_encoding_tech = int(input("Choose Encoding Technique: 1. Ordinal Encoding 2. One-Hot Encoding : ")  )
#performing the chosen encoding technique
if perform_encoding_tech == 1:
    result = ordinal_encode(data)       
elif perform_encoding_tech == 2:
    result = one_hot_encode(data)
else:
    print("Invalid Choice")
    result = None
#displaying the result
print(result)


