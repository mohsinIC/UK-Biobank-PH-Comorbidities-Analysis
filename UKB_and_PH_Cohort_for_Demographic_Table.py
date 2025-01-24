#!/usr/bin/env python
# coding: utf-8

# **The purpose of this code is to include demographic (BMI,Smoking,Sex,Age Groups, IMD) vairables to get the statistical data for UK biobank and PH Cohort.**

# <div style="background-color: #d3f5d3; padding: 10px;">
#     <h2><center>1. Importing Libraries</center></h2>
# </div>

# In[ ]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import matplotlib.pyplot as plt
#import seaborn as sns



#pd.set_option('display.max_rows', None)
#pd.reset_option('display.max_rows', None)
#pd.set_option('display.max_columns', None)
#pd.reset_option('display.max_columns', None)


# In[ ]:


#!pip install scikit-learn


# <div style="background-color: #d3f5d3; padding: 10px;">
#     <h2><center>2. Complete Structured Dataset (with ICD10 Codes)</center></h2>
# </div>

# **2a. Imported dataset from UK Biobank (only with ICD10 codes).**
# 
# **This dataset contains the variables such as "Participant IDs", "Year of Birth","Month of Birth", "Ethnicity", "Sex"  and having both ICD10 and Main ICD10 Codes (with Diagnosis Dates), Diseases Names, Birth and Death Records**

# In[ ]:


### Importing the dataset
d = []
d = pd.read_csv('dataset.csv')
ICD10_dataset = d
## initialize df equal to dataset
ICD10_dataset = ICD10_dataset.sort_values(by=['Participant ID'])




# Create dictionaries to store unique counts, row counts, NaN counts, and empty counts
unique_counts_ICD10_dataset = {}
row_counts_ICD10_dataset = {}
nan_counts_ICD10_dataset = {}
empty_counts_ICD10_dataset = {}

# Loop through columns and count unique items, row counts, NaN counts, and empty counts
for column_ICD10_dataset in ICD10_dataset.columns:
    unique_count_ICD10_dataset = ICD10_dataset[column_ICD10_dataset].nunique()
    row_count_ICD10_dataset = len(ICD10_dataset[column_ICD10_dataset])
    nan_count_ICD10_dataset = ICD10_dataset[column_ICD10_dataset].isna().sum()  # Count NaN values
    empty_count_ICD10_dataset = ICD10_dataset[column_ICD10_dataset].eq('').sum()  # Count empty string values

    unique_counts_ICD10_dataset[column_ICD10_dataset] = [unique_count_ICD10_dataset]
    row_counts_ICD10_dataset[column_ICD10_dataset] = [row_count_ICD10_dataset]
    nan_counts_ICD10_dataset[column_ICD10_dataset] = [nan_count_ICD10_dataset]
    empty_counts_ICD10_dataset[column_ICD10_dataset] = [empty_count_ICD10_dataset]

# Create DataFrames from the dictionaries
unique_counts_ICD10_databank = []
row_counts_ICD10_databank = []
nan_counts_ICD10_databank = []
empty_counts_ICD10_databank = []

unique_counts_ICD10_databank = pd.DataFrame(unique_counts_ICD10_dataset, index=['Unique Count'])
row_counts_ICD10_databank = pd.DataFrame(row_counts_ICD10_dataset, index=['Row Count'])
nan_counts_ICD10_databank = pd.DataFrame(nan_counts_ICD10_dataset, index=['NaN Count'])
empty_counts_ICD10_databank = pd.DataFrame(empty_counts_ICD10_dataset, index=['Empty Count'])

# Concatenate the DataFrames
result_ICD10_dataset = []
result_ICD10_dataset = pd.concat([unique_counts_ICD10_databank, row_counts_ICD10_databank, nan_counts_ICD10_databank, empty_counts_ICD10_databank])

# Display the combined DataFrame
#print("ICD10-base Clinal Dataset:")
print()
#display(result_ICD10_dataset)
print()
#ICD10_dataset.head(3)


# **2b. Extract the Variables related to "ICD10 Codes" and its related diseases names and Diagnosis Dates**

# In[ ]:


### initialize df1 as ICD10 codes dataset
ICD10_Codes_Dates_Table = []
ICD10_Codes_Dates_Table = ICD10_dataset.iloc[:, :249]




# Create dictionaries to store unique counts, row counts, NaN counts, and empty counts
unique_counts_ICD10_Codes_Dates_Table = {}
row_counts_ICD10_Codes_Dates_Table = {}
nan_counts_ICD10_Codes_Dates_Table = {}
empty_counts_ICD10_Codes_Dates_Table = {}

# Loop through columns and count unique items, row counts, NaN counts, and empty counts
for column_ICD10_Codes_Dates_Table in ICD10_Codes_Dates_Table.columns:
    unique_count_ICD10_Codes_Dates_Table = ICD10_Codes_Dates_Table[column_ICD10_Codes_Dates_Table].nunique()
    row_count_ICD10_Codes_Dates_Table = len(ICD10_Codes_Dates_Table[column_ICD10_Codes_Dates_Table])
    nan_count_ICD10_Codes_Dates_Table = ICD10_Codes_Dates_Table[column_ICD10_Codes_Dates_Table].isna().sum()  # Count NaN values
    empty_count_ICD10_Codes_Dates_Table = ICD10_Codes_Dates_Table[column_ICD10_Codes_Dates_Table].eq('').sum()  # Count empty string values

    unique_counts_ICD10_Codes_Dates_Table[column_ICD10_Codes_Dates_Table] = [unique_count_ICD10_Codes_Dates_Table]
    row_counts_ICD10_Codes_Dates_Table[column_ICD10_Codes_Dates_Table] = [row_count_ICD10_Codes_Dates_Table]
    nan_counts_ICD10_Codes_Dates_Table[column_ICD10_Codes_Dates_Table] = [nan_count_ICD10_Codes_Dates_Table]
    empty_counts_ICD10_Codes_Dates_Table[column_ICD10_Codes_Dates_Table] = [empty_count_ICD10_Codes_Dates_Table]

# Create DataFrames from the dictionaries
unique_counts_ICD10_Codes_Dates_Table_databank = []
row_counts_ICD10_Codes_Dates_Table_databank = []
nan_counts_ICD10_ICD10_Codes_Dates_Table_databank = []
empty_counts_ICD10_ICD10_Codes_Dates_Table_databank = []

unique_counts_ICD10_Codes_Dates_Table_databank = pd.DataFrame(unique_counts_ICD10_Codes_Dates_Table, index=['Unique Count'])
row_counts_ICD10_Codes_Dates_Table_databank = pd.DataFrame(row_counts_ICD10_Codes_Dates_Table, index=['Row Count'])
nan_counts_ICD10_Codes_Dates_Table_databank = pd.DataFrame(nan_counts_ICD10_Codes_Dates_Table, index=['NaN Count'])
empty_counts_ICD10_Codes_Dates_Table_databank = pd.DataFrame(empty_counts_ICD10_Codes_Dates_Table, index=['Empty Count'])

# Concatenate the DataFrames
result_ICD10_Codes_Dates_Table = []
result_ICD10_Codes_Dates_Table = pd.concat([unique_counts_ICD10_Codes_Dates_Table_databank, row_counts_ICD10_Codes_Dates_Table_databank, nan_counts_ICD10_Codes_Dates_Table_databank, empty_counts_ICD10_Codes_Dates_Table_databank])

# Display the combined DataFrame
#print("ICD10 Codes with Dates Table:")
print()
#display(result_ICD10_Codes_Dates_Table)
print()
#ICD10_Codes_Dates_Table.head(3)


# **2c. Structure the "ICD10 Codes" with related Diseases and Diagnosis Dates**

# In[ ]:


#### Create a new DataFrame to store the modified data
Storing_ICD10_Codes_Dates_Table = []

#### Iterate through each row
for idx, row in ICD10_Codes_Dates_Table.iterrows():
    participant_id = row['Participant ID']
    year_of_birth = row['Year of Birth']
    month_of_birth = row['Month of Birth']
    ethnicity = row['Ethnicity']
    sex = row['Sex']
    icd_names = row['ICD10 - Diagnosis'].split('|')
    dates = [row['ICD10 date-0'], row['ICD10 date-1'], row['ICD10 date-2'],
             row['ICD10 date-3'], row['ICD10 date-4'], row['ICD10 date-5'],
             row['ICD10 date-6'], row['ICD10 date-7'], row['ICD10 date-8'],
             row['ICD10 date-9'], row['ICD10 date-10'], row['ICD10 date-11'],
             row['ICD10 date-12'], row['ICD10 date-13'], row['ICD10 date-14'],
             row['ICD10 date-15'], row['ICD10 date-16'], row['ICD10 date-17'],
             row['ICD10 date-18'], row['ICD10 date-19'], row['ICD10 date-20'],
             row['ICD10 date-21'], row['ICD10 date-22'], row['ICD10 date-23'],
             row['ICD10 date-24'], row['ICD10 date-25'], row['ICD10 date-26'],
             row['ICD10 date-27'], row['ICD10 date-28'], row['ICD10 date-29'],
             row['ICD10 date-30'], row['ICD10 date-31'], row['ICD10 date-32'],
             row['ICD10 date-33'], row['ICD10 date-34'], row['ICD10 date-35'],
             row['ICD10 date-36'], row['ICD10 date-37'], row['ICD10 date-38'],
             row['ICD10 date-39'], row['ICD10 date-40'], row['ICD10 date-41'],
             row['ICD10 date-42'], row['ICD10 date-43'], row['ICD10 date-44'],
             row['ICD10 date-45'], row['ICD10 date-46'], row['ICD10 date-47'],
             row['ICD10 date-48'], row['ICD10 date-49'], row['ICD10 date-50'],
             row['ICD10 date-51'], row['ICD10 date-52'], row['ICD10 date-53'],
             row['ICD10 date-54'], row['ICD10 date-55'], row['ICD10 date-56'],
             row['ICD10 date-57'], row['ICD10 date-58'], row['ICD10 date-59'],
             row['ICD10 date-60'], row['ICD10 date-61'], row['ICD10 date-62'],
             row['ICD10 date-63'], row['ICD10 date-64'], row['ICD10 date-65'],
             row['ICD10 date-66'], row['ICD10 date-67'], row['ICD10 date-68'],
             row['ICD10 date-69'], row['ICD10 date-70'], row['ICD10 date-71'],
             row['ICD10 date-72'], row['ICD10 date-73'], row['ICD10 date-74'],
             row['ICD10 date-75'], row['ICD10 date-76'], row['ICD10 date-77'],
             row['ICD10 date-78'], row['ICD10 date-79'], row['ICD10 date-80'],
             row['ICD10 date-81'], row['ICD10 date-82'],row['ICD10 date-83'],
             row['ICD10 date-84'], row['ICD10 date-85'],row['ICD10 date-86'],
             row['ICD10 date-87'], row['ICD10 date-88'],row['ICD10 date-89'], row['ICD10 date-90'],
             row['ICD10 date-91'], row['ICD10 date-92'],row['ICD10 date-93'],
             row['ICD10 date-94'], row['ICD10 date-95'],row['ICD10 date-96'],
             row['ICD10 date-97'], row['ICD10 date-98'],row['ICD10 date-99'], row['ICD10 date-100'],
             row['ICD10 date-101'], row['ICD10 date-102'],
             row['ICD10 date-103'], row['ICD10 date-104'], row['ICD10 date-105'],
             row['ICD10 date-106'], row['ICD10 date-107'], row['ICD10 date-108'],
             row['ICD10 date-109'], row['ICD10 date-110'], row['ICD10 date-111'],
             row['ICD10 date-112'], row['ICD10 date-113'], row['ICD10 date-114'],
             row['ICD10 date-115'], row['ICD10 date-116'], row['ICD10 date-117'],
             row['ICD10 date-118'], row['ICD10 date-119'], row['ICD10 date-120'],
             row['ICD10 date-121'], row['ICD10 date-122'], row['ICD10 date-123'],
             row['ICD10 date-124'], row['ICD10 date-125'], row['ICD10 date-126'],
             row['ICD10 date-127'], row['ICD10 date-128'], row['ICD10 date-129'],
             row['ICD10 date-130'], row['ICD10 date-131'], row['ICD10 date-132'],
             row['ICD10 date-133'], row['ICD10 date-134'], row['ICD10 date-135'],
             row['ICD10 date-136'], row['ICD10 date-137'], row['ICD10 date-138'],
             row['ICD10 date-139'], row['ICD10 date-140'], row['ICD10 date-141'],
             row['ICD10 date-142'], row['ICD10 date-143'], row['ICD10 date-144'],
             row['ICD10 date-145'], row['ICD10 date-146'], row['ICD10 date-147'],
             row['ICD10 date-148'], row['ICD10 date-149'], row['ICD10 date-150'],
             row['ICD10 date-151'], row['ICD10 date-152'], row['ICD10 date-153'],
             row['ICD10 date-154'], row['ICD10 date-155'], row['ICD10 date-156'],
             row['ICD10 date-157'], row['ICD10 date-158'], row['ICD10 date-159'],
             row['ICD10 date-160'], row['ICD10 date-161'], row['ICD10 date-162'],
             row['ICD10 date-163'], row['ICD10 date-164'], row['ICD10 date-165'],
             row['ICD10 date-166'], row['ICD10 date-167'], row['ICD10 date-168'],
             row['ICD10 date-169'], row['ICD10 date-170'], row['ICD10 date-171'],
             row['ICD10 date-172'], row['ICD10 date-173'], row['ICD10 date-174'],
             row['ICD10 date-175'], row['ICD10 date-176'], row['ICD10 date-177'],
             row['ICD10 date-178'], row['ICD10 date-179'], row['ICD10 date-180'],
             row['ICD10 date-181'], row['ICD10 date-182'],row['ICD10 date-183'],
             row['ICD10 date-184'], row['ICD10 date-185'],row['ICD10 date-186'],
             row['ICD10 date-187'], row['ICD10 date-188'],row['ICD10 date-189'], row['ICD10 date-190'],
             row['ICD10 date-191'], row['ICD10 date-192'],row['ICD10 date-193'],
             row['ICD10 date-194'], row['ICD10 date-195'],row['ICD10 date-196'],
             row['ICD10 date-197'], row['ICD10 date-198'],row['ICD10 date-199'], row['ICD10 date-200'],
             row['ICD10 date-201'], row['ICD10 date-202'],
             row['ICD10 date-203'], row['ICD10 date-204'], row['ICD10 date-205'],
             row['ICD10 date-206'], row['ICD10 date-207'], row['ICD10 date-208'],
             row['ICD10 date-209'], row['ICD10 date-210'], row['ICD10 date-211'],
             row['ICD10 date-212'], row['ICD10 date-213'], row['ICD10 date-214'],
             row['ICD10 date-215'], row['ICD10 date-216'], row['ICD10 date-217'],
             row['ICD10 date-218'], row['ICD10 date-219'], row['ICD10 date-220'],
             row['ICD10 date-221'], row['ICD10 date-222'], row['ICD10 date-223'],
             row['ICD10 date-224'], row['ICD10 date-225'], row['ICD10 date-226'],
             row['ICD10 date-227'], row['ICD10 date-228'], row['ICD10 date-229'],
             row['ICD10 date-230'], row['ICD10 date-231'], row['ICD10 date-232'],
             row['ICD10 date-233'], row['ICD10 date-234'], row['ICD10 date-235'],
             row['ICD10 date-236'], row['ICD10 date-237'], row['ICD10 date-238'],
             row['ICD10 date-239'], row['ICD10 date-240'], row['ICD10 date-241'],
             row['ICD10 date-242']]


    for i in range(243):
        new_row = [participant_id,year_of_birth,month_of_birth,ethnicity,sex, icd_names[i] if len(icd_names) > i else None, dates[i]]
        Storing_ICD10_Codes_Dates_Table.append(new_row)

#### Create a new DataFrame with the modified data
ICD10_Codes_Dates_dataset = []
ICD10_Codes_Dates_dataset = pd.DataFrame(Storing_ICD10_Codes_Dates_Table, columns=['Participant ID','Year of Birth','Month of Birth','Ethnicity','Sex','ICD10 codes with Diseases Names', 'ICD10 Diagnosis Date'])
#### Remove rows with NaN values in both columns
ICD10_Codes_Dates_dataset = ICD10_Codes_Dates_dataset.dropna(subset=['ICD10 codes with Diseases Names', 'ICD10 Diagnosis Date'])
ICD10_Codes_Dates_dataset


#### Reset the index after dropping rows
ICD10_Codes_Dates_dataset.reset_index(drop=True, inplace=True)
Organised_ICD10_Codes_Dates_Table = []
Organised_ICD10_Codes_Dates_Table = ICD10_Codes_Dates_dataset




# Create dictionaries to store unique counts, row counts, NaN counts, and empty counts
unique_counts_Organised_ICD10_Codes_Dates_Table = {}
row_counts_Organised_ICD10_Codes_Dates_Table = {}
nan_counts_Organised_ICD10_Codes_Dates_Table = {}
empty_counts_Organised_ICD10_Codes_Dates_Table = {}

# Loop through columns and count unique items, row counts, NaN counts, and empty counts
for column_Organised_ICD10_Codes_Dates_Table in Organised_ICD10_Codes_Dates_Table.columns:
    unique_count_Organised_ICD10_Codes_Dates_Table = Organised_ICD10_Codes_Dates_Table[column_Organised_ICD10_Codes_Dates_Table].nunique()
    row_count_Organised_ICD10_Codes_Dates_Table = len(Organised_ICD10_Codes_Dates_Table[column_Organised_ICD10_Codes_Dates_Table])
    nan_count_Organised_ICD10_Codes_Dates_Table = Organised_ICD10_Codes_Dates_Table[column_Organised_ICD10_Codes_Dates_Table].isna().sum()  # Count NaN values
    empty_count_Organised_ICD10_Codes_Dates_Table = Organised_ICD10_Codes_Dates_Table[column_Organised_ICD10_Codes_Dates_Table].eq('').sum()  # Count empty string values

    unique_counts_Organised_ICD10_Codes_Dates_Table[column_Organised_ICD10_Codes_Dates_Table] = [unique_count_Organised_ICD10_Codes_Dates_Table]
    row_counts_Organised_ICD10_Codes_Dates_Table[column_Organised_ICD10_Codes_Dates_Table] = [row_count_Organised_ICD10_Codes_Dates_Table]
    nan_counts_Organised_ICD10_Codes_Dates_Table[column_Organised_ICD10_Codes_Dates_Table] = [nan_count_Organised_ICD10_Codes_Dates_Table]
    empty_counts_Organised_ICD10_Codes_Dates_Table[column_Organised_ICD10_Codes_Dates_Table] = [empty_count_Organised_ICD10_Codes_Dates_Table]

# Create DataFrames from the dictionaries
unique_counts_Organised_ICD10_Codes_Dates_Table_databank = []
row_counts_Organised_ICD10_Codes_Dates_Table_databank = []
nan_counts_Organised_ICD10_ICD10_Codes_Dates_Table_databank = []
empty_counts_Organised_ICD10_ICD10_Codes_Dates_Table_databank = []

unique_counts_Organised_ICD10_Codes_Dates_Table_databank = pd.DataFrame(unique_counts_Organised_ICD10_Codes_Dates_Table, index=['Unique Count'])
row_counts_Organised_ICD10_Codes_Dates_Table_databank = pd.DataFrame(row_counts_Organised_ICD10_Codes_Dates_Table, index=['Row Count'])
nan_counts_Organised_ICD10_Codes_Dates_Table_databank = pd.DataFrame(nan_counts_Organised_ICD10_Codes_Dates_Table, index=['NaN Count'])
empty_counts_Organised_ICD10_Codes_Dates_Table_databank = pd.DataFrame(empty_counts_Organised_ICD10_Codes_Dates_Table, index=['Empty Count'])

# Concatenate the DataFrames
result_Organised_ICD10_Codes_Dates_Table = []
result_Organised_ICD10_Codes_Dates_Table = pd.concat([unique_counts_Organised_ICD10_Codes_Dates_Table_databank, row_counts_Organised_ICD10_Codes_Dates_Table_databank, nan_counts_Organised_ICD10_Codes_Dates_Table_databank, empty_counts_Organised_ICD10_Codes_Dates_Table_databank])

# Display the combined DataFrame
print("Organised ICD10 Codes with Dates Table:")
print()
display(result_Organised_ICD10_Codes_Dates_Table)
print()







### Seperate the ICD10 Codes and ICD10 Diseases columns
Organised_ICD10_Codes_Dates_dataset = []
Organised_ICD10_Codes_Dates_dataset = Organised_ICD10_Codes_Dates_Table
Organised_ICD10_Codes_Dates_dataset['ICD10 codes'] = Organised_ICD10_Codes_Dates_dataset['ICD10 codes with Diseases Names'].str.extract(r'([A-Z]\d+\.\d+|[A-Z]\d+)')  # Handles both cases
Organised_ICD10_Codes_Dates_dataset['ICD10 Diseases'] = Organised_ICD10_Codes_Dates_dataset['ICD10 codes with Diseases Names'].str.replace(r'[A-Z]\d+\.\d+|[A-Z]\d+', '')
Organised_ICD10_Codes_Dates_dataset = Organised_ICD10_Codes_Dates_dataset.drop(columns=['ICD10 codes with Diseases Names'])
Organised_ICD10_Codes_Dates_dataset = Organised_ICD10_Codes_Dates_dataset.sort_values(by=['Participant ID'])


#ICD10_Codes_Dates_dataset.head(3)


# **2d. Extract the "Main ICD10 Codes" Variables from the main dataset**

# In[ ]:


#### initialize df1 as ICD10 codes dataset
Main_ICD10_Codes_Dates_Table = []
Main_ICD10_Codes_Dates_Table = ICD10_dataset.iloc[:, :5].join(ICD10_dataset.iloc[:, 249:329])
Main_ICD10_Codes_Dates_Table  = Main_ICD10_Codes_Dates_Table .dropna(subset=['Main ICD10 - Diagnosis'])





# Create dictionaries to store unique counts, row counts, NaN counts, and empty counts
unique_counts_Main_ICD10_Codes_Dates_Table = {}
row_counts_Main_ICD10_Codes_Dates_Table = {}
nan_counts_Main_ICD10_Codes_Dates_Table = {}
empty_counts_Main_ICD10_Codes_Dates_Table = {}

# Loop through columns and count unique items, row counts, NaN counts, and empty counts
for column_Main_ICD10_Codes_Dates_Table in Main_ICD10_Codes_Dates_Table.columns:
    unique_count_Main_ICD10_Codes_Dates_Table = Main_ICD10_Codes_Dates_Table[column_Main_ICD10_Codes_Dates_Table].nunique()
    row_count_Main_ICD10_Codes_Dates_Table = len(Main_ICD10_Codes_Dates_Table[column_Main_ICD10_Codes_Dates_Table])
    nan_count_Main_ICD10_Codes_Dates_Table = Main_ICD10_Codes_Dates_Table[column_Main_ICD10_Codes_Dates_Table].isna().sum()  # Count NaN values
    empty_count_Main_ICD10_Codes_Dates_Table = Main_ICD10_Codes_Dates_Table[column_Main_ICD10_Codes_Dates_Table].eq('').sum()  # Count empty string values

    unique_counts_Main_ICD10_Codes_Dates_Table[column_Main_ICD10_Codes_Dates_Table] = [unique_count_Main_ICD10_Codes_Dates_Table]
    row_counts_Main_ICD10_Codes_Dates_Table[column_Main_ICD10_Codes_Dates_Table] = [row_count_Main_ICD10_Codes_Dates_Table]
    nan_counts_Main_ICD10_Codes_Dates_Table[column_Main_ICD10_Codes_Dates_Table] = [nan_count_Main_ICD10_Codes_Dates_Table]
    empty_counts_Main_ICD10_Codes_Dates_Table[column_Main_ICD10_Codes_Dates_Table] = [empty_count_Main_ICD10_Codes_Dates_Table]

# Create DataFrames from the dictionaries
unique_counts_Main_ICD10_Codes_Dates_Table_databank = []
row_counts_Main_ICD10_Codes_Dates_Table_databank = []
nan_counts_Main_ICD10_ICD10_Codes_Dates_Table_databank = []
empty_counts_Main_ICD10_ICD10_Codes_Dates_Table_databank = []

unique_counts_Main_ICD10_Codes_Dates_Table_databank = pd.DataFrame(unique_counts_Main_ICD10_Codes_Dates_Table, index=['Unique Count'])
row_counts_Main_ICD10_Codes_Dates_Table_databank = pd.DataFrame(row_counts_Main_ICD10_Codes_Dates_Table, index=['Row Count'])
nan_counts_Main_ICD10_Codes_Dates_Table_databank = pd.DataFrame(nan_counts_Main_ICD10_Codes_Dates_Table, index=['NaN Count'])
empty_counts_Main_ICD10_Codes_Dates_Table_databank = pd.DataFrame(empty_counts_Main_ICD10_Codes_Dates_Table, index=['Empty Count'])

# Concatenate the DataFrames
result_Main_ICD10_Codes_Dates_Table = []
result_Main_ICD10_Codes_Dates_Table = pd.concat([unique_counts_Main_ICD10_Codes_Dates_Table_databank, row_counts_Main_ICD10_Codes_Dates_Table_databank, nan_counts_Main_ICD10_Codes_Dates_Table_databank, empty_counts_Main_ICD10_Codes_Dates_Table_databank])

# Display the combined DataFrame
print("Main ICD10 Codes with Dates Table:")
print()
#display(result_Main_ICD10_Codes_Dates_Table)
print()
#Main_ICD10_Codes_Dates_Table.head(3)


# **2e. Structure the "Main ICD10 Codes" with related Diseases and Diagnosis Dates**

# In[ ]:


#### Create a new DataFrame to store the modified data
Storing_Main_ICD10_Codes_Dates_Table = []

#### Iterate through each row
for idx_Main, row in Main_ICD10_Codes_Dates_Table.iterrows():
    participant_id_Main = row['Participant ID']
    year_of_birth_Main = row['Year of Birth']
    month_of_birth_Main = row['Month of Birth']
    ethnicity_Main = row['Ethnicity']
    sex_Main = row['Sex']
    icd_names_Main = row['Main ICD10 - Diagnosis'].split('|')
    dates_Main = [row['Main ICD10 date-0'], row['Main ICD10 date-1'], row['Main ICD10 date-2'],
             row['Main ICD10 date-3'], row['Main ICD10 date-4'], row['Main ICD10 date-5'],
             row['Main ICD10 date-6'], row['Main ICD10 date-7'], row['Main ICD10 date-8'],
             row['Main ICD10 date-9'], row['Main ICD10 date-10'], row['Main ICD10 date-11'],
             row['Main ICD10 date-12'], row['Main ICD10 date-13'], row['Main ICD10 date-14'],
             row['Main ICD10 date-15'], row['Main ICD10 date-16'], row['Main ICD10 date-17'],
             row['Main ICD10 date-18'], row['Main ICD10 date-19'], row['Main ICD10 date-20'],
             row['Main ICD10 date-21'], row['Main ICD10 date-22'], row['Main ICD10 date-23'],
             row['Main ICD10 date-24'], row['Main ICD10 date-25'], row['Main ICD10 date-26'],
             row['Main ICD10 date-27'], row['Main ICD10 date-28'], row['Main ICD10 date-29'],
             row['Main ICD10 date-30'], row['Main ICD10 date-31'], row['Main ICD10 date-32'],
             row['Main ICD10 date-33'], row['Main ICD10 date-34'], row['Main ICD10 date-35'],
             row['Main ICD10 date-36'], row['Main ICD10 date-37'], row['Main ICD10 date-38'],
             row['Main ICD10 date-39'], row['Main ICD10 date-40'], row['Main ICD10 date-41'],
             row['Main ICD10 date-42'], row['Main ICD10 date-43'], row['Main ICD10 date-44'],
             row['Main ICD10 date-45'], row['Main ICD10 date-46'], row['Main ICD10 date-47'],
             row['Main ICD10 date-48'], row['Main ICD10 date-49'], row['Main ICD10 date-50'],
             row['Main ICD10 date-51'], row['Main ICD10 date-52'], row['Main ICD10 date-53'],
             row['Main ICD10 date-54'], row['Main ICD10 date-55'], row['Main ICD10 date-56'],
             row['Main ICD10 date-57'], row['Main ICD10 date-58'], row['Main ICD10 date-59'],
             row['Main ICD10 date-60'], row['Main ICD10 date-61'], row['Main ICD10 date-62'],
             row['Main ICD10 date-63'], row['Main ICD10 date-64'], row['Main ICD10 date-65'],
             row['Main ICD10 date-66'], row['Main ICD10 date-67'], row['Main ICD10 date-68'],
             row['Main ICD10 date-69'], row['Main ICD10 date-70'], row['Main ICD10 date-71'],
             row['Main ICD10 date-72'], row['Main ICD10 date-73'], row['Main ICD10 date-74'],
             row['Main ICD10 date-75'], row['Main ICD10 date-76'], row['Main ICD10 date-77'],
             row['Main ICD10 date-78']]


    for i in range(79):
        new_row_Main = [participant_id_Main,year_of_birth_Main,month_of_birth_Main,ethnicity_Main,sex_Main, icd_names_Main[i] if len(icd_names_Main) > i else None, dates_Main[i]]
        Storing_Main_ICD10_Codes_Dates_Table.append(new_row_Main)

#### Create a new DataFrame with the modified data
Main_ICD10_Codes_Dates_dataset = []
Main_ICD10_Codes_Dates_dataset = pd.DataFrame(Storing_Main_ICD10_Codes_Dates_Table, columns=['Participant ID','Year of Birth','Month of Birth','Ethnicity','Sex','Main ICD10 codes with Diseases Names', 'Main ICD10 Diagnosis Date'])
### Remove rows with NaN values in both columns
Main_ICD10_Codes_Dates_dataset = Main_ICD10_Codes_Dates_dataset.dropna(subset=['Main ICD10 codes with Diseases Names', 'Main ICD10 Diagnosis Date'])
Main_ICD10_Codes_Dates_dataset


#### Reset the index after dropping rows
Main_ICD10_Codes_Dates_dataset.reset_index(drop=True, inplace=True)
Main_ICD10_Codes_Dates_dataset





Organised_Main_ICD10_Codes_Dates_Table = []
Organised_Main_ICD10_Codes_Dates_Table = Main_ICD10_Codes_Dates_dataset




# Create dictionaries to store unique counts, row counts, NaN counts, and empty counts
unique_counts_Organised_Main_ICD10_Codes_Dates_Table = {}
row_counts_Organised_Main_ICD10_Codes_Dates_Table = {}
nan_counts_Organised_Main_ICD10_Codes_Dates_Table = {}
empty_counts_Organised_Main_ICD10_Codes_Dates_Table = {}

# Loop through columns and count unique items, row counts, NaN counts, and empty counts
for column_Organised_Main_ICD10_Codes_Dates_Table in Organised_Main_ICD10_Codes_Dates_Table.columns:
    unique_count_Organised_Main_ICD10_Codes_Dates_Table = Organised_Main_ICD10_Codes_Dates_Table[column_Organised_Main_ICD10_Codes_Dates_Table].nunique()
    row_count_Organised_Main_ICD10_Codes_Dates_Table = len(Organised_Main_ICD10_Codes_Dates_Table[column_Organised_Main_ICD10_Codes_Dates_Table])
    nan_count_Organised_Main_ICD10_Codes_Dates_Table = Organised_Main_ICD10_Codes_Dates_Table[column_Organised_Main_ICD10_Codes_Dates_Table].isna().sum()  # Count NaN values
    empty_count_Organised_Main_ICD10_Codes_Dates_Table = Organised_Main_ICD10_Codes_Dates_Table[column_Organised_Main_ICD10_Codes_Dates_Table].eq('').sum()  # Count empty string values

    unique_counts_Organised_Main_ICD10_Codes_Dates_Table[column_Organised_Main_ICD10_Codes_Dates_Table] = [unique_count_Organised_Main_ICD10_Codes_Dates_Table]
    row_counts_Organised_Main_ICD10_Codes_Dates_Table[column_Organised_Main_ICD10_Codes_Dates_Table] = [row_count_Organised_Main_ICD10_Codes_Dates_Table]
    nan_counts_Organised_Main_ICD10_Codes_Dates_Table[column_Organised_Main_ICD10_Codes_Dates_Table] = [nan_count_Organised_Main_ICD10_Codes_Dates_Table]
    empty_counts_Organised_Main_ICD10_Codes_Dates_Table[column_Organised_Main_ICD10_Codes_Dates_Table] = [empty_count_Organised_Main_ICD10_Codes_Dates_Table]

# Create DataFrames from the dictionaries
unique_counts_Organised_Main_ICD10_Codes_Dates_Table_databank = []
row_counts_Organised_Main_ICD10_Codes_Dates_Table_databank = []
nan_counts_Organised_Main_ICD10_ICD10_Codes_Dates_Table_databank = []
empty_counts_Organised_Main_ICD10_ICD10_Codes_Dates_Table_databank = []

unique_counts_Organised_Main_ICD10_Codes_Dates_Table_databank = pd.DataFrame(unique_counts_Organised_Main_ICD10_Codes_Dates_Table, index=['Unique Count'])
row_counts_Organised_Main_ICD10_Codes_Dates_Table_databank = pd.DataFrame(row_counts_Organised_Main_ICD10_Codes_Dates_Table, index=['Row Count'])
nan_counts_Organised_Main_ICD10_Codes_Dates_Table_databank = pd.DataFrame(nan_counts_Organised_Main_ICD10_Codes_Dates_Table, index=['NaN Count'])
empty_counts_Organised_Main_ICD10_Codes_Dates_Table_databank = pd.DataFrame(empty_counts_Organised_Main_ICD10_Codes_Dates_Table, index=['Empty Count'])

# Concatenate the DataFrames
result_Organised_Main_ICD10_Codes_Dates_Table = []
result_Organised_Main_ICD10_Codes_Dates_Table = pd.concat([unique_counts_Organised_Main_ICD10_Codes_Dates_Table_databank, row_counts_Organised_Main_ICD10_Codes_Dates_Table_databank, nan_counts_Organised_Main_ICD10_Codes_Dates_Table_databank, empty_counts_Organised_Main_ICD10_Codes_Dates_Table_databank])

# Display the combined DataFrame
print("Organised Main ICD10 Codes with Dates Table:")
print()
display(result_Organised_Main_ICD10_Codes_Dates_Table)
print()






#### Seperate the Main ICD10 Codes and Main ICD10 Diseases columns
Organised_Main_ICD10_Codes_Dates_dataset = []
Organised_Main_ICD10_Codes_Dates_dataset = Organised_Main_ICD10_Codes_Dates_Table

Organised_Main_ICD10_Codes_Dates_dataset['Main ICD10 codes'] = Organised_Main_ICD10_Codes_Dates_dataset['Main ICD10 codes with Diseases Names'].str.extract(r'([A-Z]\d+\.\d+|[A-Z]\d+)')  # Handles both cases
Organised_Main_ICD10_Codes_Dates_dataset['Main ICD10 Diseases'] = Organised_Main_ICD10_Codes_Dates_dataset['Main ICD10 codes with Diseases Names'].str.replace(r'[A-Z]\d+\.\d+|[A-Z]\d+', '')
Organised_Main_ICD10_Codes_Dates_dataset = Organised_Main_ICD10_Codes_Dates_dataset.drop(columns=['Main ICD10 codes with Diseases Names'])
Organised_Main_ICD10_Codes_Dates_dataset = Organised_Main_ICD10_Codes_Dates_dataset.sort_values(by=['Participant ID'])


#Main_ICD10_Codes_Dates_dataset.head(3)


# **2f. Concentenate "ICD10_Code_dataset" and "Main_ICD10_Code_dataset" datasets**

# In[ ]:


### Concentenate (combine) ICD10 codes dataset  and Main ICD10 codes dataset
data_table = []
data_table = pd.concat([Organised_ICD10_Codes_Dates_dataset ,Organised_Main_ICD10_Codes_Dates_dataset])
data_table = data_table.sort_values(by='Participant ID')
data_table.fillna('', inplace=True)




# Create dictionaries to store unique counts, row counts, NaN counts, and empty counts
unique_counts_data_table = {}
row_counts_data_table= {}
nan_counts_data_table = {}
empty_counts_data_table = {}

# Loop through columns and count unique items, row counts, NaN counts, and empty counts
for column_data_table in data_table.columns:
    unique_count_data_table = data_table[column_data_table].nunique()
    row_count_data_table = len(data_table[column_data_table])
    nan_count_data_table = data_table[column_data_table].isna().sum()  # Count NaN values
    empty_count_data_table = data_table[column_data_table].eq('').sum()  # Count empty string values

    unique_counts_data_table[column_data_table] = [unique_count_data_table]
    row_counts_data_table[column_data_table] = [row_count_data_table]
    nan_counts_data_table[column_data_table] = [nan_count_data_table]
    empty_counts_data_table[column_data_table] = [empty_count_data_table]

# Create DataFrames from the dictionaries
unique_counts_data_table_records = []
row_counts_data_table_records = []
nan_counts_data_table_records = []
empty_counts_data_table_records = []

unique_counts_data_table_records = pd.DataFrame(unique_counts_data_table, index=['Unique Count'])
row_counts_data_table_records = pd.DataFrame(row_counts_data_table, index=['Row Count'])
nan_counts_data_table_records = pd.DataFrame(nan_counts_data_table, index=['NaN Count'])
empty_counts_data_table_records = pd.DataFrame(empty_counts_data_table, index=['Empty Count'])

# Concatenate the DataFrames
result_data_table = []
result_data_table = pd.concat([unique_counts_data_table_records, row_counts_data_table_records, nan_counts_data_table_records, empty_counts_data_table_records])

# Display the combined DataFrame
print("Data Table Record:")
print()
#display(result_data_table)
print()
#data_table.head(3)


# **2g. Create Two new Variables: "Combined ICD10 Codes" and "Combined ICD10 Diagnosis Date"**

# In[ ]:


### Create a new column 'Combined ICD10 Codes' by concatenating 'ICD10 codes' and 'Main ICD10 codes'
data_table['Combined ICD10 Codes'] = data_table['ICD10 codes'] + data_table['Main ICD10 codes']


#### Create a new column 'Combined ICD10 Diagnosis Date' by selecting the non-empty value between 'ICD10 Diagnosis Date' and 'Main ICD10 Diagnosis Date'
data_table['Combined ICD10 Diagnosis Date'] = np.where(data_table['ICD10 Diagnosis Date'] != '', data_table['ICD10 Diagnosis Date'], data_table['Main ICD10 Diagnosis Date'])


#### Create a new column 'Combined ICD10 Diseases' by concatenating 'ICD10 Diseases' and 'Main ICD10 Diseases'
data_table['Combined ICD10 Diseases'] = data_table['ICD10 Diseases']  + data_table['Main ICD10 Diseases']


### Drop the original columns that are no longer needed
data_table.drop(['ICD10 codes', 'ICD10 Diagnosis Date', 'Main ICD10 codes', 'Main ICD10 Diagnosis Date', 'ICD10 Diseases', 'Main ICD10 Diseases'], axis=1, inplace=True)

data_table = data_table.sort_values(by=['Participant ID','Combined ICD10 Codes','Combined ICD10 Diagnosis Date'])



Combined_ICD10_data_table = []
Combined_ICD10_data_table = data_table

# Create dictionaries to store unique counts, row counts, NaN counts, and empty counts
unique_counts_Combined_ICD10_data_table = {}
row_counts_Combined_ICD10_data_table= {}
nan_counts_Combined_ICD10_data_table = {}
empty_counts_Combined_ICD10_data_table = {}

# Loop through columns and count unique items, row counts, NaN counts, and empty counts
for column_Combined_ICD10_data_table in Combined_ICD10_data_table.columns:
    unique_count_Combined_ICD10_data_table = Combined_ICD10_data_table[column_Combined_ICD10_data_table].nunique()
    row_count_Combined_ICD10_data_table = len(Combined_ICD10_data_table[column_Combined_ICD10_data_table])
    nan_count_Combined_ICD10_data_table = Combined_ICD10_data_table[column_Combined_ICD10_data_table].isna().sum()  # Count NaN values
    empty_count_Combined_ICD10_data_table = Combined_ICD10_data_table[column_Combined_ICD10_data_table].eq('').sum()  # Count empty string values

    unique_counts_Combined_ICD10_data_table[column_Combined_ICD10_data_table] = [unique_count_Combined_ICD10_data_table]
    row_counts_Combined_ICD10_data_table[column_Combined_ICD10_data_table] = [row_count_Combined_ICD10_data_table]
    nan_counts_Combined_ICD10_data_table[column_Combined_ICD10_data_table] = [nan_count_Combined_ICD10_data_table]
    empty_counts_Combined_ICD10_data_table[column_Combined_ICD10_data_table] = [empty_count_Combined_ICD10_data_table]

# Create DataFrames from the dictionaries
unique_counts_Combined_ICD10_data_table_records = []
row_counts_Combined_ICD10_data_table_records = []
nan_counts_Combined_ICD10_data_table_records = []
empty_counts_Combined_ICD10_data_table_records = []

unique_counts_Combined_ICD10_data_table_records = pd.DataFrame(unique_counts_Combined_ICD10_data_table, index=['Unique Count'])
row_counts_Combined_ICD10_data_table_records = pd.DataFrame(row_counts_Combined_ICD10_data_table, index=['Row Count'])
nan_counts_Combined_ICD10_data_table_records = pd.DataFrame(nan_counts_Combined_ICD10_data_table, index=['NaN Count'])
empty_counts_Combined_ICD10_data_table_records = pd.DataFrame(empty_counts_Combined_ICD10_data_table, index=['Empty Count'])

# Concatenate the DataFrames
result_Combined_ICD10_data_table = []
result_Combined_ICD10_data_table = pd.concat([unique_counts_Combined_ICD10_data_table_records, row_counts_Combined_ICD10_data_table_records, nan_counts_Combined_ICD10_data_table_records, empty_counts_Combined_ICD10_data_table_records])

# Display the combined DataFrame
#print("Combined ICD10 Data Table Record:")
#print()
#display(result_Combined_ICD10_data_table)
#print()
#data_table.head(3)


# **2h. Drop Duplicates and Rearrange Variables and Save the output as Dataset**

# In[ ]:


data_table = data_table.drop_duplicates(['Participant ID','Combined ICD10 Codes','Combined ICD10 Diagnosis Date','Combined ICD10 Diseases'])
data_table


#### Rearrange the columns
data_table = data_table[['Participant ID', 'Sex', 'Year of Birth', 'Month of Birth', 'Ethnicity', 'Combined ICD10 Diseases','Combined ICD10 Diagnosis Date','Combined ICD10 Codes']]
data_table


dropped_duplicates_data_table = []
dropped_duplicates_data_table = data_table


# Create dictionaries to store unique counts, row counts, NaN counts, and empty counts
unique_counts_dropped_duplicates_data_table = {}
row_counts_dropped_duplicates_data_table= {}
nan_counts_dropped_duplicates_data_table = {}
empty_counts_dropped_duplicates_data_table = {}

# Loop through columns and count unique items, row counts, NaN counts, and empty counts
for column_dropped_duplicates_data_table in dropped_duplicates_data_table.columns:
    unique_count_dropped_duplicates_data_table = dropped_duplicates_data_table[column_dropped_duplicates_data_table].nunique()
    row_count_dropped_duplicates_data_table = len(dropped_duplicates_data_table[column_dropped_duplicates_data_table])
    nan_count_dropped_duplicates_data_table = dropped_duplicates_data_table[column_dropped_duplicates_data_table].isna().sum()  # Count NaN values
    empty_count_dropped_duplicates_data_table = dropped_duplicates_data_table[column_dropped_duplicates_data_table].eq('').sum()  # Count empty string values

    unique_counts_dropped_duplicates_data_table[column_dropped_duplicates_data_table] = [unique_count_dropped_duplicates_data_table]
    row_counts_dropped_duplicates_data_table[column_dropped_duplicates_data_table] = [row_count_dropped_duplicates_data_table]
    nan_counts_dropped_duplicates_data_table[column_dropped_duplicates_data_table] = [nan_count_dropped_duplicates_data_table]
    empty_counts_dropped_duplicates_data_table[column_dropped_duplicates_data_table] = [empty_count_dropped_duplicates_data_table]

# Create DataFrames from the dictionaries
unique_counts_dropped_duplicates_data_table_records = []
row_counts_dropped_duplicates_data_table_records = []
nan_counts_dropped_duplicates_data_table_records = []
empty_counts_dropped_duplicates_data_table_records = []

unique_counts_dropped_duplicates_data_table_records = pd.DataFrame(unique_counts_dropped_duplicates_data_table, index=['Unique Count'])
row_counts_dropped_duplicates_data_table_records = pd.DataFrame(row_counts_dropped_duplicates_data_table, index=['Row Count'])
nan_counts_dropped_duplicates_data_table_records = pd.DataFrame(nan_counts_dropped_duplicates_data_table, index=['NaN Count'])
empty_counts_dropped_duplicates_data_table_records = pd.DataFrame(empty_counts_dropped_duplicates_data_table, index=['Empty Count'])

# Concatenate the DataFrames
result_dropped_duplicates_data_table = []
result_dropped_duplicates_data_table = pd.concat([unique_counts_dropped_duplicates_data_table_records, row_counts_dropped_duplicates_data_table_records, nan_counts_dropped_duplicates_data_table_records, empty_counts_dropped_duplicates_data_table_records])

# Display the combined DataFrame
print("Dropped Duplicates from Data Table Record:")
print()
display(result_dropped_duplicates_data_table)
print()
data_table.head(3)



#### Specify the file path where you want to save the CSV file
#file_path = 'All ICD10 Codes with Diseases Names and Dates Data.csv'

#### Use the to_csv method to save the DataFrame as a CSV file
#data_table.to_csv(file_path, index=False)  # Set index=False to exclude the index column


# In[ ]:


All_ICD10_with_Diseases_Dates_Data = []
All_ICD10_with_Diseases_Dates_Data = pd.read_csv('All ICD10 Codes with Diseases Names and Dates Data.csv')

# Display the combined DataFrame
#print("Dropped Duplicates from Data Table Record:")
print()
#display(result_dropped_duplicates_data_table)

# Create dictionaries to store unique counts, row counts, NaN counts, and empty counts
unique_counts_All_ICD10_with_Diseases_Dates_Data = {}
row_counts_All_ICD10_with_Diseases_Dates_Data = {}
nan_counts_All_ICD10_with_Diseases_Dates_Data = {}
empty_counts_All_ICD10_with_Diseases_Dates_Data = {}

# Loop through columns and count unique items, row counts, NaN counts, and empty counts
for column_All_ICD10_with_Diseases_Dates_Data in All_ICD10_with_Diseases_Dates_Data.columns:
    unique_count_All_ICD10_with_Diseases_Dates_Data = All_ICD10_with_Diseases_Dates_Data[column_All_ICD10_with_Diseases_Dates_Data].nunique()
    row_count_All_ICD10_with_Diseases_Dates_Data = len(All_ICD10_with_Diseases_Dates_Data[column_All_ICD10_with_Diseases_Dates_Data])
    nan_count_All_ICD10_with_Diseases_Dates_Data = All_ICD10_with_Diseases_Dates_Data[column_All_ICD10_with_Diseases_Dates_Data].isna().sum()  # Count NaN values
    empty_count_All_ICD10_with_Diseases_Dates_Data = All_ICD10_with_Diseases_Dates_Data[column_All_ICD10_with_Diseases_Dates_Data].eq('').sum()  # Count empty string values

    unique_counts_All_ICD10_with_Diseases_Dates_Data[column_All_ICD10_with_Diseases_Dates_Data] = [unique_count_All_ICD10_with_Diseases_Dates_Data]
    row_counts_All_ICD10_with_Diseases_Dates_Data[column_All_ICD10_with_Diseases_Dates_Data] = [row_count_All_ICD10_with_Diseases_Dates_Data]
    nan_counts_All_ICD10_with_Diseases_Dates_Data[column_All_ICD10_with_Diseases_Dates_Data] = [nan_count_All_ICD10_with_Diseases_Dates_Data]
    empty_counts_All_ICD10_with_Diseases_Dates_Data[column_All_ICD10_with_Diseases_Dates_Data] = [empty_count_All_ICD10_with_Diseases_Dates_Data]

# Create DataFrames from the dictionaries
unique_counts_All_ICD10_with_Diseases_Dates_Datas = []
row_counts_All_ICD10_with_Diseases_Dates_Datas = []
nan_counts_All_ICD10_with_Diseases_Dates_Datas = []
empty_counts_All_ICD10_with_Diseases_Dates_Datas = []

unique_counts_All_ICD10_with_Diseases_Dates_Datas = pd.DataFrame(unique_counts_All_ICD10_with_Diseases_Dates_Data, index=['Unique Count'])
row_counts_All_ICD10_with_Diseases_Dates_Datas = pd.DataFrame(row_counts_All_ICD10_with_Diseases_Dates_Data, index=['Row Count'])
nan_counts_All_ICD10_with_Diseases_Dates_Datas = pd.DataFrame(nan_counts_All_ICD10_with_Diseases_Dates_Data, index=['NaN Count'])
empty_counts_All_ICD10_with_Diseases_Dates_Datas = pd.DataFrame(empty_counts_All_ICD10_with_Diseases_Dates_Data, index=['Empty Count'])

# Concatenate the DataFrames
result_All_ICD10_with_Diseases_Dates_Data = []
result_All_ICD10_with_Diseases_Dates_Data = pd.concat([unique_counts_All_ICD10_with_Diseases_Dates_Datas, row_counts_All_ICD10_with_Diseases_Dates_Datas, nan_counts_All_ICD10_with_Diseases_Dates_Datas, empty_counts_All_ICD10_with_Diseases_Dates_Datas])

# Display the combined DataFrame
#print("All_ICD10_with_Diseases_Dates_Data Record:")
#print()
#display(result_All_ICD10_with_Diseases_Dates_Data)
#print()

#All_ICD10_with_Diseases_Dates_Data.head(5)


# **2i. Import Death Dates dataset from UK biobank**

# In[ ]:


Death_Date_Record = []
Death_Date_Record = pd.read_csv('Death Date Record.csv')
Death_Date_Record = Death_Date_Record.drop_duplicates()




# Create dictionaries to store unique counts, row counts, NaN counts, and empty counts
unique_counts_Death_Date_Record = {}
row_counts_Death_Date_Record = {}
nan_counts_Death_Date_Record = {}
empty_counts_Death_Date_Record = {}

# Loop through columns and count unique items, row counts, NaN counts, and empty counts
for column_Death_Date_Record in Death_Date_Record.columns:
    unique_count_Death_Date_Record = Death_Date_Record[column_Death_Date_Record].nunique()
    row_count_Death_Date_Record = len(Death_Date_Record[column_Death_Date_Record])
    nan_count_Death_Date_Record = Death_Date_Record[column_Death_Date_Record].isna().sum()  # Count NaN values
    empty_count_Death_Date_Record = Death_Date_Record[column_Death_Date_Record].eq('').sum()  # Count empty string values

    unique_counts_Death_Date_Record[column_Death_Date_Record] = [unique_count_Death_Date_Record]
    row_counts_Death_Date_Record[column_Death_Date_Record] = [row_count_Death_Date_Record]
    nan_counts_Death_Date_Record[column_Death_Date_Record] = [nan_count_Death_Date_Record]
    empty_counts_Death_Date_Record[column_Death_Date_Record] = [empty_count_Death_Date_Record]

# Create DataFrames from the dictionaries
unique_counts_Death_Date = []
row_counts_Death_Date = []
nan_counts_Death_Date = []
empty_counts_Death_Date = []

unique_counts_Death_Date = pd.DataFrame(unique_counts_Death_Date_Record, index=['Unique Count'])
row_counts_Death_Date = pd.DataFrame(row_counts_Death_Date_Record, index=['Row Count'])
nan_counts_Death_Date = pd.DataFrame(nan_counts_Death_Date_Record, index=['NaN Count'])
empty_counts_Death_Date = pd.DataFrame(empty_counts_Death_Date_Record, index=['Empty Count'])

# Concatenate the DataFrames
result_Death_Date_Record = []
result_Death_Date_Record = pd.concat([unique_counts_Death_Date, row_counts_Death_Date, nan_counts_Death_Date, empty_counts_Death_Date])

# Display the combined DataFrame
#print("Death Date Record:")
#print()
#display(result_Death_Date_Record)



#Death_Date_Record.head(3)


# **2j. Import Death Cause dataset from UK biobank**

# In[ ]:


Death_Cause_Record = []
Death_Cause_Record = pd.read_csv('Death Cause Record.csv')
Death_Cause_Record = Death_Cause_Record.drop_duplicates()
Death_Cause_Record = Death_Cause_Record.rename(columns={'ICD10 codes':'Death Cause Disease ICD10 Codes','ICD10 Diseases':'Death Cause Diseases'})



# Create dictionaries to store unique counts, row counts, NaN counts, and empty counts
unique_counts_Death_Cause_Record = {}
row_counts_Death_Cause_Record = {}
nan_counts_Death_Cause_Record = {}
empty_counts_Death_Cause_Record = {}

# Loop through columns and count unique items, row counts, NaN counts, and empty counts
for column_Death_Cause_Record in Death_Cause_Record.columns:
    unique_count_Death_Cause_Record = Death_Cause_Record[column_Death_Cause_Record].nunique()
    row_count_Death_Cause_Record = len(Death_Cause_Record[column_Death_Cause_Record])
    nan_count_Death_Cause_Record = Death_Cause_Record[column_Death_Cause_Record].isna().sum()  # Count NaN values
    empty_count_Death_Cause_Record = Death_Cause_Record[column_Death_Cause_Record].eq('').sum()  # Count empty string values

    unique_counts_Death_Cause_Record[column_Death_Cause_Record] = [unique_count_Death_Cause_Record]
    row_counts_Death_Cause_Record[column_Death_Cause_Record] = [row_count_Death_Cause_Record]
    nan_counts_Death_Cause_Record[column_Death_Cause_Record] = [nan_count_Death_Cause_Record]
    empty_counts_Death_Cause_Record[column_Death_Cause_Record] = [empty_count_Death_Cause_Record]

# Create DataFrames from the dictionaries
unique_counts_Death_Cause = []
row_counts_Death_Cause = []
nan_counts_Death_Cause = []
empty_counts_Death_Cause = []

unique_counts_Death_Cause = pd.DataFrame(unique_counts_Death_Cause_Record, index=['Unique Count'])
row_counts_Death_Cause = pd.DataFrame(row_counts_Death_Cause_Record, index=['Row Count'])
nan_counts_Death_Cause = pd.DataFrame(nan_counts_Death_Cause_Record, index=['NaN Count'])
empty_counts_Death_Cause = pd.DataFrame(empty_counts_Death_Cause_Record, index=['Empty Count'])

# Concatenate the DataFrames
result_Death_Cause_Record = []
result_Death_Cause_Record = pd.concat([unique_counts_Death_Cause, row_counts_Death_Cause, nan_counts_Death_Cause, empty_counts_Death_Cause])

# Display the combined DataFrame
#print("Death Cause Record:")
#print()
#display(result_Death_Cause_Record)




#Death_Cause_Record.head(3)


# **2k. Import GP dataset of drugs (medicine) from UK biobank**

# In[ ]:


GP_Prescription_Record = []
GP_Prescription_Record = pd.read_csv('GP Prescription Record.csv')
GP_Prescription_Record = GP_Prescription_Record.drop_duplicates()
GP_Prescription_Record = GP_Prescription_Record.rename(columns={'Issue Date':'Drug Issue Date','Quantity':'Drug Quantity'})

# Create dictionaries to store unique counts, row counts, NaN counts, and empty counts
unique_counts_GP_Prescription_Record = {}
row_counts_GP_Prescription_Record = {}
nan_counts_GP_Prescription_Record = {}
empty_counts_GP_Prescription_Record = {}

# Loop through columns and count unique items, row counts, NaN counts, and empty counts
for column_GP_Prescription_Record in GP_Prescription_Record.columns:
    unique_count_GP_Prescription_Record = GP_Prescription_Record[column_GP_Prescription_Record].nunique()
    row_count_GP_Prescription_Record = len(GP_Prescription_Record[column_GP_Prescription_Record])
    nan_count_GP_Prescription_Record = GP_Prescription_Record[column_GP_Prescription_Record].isna().sum()  # Count NaN values
    empty_count_GP_Prescription_Record = GP_Prescription_Record[column_GP_Prescription_Record].eq('').sum()  # Count empty string values

    unique_counts_GP_Prescription_Record[column_GP_Prescription_Record] = [unique_count_GP_Prescription_Record]
    row_counts_GP_Prescription_Record[column_GP_Prescription_Record] = [row_count_GP_Prescription_Record]
    nan_counts_GP_Prescription_Record[column_GP_Prescription_Record] = [nan_count_GP_Prescription_Record]
    empty_counts_GP_Prescription_Record[column_GP_Prescription_Record] = [empty_count_GP_Prescription_Record]

# Create DataFrames from the dictionaries
unique_counts_GP_Prescription = []
row_counts_GP_Prescription = []
nan_counts_GP_Prescription = []
empty_counts_GP_Prescription_Record = []

unique_counts_GP_Prescription = pd.DataFrame(unique_counts_GP_Prescription_Record, index=['Unique Count'])
row_counts_GP_Prescription = pd.DataFrame(row_counts_GP_Prescription_Record, index=['Row Count'])
nan_counts_GP_Prescription = pd.DataFrame(nan_counts_GP_Prescription_Record, index=['NaN Count'])
empty_counts_GP_Prescription = pd.DataFrame(empty_counts_GP_Prescription_Record, index=['Empty Count'])

# Concatenate the DataFrames
result_GP_Prescription_Record = []
result_GP_Prescription_Record = pd.concat([unique_counts_GP_Prescription, row_counts_GP_Prescription, nan_counts_GP_Prescription, empty_counts_GP_Prescription])

# Display the combined DataFrame
#print("GP Prescription Dataset Record:")
#print()
#display(result_GP_Prescription_Record)




#GP_Prescription_Record.head(3)


# **2l. Merge the datasets "Death_Date_Record" and "Death_Cause_Record" based on the "Participant ID" variable**

# In[ ]:


### Merge the datasets based on the "Participant ID" column
Death_Pair_datasets = []
Death_Pair_datasets = pd.merge(Death_Date_Record, Death_Cause_Record,   on="Participant ID", how="outer")
Death_Pair_datasets = Death_Pair_datasets.sort_values(by=['Participant ID'])




# Create dictionaries to store unique counts, row counts, NaN counts, and empty counts
unique_counts_Death_Pair_datasets = {}
row_counts_Death_Pair_datasets = {}
nan_counts_Death_Pair_datasets = {}
empty_counts_Death_Pair_datasets = {}

# Loop through columns and count unique items, row counts, NaN counts, and empty counts
for column_Death_Pair_datasets in Death_Pair_datasets.columns:
    unique_count_Death_Pair_datasets = Death_Pair_datasets[column_Death_Pair_datasets].nunique()
    row_count_Death_Pair_datasets = len(Death_Pair_datasets[column_Death_Pair_datasets])
    nan_count_Death_Pair_datasets = Death_Pair_datasets[column_Death_Pair_datasets].isna().sum()  # Count NaN values
    empty_count_Death_Pair_datasets = Death_Pair_datasets[column_Death_Pair_datasets].eq('').sum()  # Count empty string values

    unique_counts_Death_Pair_datasets[column_Death_Pair_datasets] = [unique_count_Death_Pair_datasets]
    row_counts_Death_Pair_datasets[column_Death_Pair_datasets] = [row_count_Death_Pair_datasets]
    nan_counts_Death_Pair_datasets[column_Death_Pair_datasets] = [nan_count_Death_Pair_datasets]
    empty_counts_Death_Pair_datasets[column_Death_Pair_datasets] = [empty_count_Death_Pair_datasets]

# Create DataFrames from the dictionaries
unique_counts_Death_Pair = []
row_counts_Death_Pair = []
nan_counts_Death_Pair = []
empty_counts_Death_Pair = []

unique_counts_Death_Pair = pd.DataFrame(unique_counts_Death_Pair_datasets, index=['Unique Count'])
row_counts_Death_Pair = pd.DataFrame(row_counts_Death_Pair_datasets, index=['Row Count'])
nan_counts_Death_Pair = pd.DataFrame(nan_counts_Death_Pair_datasets, index=['NaN Count'])
empty_counts_Death_Pair = pd.DataFrame(empty_counts_Death_Pair_datasets, index=['Empty Count'])

# Concatenate the DataFrames
result_Death_Pair_datasets = []
result_Death_Pair_datasets = pd.concat([unique_counts_Death_Pair, row_counts_Death_Pair, nan_counts_Death_Pair, empty_counts_Death_Pair])

# Display the combined DataFrame
#print("Death Date & Cause Paired Datasets:")
#print()
#display(result_Death_Pair_datasets)




#Death_Pair_datasets.head(3)


# In[ ]:


### Count NaN values in the DataFrame
nan_counts_in_Death_Pair_datasets = []
nan_counts_in_Death_Pair_datasets = Death_Pair_datasets.isna().sum()
#nan_counts_in_Death_Pair_datasets


# In[ ]:


### Create a Boolean mask to identify rows with NaN values
nan_mask = []
nan_mask = Death_Pair_datasets.isna().any(axis=1)

#### Use the mask to extract and display rows with NaN values
rows_with_nan_in_Death_Pair_datasets = Death_Pair_datasets[nan_mask]

#### Display the rows with NaN values
#rows_with_nan_in_Death_Pair_datasets.head(5)


# **2m. Merge the datsets: "Death_Pair_datasets" and "All_ICD10_with_Diseases_Dates_Data**

# In[ ]:


All_ICD10_with_Diseases_Dates_Data = []
All_ICD10_with_Diseases_Dates_Data = pd.read_csv('All ICD10 Codes with Diseases Names and Dates Data.csv')
#All_ICD10_with_Diseases_Dates_Data.head(3)                                                 


# In[ ]:


Final_Dataset = []
Final_Dataset = pd.merge(Death_Pair_datasets,All_ICD10_with_Diseases_Dates_Data,   on="Participant ID", how="outer")
new_order = ['Participant ID', 'Year of Birth', 'Month of Birth' , 'Sex' , 'Ethnicity' ,  'Combined ICD10 Diagnosis Date', 'Combined ICD10 Diseases' , 'Date of Death' , 'Death Cause Diseases' , 'Combined ICD10 Codes','Death Cause Disease ICD10 Codes']  # Specify the order of columns
Final_Dataset = Final_Dataset[new_order]
Final_Dataset = Final_Dataset.sort_values(by=['Participant ID', 'Combined ICD10 Diagnosis Date'])




# Create dictionaries to store unique counts, row counts, NaN counts, and empty counts
unique_counts_Final_Dataset = {}
row_counts_Final_Dataset = {}
nan_counts_Final_Dataset = {}
empty_counts_Final_Dataset = {}

# Loop through columns and count unique items, row counts, NaN counts, and empty counts
for column_Final_Dataset in Final_Dataset.columns:
    unique_count_Final_Dataset = Final_Dataset[column_Final_Dataset].nunique()
    row_count_Final_Dataset = len(Final_Dataset[column_Final_Dataset])
    nan_count_Final_Dataset = Final_Dataset[column_Final_Dataset].isna().sum()  # Count NaN values
    empty_count_Final_Dataset = Final_Dataset[column_Final_Dataset].eq('').sum()  # Count empty string values

    unique_counts_Final_Dataset[column_Final_Dataset] = [unique_count_Final_Dataset]
    row_counts_Final_Dataset[column_Final_Dataset] = [row_count_Final_Dataset]
    nan_counts_Final_Dataset[column_Final_Dataset] = [nan_count_Final_Dataset]
    empty_counts_Final_Dataset[column_Final_Dataset] = [empty_count_Final_Dataset]

# Create DataFrames from the dictionaries
unique_counts_Final_Dataset_Record = []
row_counts_Final_Dataset_Record = []
nan_counts_Final_Dataset_Record = []
empty_counts_Final_Dataset_Record = []

unique_counts_Final_Dataset_Record = pd.DataFrame(unique_counts_Final_Dataset, index=['Unique Count'])
row_counts_Final_Dataset_Record = pd.DataFrame(row_counts_Final_Dataset, index=['Row Count'])
nan_counts_Final_Dataset_Record = pd.DataFrame(nan_counts_Final_Dataset, index=['NaN Count'])
empty_counts_Final_Dataset_Record = pd.DataFrame(empty_counts_Final_Dataset, index=['Empty Count'])

# Concatenate the DataFrames
result_Final_Dataset = []
result_Final_Dataset = pd.concat([unique_counts_Final_Dataset_Record, row_counts_Final_Dataset_Record, nan_counts_Final_Dataset_Record, empty_counts_Final_Dataset_Record])

# Display the combined DataFrame
#print("Final (ICD10 dataset & Death Datasets) Dataset Record:")
#print()
#display(result_Final_Dataset)
#print()
#Final_Dataset.head(5)


# **2n. Drop Duplicates**

# In[ ]:


Final_Dataset = Final_Dataset.drop_duplicates()
Dropped_Duplicates_Final_Dataset = []
Dropped_Duplicates_Final_Dataset = Final_Dataset



# Create dictionaries to store unique counts, row counts, NaN counts, and empty counts
unique_counts_Dropped_Duplicates_Final_Dataset = {}
row_counts_Dropped_Duplicates_Final_Dataset = {}
nan_counts_Dropped_Duplicates_Final_Dataset = {}
empty_counts_Dropped_Duplicates_Final_Dataset = {}

# Loop through columns and count unique items, row counts, NaN counts, and empty counts
for column_Dropped_Duplicates_Final_Dataset in Dropped_Duplicates_Final_Dataset.columns:
    unique_count_Dropped_Duplicates_Final_Dataset = Dropped_Duplicates_Final_Dataset[column_Dropped_Duplicates_Final_Dataset].nunique()
    row_count_Dropped_Duplicates_Final_Dataset = len(Dropped_Duplicates_Final_Dataset[column_Dropped_Duplicates_Final_Dataset])
    nan_count_Dropped_Duplicates_Final_Dataset = Dropped_Duplicates_Final_Dataset[column_Dropped_Duplicates_Final_Dataset].isna().sum()  # Count NaN values
    empty_count_Dropped_Duplicates_Final_Dataset = Dropped_Duplicates_Final_Dataset[column_Dropped_Duplicates_Final_Dataset].eq('').sum()  # Count empty string values

    unique_counts_Dropped_Duplicates_Final_Dataset[column_Dropped_Duplicates_Final_Dataset] = [unique_count_Dropped_Duplicates_Final_Dataset]
    row_counts_Dropped_Duplicates_Final_Dataset[column_Dropped_Duplicates_Final_Dataset] = [row_count_Dropped_Duplicates_Final_Dataset]
    nan_counts_Dropped_Duplicates_Final_Dataset[column_Dropped_Duplicates_Final_Dataset] = [nan_count_Dropped_Duplicates_Final_Dataset]
    empty_counts_Dropped_Duplicates_Final_Dataset[column_Dropped_Duplicates_Final_Dataset] = [empty_count_Dropped_Duplicates_Final_Dataset]

# Create DataFrames from the dictionaries
unique_counts_Dropped_Duplicates_Final_Dataset_Record = []
row_counts_Dropped_Duplicates_Final_Dataset_Record = []
nan_counts_Dropped_Duplicates_Final_Dataset_Record = []
empty_counts_Dropped_Duplicates_Final_Dataset_Record = []

unique_counts_Dropped_Duplicates_Final_Dataset_Record = pd.DataFrame(unique_counts_Dropped_Duplicates_Final_Dataset, index=['Unique Count'])
row_counts_Dropped_Duplicates_Final_Dataset_Record = pd.DataFrame(row_counts_Dropped_Duplicates_Final_Dataset, index=['Row Count'])
nan_counts_Dropped_Duplicates_Final_Dataset_Record = pd.DataFrame(nan_counts_Dropped_Duplicates_Final_Dataset, index=['NaN Count'])
empty_counts_Dropped_Duplicates_Final_Dataset_Record = pd.DataFrame(empty_counts_Dropped_Duplicates_Final_Dataset, index=['Empty Count'])

# Concatenate the DataFrames
result_Dropped_Duplicates_Final_Dataset = []
result_Dropped_Duplicates_Final_Dataset = pd.concat([unique_counts_Dropped_Duplicates_Final_Dataset_Record, row_counts_Dropped_Duplicates_Final_Dataset_Record, nan_counts_Dropped_Duplicates_Final_Dataset_Record, empty_counts_Dropped_Duplicates_Final_Dataset_Record])

# Display the combined DataFrame
#print("Dropped Duplicates Final (ICD10 dataset & Death Datasets) Dataset Record:")
#print()
#display(result_Dropped_Duplicates_Final_Dataset)
#print()
#Final_Dataset.head(5)


# In[ ]:


#### Count NaN values in the DataFrame
nan_counts_Final_Dataset = []
nan_counts_Final_Dataset = Final_Dataset.isna().sum()
#nan_counts_Final_Dataset


# In[ ]:


### Create a Boolean mask to identify rows with NaN values
nan_mask_Final_Dataset = []
nan_mask_Final_Dataset = Final_Dataset[['Year of Birth', 'Month of Birth' , 'Sex' , 'Combined ICD10 Diagnosis Date' , 'Combined ICD10 Codes' , 'Combined ICD10 Codes']].isna().any(axis=1)

### Use the mask to extract and display rows with NaN values
rows_with_nan_Final_Dataset = []
rows_with_nan_Final_Dataset = Final_Dataset[nan_mask_Final_Dataset]

#### Display the rows with NaN values
#rows_with_nan_Final_Dataset.head(5)


# In[ ]:


#### List of columns with NaN values to consider
columns_with_nan = []
columns_with_nan = ["Year of Birth", "Month of Birth", "Sex", "Combined ICD10 Diagnosis Date", "Combined ICD10 Diseases", "Combined ICD10 Codes"]
columns_with_nan



#### Remove rows with NaN values in the specified columns
Final_Dataset = Final_Dataset.dropna(subset=columns_with_nan)
#Final_Dataset.head(5)


# In[ ]:


#### Count NaN values in the DataFrame
nan_counts_Final_Dataset = []
nan_counts_Final_Dataset = Final_Dataset.isna().sum()
#nan_counts_Final_Dataset


# **2o. Create a new variable in the dataset: "Alive / Dead**

# In[ ]:


#### Create a new column "Alive / Dead" based on the condition
import numpy as np
Final_Dataset['Alive / Dead'] = np.where(Final_Dataset['Date of Death'].isna(), 'Alive', 'Dead')

Final_Dataset2 = []
Final_Dataset2 = Final_Dataset



# Create dictionaries to store unique counts, row counts, NaN counts, and empty counts
unique_counts_Final_Dataset2 = {}
row_counts_Final_Dataset2 = {}
nan_counts_Final_Dataset2 = {}
empty_counts_Final_Dataset2 = {}

# Loop through columns and count unique items, row counts, NaN counts, and empty counts
for column_Final_Dataset2 in Final_Dataset2.columns:
    unique_count_Final_Dataset2 = Final_Dataset2[column_Final_Dataset2].nunique()
    row_count_Final_Dataset2 = len(Final_Dataset2[column_Final_Dataset2])
    nan_count_Final_Dataset2 = Final_Dataset2[column_Final_Dataset2].isna().sum()  # Count NaN values
    empty_count_Final_Dataset2 = Final_Dataset2[column_Final_Dataset2].eq('').sum()  # Count empty string values

    unique_counts_Final_Dataset2[column_Final_Dataset2] = [unique_count_Final_Dataset2]
    row_counts_Final_Dataset2[column_Final_Dataset2] = [row_count_Final_Dataset2]
    nan_counts_Final_Dataset2[column_Final_Dataset2] = [nan_count_Final_Dataset2]
    empty_counts_Final_Dataset2[column_Final_Dataset2] = [empty_count_Final_Dataset2]

# Create DataFrames from the dictionaries
unique_counts_Final_Dataset_Record2 = []
row_counts_Final_Dataset_Record2 = []
nan_counts_Final_Dataset_Record2 = []
empty_counts_Final_Dataset_Record2 = []

unique_counts_Final_Dataset_Record2 = pd.DataFrame(unique_counts_Final_Dataset2, index=['Unique Count'])
row_counts_Final_Dataset_Record2 = pd.DataFrame(row_counts_Final_Dataset2, index=['Row Count'])
nan_counts_Final_Dataset_Record2 = pd.DataFrame(nan_counts_Final_Dataset2, index=['NaN Count'])
empty_counts_Final_Dataset_Record2 = pd.DataFrame(empty_counts_Final_Dataset2, index=['Empty Count'])

# Concatenate the DataFrames
result_Final_Dataset2 = []
result_Final_Dataset2 = pd.concat([unique_counts_Final_Dataset_Record2, row_counts_Final_Dataset_Record2, nan_counts_Final_Dataset_Record2, empty_counts_Final_Dataset_Record2])

# Display the combined DataFrame
#print("Updated Final (ICD10 dataset & Death Datasets) Dataset Record:")
#print()
#display(result_Final_Dataset2)
#print()


#Final_Dataset.head(3)


# **2p. Create the "Age" column in the dataset**

# In[ ]:


import pandas as pd
Dataset_with_ICD10_and_Diseases_Names_and_Death_Records = []
Dataset_with_ICD10_and_Diseases_Names_and_Death_Records = pd.read_csv('Dataset with ICD10 and Diseases Names and Death Records.csv')
#Dataset_with_ICD10_and_Diseases_Names_and_Death_Records.head(3)


# In[ ]:


# Create DataFrame
Dataset_with_ICD10_and_Diseases_Names_and_Death_Records = pd.DataFrame(Dataset_with_ICD10_and_Diseases_Names_and_Death_Records)

# Convert 'Date of Death' to datetime, handling errors by coercing to NaT
Dataset_with_ICD10_and_Diseases_Names_and_Death_Records['Date of Death'] = pd.to_datetime(Dataset_with_ICD10_and_Diseases_Names_and_Death_Records['Date of Death'], errors='coerce')

# Calculate the age, only where 'Date of Death' is not NaT
Dataset_with_ICD10_and_Diseases_Names_and_Death_Records['Individual Age'] = Dataset_with_ICD10_and_Diseases_Names_and_Death_Records.apply(
    lambda row: row['Date of Death'].year - row['Year of Birth'] if pd.notnull(row['Date of Death']) else np.nan,
    axis=1
)


# Convert 'Combined ICD10 Diagnosis Date' to datetime
Dataset_with_ICD10_and_Diseases_Names_and_Death_Records['Combined ICD10 Diagnosis Date'] = pd.to_datetime(Dataset_with_ICD10_and_Diseases_Names_and_Death_Records['Combined ICD10 Diagnosis Date'], errors='coerce')

# Find the latest diagnosis date for each participant
latest_dates = Dataset_with_ICD10_and_Diseases_Names_and_Death_Records.groupby('Participant ID')['Combined ICD10 Diagnosis Date'].max().reset_index()

# Rename the column to 'Latest Diagnosis Date'
latest_dates.rename(columns={'Combined ICD10 Diagnosis Date': 'Latest Diagnosis Date'}, inplace=True)

# Merge the latest dates back into the original DataFrame
Dataset_with_ICD10_and_Diseases_Names_and_Death_Records = Dataset_with_ICD10_and_Diseases_Names_and_Death_Records.merge(latest_dates, on='Participant ID', how='left')



# Convert 'Date of Death' to datetime, handling errors by coercing to NaT
Dataset_with_ICD10_and_Diseases_Names_and_Death_Records['Latest Diagnosis Date'] = pd.to_datetime(Dataset_with_ICD10_and_Diseases_Names_and_Death_Records['Latest Diagnosis Date'], errors='coerce')


# Replace NaN values in 'Individual Age' with the difference between 'Latest Diagnosis Date' and 'Year of Birth'
Dataset_with_ICD10_and_Diseases_Names_and_Death_Records['Individual Age'] = Dataset_with_ICD10_and_Diseases_Names_and_Death_Records.apply(
    lambda row: row['Latest Diagnosis Date'].year - row['Year of Birth'] if pd.isnull(row['Individual Age']) else row['Individual Age'],
    axis=1
)


# Drop the 'Latest Diagnosis Date' column
Dataset_with_ICD10_and_Diseases_Names_and_Death_Records.drop(columns=['Latest Diagnosis Date'], inplace=True)

#Dataset_with_ICD10_and_Diseases_Names_and_Death_Records.head(3)


# In[ ]:


# Define the age ranges
bins = [30, 40, 50, 60, 70, 80, 90, 100]
labels = ["30 - 40", "41 - 50", "51 - 60", "61 - 70", "71 - 80", "81 - 90", "91 - 100"]

# Create a new column 'Age Range' with the defined bins
Dataset_with_ICD10_and_Diseases_Names_and_Death_Records['Age Range'] = pd.cut(Dataset_with_ICD10_and_Diseases_Names_and_Death_Records['Individual Age'], bins=bins, labels=labels, right=False)
#Dataset_with_ICD10_and_Diseases_Names_and_Death_Records.head(3)


# In[ ]:


#file_path = []

## Specify the file path where you want to save the CSV file
#file_path = 'Dataset with ICD10 and Diseases Names and Death Records.csv'

## Use the to_csv method to save the DataFrame as a CSV file
#Dataset_with_ICD10_and_Diseases_Names_and_Death_Records.to_csv(file_path, index=False)  # Set index=False to exclude the index column


# <div style="background-color: #d3f5d3; padding: 10px;">
#     <h2><center> Age - Range Count -for UKB</center></h2>
# </div>

# In[ ]:


Dataset_with_ICD10_and_Diseases_Names_and_Death_Records = []
Dataset_with_ICD10_and_Diseases_Names_and_Death_Records = pd.read_csv('Dataset with ICD10 and Diseases Names and Death Records.csv')
#Dataset_with_ICD10_and_Diseases_Names_and_Death_Records.head(3)


# In[ ]:


# Total number of participants
total_participants = []
total_participants = 440014

# Drop duplicate Participant ID rows to get unique participants
unique_participants = []
unique_participants = Dataset_with_ICD10_and_Diseases_Names_and_Death_Records.drop_duplicates(subset=['Participant ID'])


# Count occurrences of each age range
age_range_counts = []
age_range_counts = unique_participants['Age Range'].value_counts().sort_index()

# Calculate percentages
age_range_percentages = (age_range_counts / total_participants) * 100

# Display the results
for age_range, count in age_range_counts.items():
    percentage = age_range_percentages[age_range]
    print(f"{age_range} : {count} ({percentage:.2f} %)")


# <div style="background-color: #d3f5d3; padding: 10px;">
#     <h2><center>3. Sex and Ethnicity Count -for UKB</center></h2>
# </div>

# **3a. Import the "Final Dataset"**

# In[ ]:


All_ICD10_with_Diseases_Dates_Data = []
All_ICD10_with_Diseases_Dates_Data = pd.read_csv('Dataset with ICD10 and Diseases Names and Death Records.csv')
#All_ICD10_with_Diseases_Dates_Data.head(3)


# In[ ]:


# Display the combined DataFrame
#print("Dropped Duplicates from Data Table Record:")
#print()
#display(result_dropped_duplicates_data_table)

# Create dictionaries to store unique counts, row counts, NaN counts, and empty counts
unique_counts_All_ICD10_with_Diseases_Dates_Data = {}
row_counts_All_ICD10_with_Diseases_Dates_Data = {}
nan_counts_All_ICD10_with_Diseases_Dates_Data = {}
empty_counts_All_ICD10_with_Diseases_Dates_Data = {}

# Loop through columns and count unique items, row counts, NaN counts, and empty counts
for column_All_ICD10_with_Diseases_Dates_Data in All_ICD10_with_Diseases_Dates_Data.columns:
    unique_count_All_ICD10_with_Diseases_Dates_Data = All_ICD10_with_Diseases_Dates_Data[column_All_ICD10_with_Diseases_Dates_Data].nunique()
    row_count_All_ICD10_with_Diseases_Dates_Data = len(All_ICD10_with_Diseases_Dates_Data[column_All_ICD10_with_Diseases_Dates_Data])
    nan_count_All_ICD10_with_Diseases_Dates_Data = All_ICD10_with_Diseases_Dates_Data[column_All_ICD10_with_Diseases_Dates_Data].isna().sum()  # Count NaN values
    empty_count_All_ICD10_with_Diseases_Dates_Data = All_ICD10_with_Diseases_Dates_Data[column_All_ICD10_with_Diseases_Dates_Data].eq('').sum()  # Count empty string values

    unique_counts_All_ICD10_with_Diseases_Dates_Data[column_All_ICD10_with_Diseases_Dates_Data] = [unique_count_All_ICD10_with_Diseases_Dates_Data]
    row_counts_All_ICD10_with_Diseases_Dates_Data[column_All_ICD10_with_Diseases_Dates_Data] = [row_count_All_ICD10_with_Diseases_Dates_Data]
    nan_counts_All_ICD10_with_Diseases_Dates_Data[column_All_ICD10_with_Diseases_Dates_Data] = [nan_count_All_ICD10_with_Diseases_Dates_Data]
    empty_counts_All_ICD10_with_Diseases_Dates_Data[column_All_ICD10_with_Diseases_Dates_Data] = [empty_count_All_ICD10_with_Diseases_Dates_Data]

# Create DataFrames from the dictionaries
unique_counts_All_ICD10_with_Diseases_Dates_Datas = []
row_counts_All_ICD10_with_Diseases_Dates_Datas = []
nan_counts_All_ICD10_with_Diseases_Dates_Datas = []
empty_counts_All_ICD10_with_Diseases_Dates_Datas = []

unique_counts_All_ICD10_with_Diseases_Dates_Datas = pd.DataFrame(unique_counts_All_ICD10_with_Diseases_Dates_Data, index=['Unique Count'])
row_counts_All_ICD10_with_Diseases_Dates_Datas = pd.DataFrame(row_counts_All_ICD10_with_Diseases_Dates_Data, index=['Row Count'])
nan_counts_All_ICD10_with_Diseases_Dates_Datas = pd.DataFrame(nan_counts_All_ICD10_with_Diseases_Dates_Data, index=['NaN Count'])
empty_counts_All_ICD10_with_Diseases_Dates_Datas = pd.DataFrame(empty_counts_All_ICD10_with_Diseases_Dates_Data, index=['Empty Count'])

# Concatenate the DataFrames
result_All_ICD10_with_Diseases_Dates_Data = []
result_All_ICD10_with_Diseases_Dates_Data = pd.concat([unique_counts_All_ICD10_with_Diseases_Dates_Datas, row_counts_All_ICD10_with_Diseases_Dates_Datas, nan_counts_All_ICD10_with_Diseases_Dates_Datas, empty_counts_All_ICD10_with_Diseases_Dates_Datas])

# Display the combined DataFrame
#print("All_ICD10_with_Diseases_Dates_Data Record:")
#print()
#display(result_All_ICD10_with_Diseases_Dates_Data)
#print()

#All_ICD10_with_Diseases_Dates_Data.head(5)


# **3a. Count the number of Male and Female and Ethnicity items counts**

# In[ ]:


# Total number of participants
total_participants = []
total_participants = 440014



# Drop duplicate Participant ID rows to get unique participants
unique_participants = []
unique_participants = All_ICD10_with_Diseases_Dates_Data.drop_duplicates(subset=['Participant ID'])


# Count the number of each sex
sex_counts = []
sex_counts = unique_participants['Sex'].value_counts()

# Calculate the percentage for each ethnicity
sex_percentages = []
sex_percentages = (sex_counts / total_participants) * 100

# Combine counts and percentages
sex_counts_with_percentages = []
sex_counts_with_percentages = sex_counts.astype(str) + " (" + sex_percentages.round(2).astype(str) + "%)"



# Count the number of missing (NaN) values in each column
missing_counts = []
missing_counts = unique_participants.isna().sum()

# Get unique items in the "Ethnicity" column
unique_ethnicities = []
unique_ethnicities = unique_participants['Ethnicity'].unique()

# Count the number of each unique ethnicity
ethnicity_counts = []
ethnicity_counts = unique_participants['Ethnicity'].value_counts()



# Calculate the percentage for each ethnicity
ethnicity_percentages = []
ethnicity_percentages = (ethnicity_counts / total_participants) * 100

# Combine counts and percentages
ethnicity_counts_with_percentages = []
ethnicity_counts_with_percentages = ethnicity_counts.astype(str) + " (" + ethnicity_percentages.round(2).astype(str) + "%)"


# Print the counts
#print("Sex Counts with Percentages:")
#print(sex_counts_with_percentages)
#print()
#print("\nEthnicity Counts with Percentages:")
#print(ethnicity_counts_with_percentages)
#print()
#print("\nMissing Values Counts:")
#print(missing_counts)


# <div style="background-color: #d3f5d3; padding: 10px;">
#     <h2><center>4. Importing UK Biobank Dataset (Smoking Records)-for UKB</center></h2>
# </div>

# In[ ]:


All_ICD10_with_Diseases_Dates_Data = []
All_ICD10_with_Diseases_Dates_Data = pd.read_csv('Dataset with ICD10 and Diseases Names and Death Records.csv')
#All_ICD10_with_Diseases_Dates_Data.head(3)


# **3a. Import Smoking Dataset from UK Biobank**

# In[ ]:


UKB_Smoking_Records = []
UKB_Smoking_Records = pd.read_csv('UK_biobank_Smoking_data.csv')

# Rename multiple variables
UKB_Smoking_Records = UKB_Smoking_Records.rename(columns={"eid": "Participant ID", 
                        "20116-0.0": "Smoking status_Instance 0(2006-2010)",
                        "20116-1.0": "Smoking status_Instance 1(2012-2013)",
                        "20116-2.0": "Smoking status_Instance 2(2014+)",
                        "20116-3.0": "Smoking status_Instance 3(2019+)",
                        "2644-0.0": "Light smokers_Instance 0(2006-2010)",
                        "2644-1.0": "Light smokers_Instance 0(2012-2013)",
                        "2644-2.0": "Light smokers_Instance 0(2014+)",
                        "2644-3.0": "Light smokers_Instance 0(2019+)"})
UKB_Smoking_Records = UKB_Smoking_Records.drop_duplicates()

# Create dictionaries to store unique counts, row counts, NaN counts, and empty counts
unique_counts_UKB_Smoking_Records = {}
row_counts_UKB_Smoking_Records = {}
nan_counts_UKB_Smoking_Records = {}
empty_counts_UKB_Smoking_Records = {}

# Loop through columns and count unique items, row counts, NaN counts, and empty counts
for column_UKB_Smoking_Records in UKB_Smoking_Records.columns:
    unique_count_UKB_Smoking_Records = UKB_Smoking_Records[column_UKB_Smoking_Records].nunique()
    row_count_UKB_Smoking_Records = len(UKB_Smoking_Records[column_UKB_Smoking_Records])
    nan_count_UKB_Smoking_Records = UKB_Smoking_Records[column_UKB_Smoking_Records].isna().sum()  # Count NaN values
    empty_count_UKB_Smoking_Records = UKB_Smoking_Records[column_UKB_Smoking_Records].eq('').sum()  # Count empty string values

    unique_counts_UKB_Smoking_Records[column_UKB_Smoking_Records] = [unique_count_UKB_Smoking_Records]
    row_counts_UKB_Smoking_Records[column_UKB_Smoking_Records] = [row_count_UKB_Smoking_Records]
    nan_counts_UKB_Smoking_Records[column_UKB_Smoking_Records] = [nan_count_UKB_Smoking_Records]
    empty_counts_UKB_Smoking_Records[column_UKB_Smoking_Records] = [empty_count_UKB_Smoking_Records]

# Create DataFrames from the dictionaries
unique_counts_UKB_Smoking_Record = []
row_counts_UKB_Smoking_Record = []
nan_counts_UKB_Smoking_Record = []
empty_counts_UKB_Smoking_Record = []

unique_counts_UKB_Smoking_Record = pd.DataFrame(unique_counts_UKB_Smoking_Records, index=['Unique Count'])
row_counts_UKB_Smoking_Record = pd.DataFrame(row_counts_UKB_Smoking_Records, index=['Row Count'])
nan_counts_UKB_Smoking_Record = pd.DataFrame(nan_counts_UKB_Smoking_Records, index=['NaN Count'])
empty_counts_UKB_Smoking_Record = pd.DataFrame(empty_counts_UKB_Smoking_Records, index=['Empty Count'])

# Concatenate the DataFrames
result_UKB_Smoking_Records = []
result_UKB_Smoking_Records = pd.concat([unique_counts_UKB_Smoking_Record, row_counts_UKB_Smoking_Record, nan_counts_UKB_Smoking_Record, empty_counts_UKB_Smoking_Record])

# Display the combined DataFrame
#print("UKB_Smoking_Records:")
#print()
#display(result_UKB_Smoking_Records)

#UKB_Smoking_Records.head(3)


# **3b. I removed the all the columns named "Light smokers_Instance" as they are not required**

# In[ ]:


columns_to_check = []
columns_to_check = ['Smoking status_Instance 0(2006-2010)',
                    'Smoking status_Instance 1(2012-2013)',
                    'Smoking status_Instance 2(2014+)',
                    'Smoking status_Instance 3(2019+)']

# Create a new column 'Smoking Status' and fill it with non-NaN values from the specified columns
UKB_Smoking_Records['Smoking Status'] = UKB_Smoking_Records[columns_to_check].apply(lambda row: next((value for value in row if not pd.isna(value)), np.nan), axis=1)


columns_to_drop = []
columns_to_drop = ['Smoking status_Instance 0(2006-2010)',
                   'Smoking status_Instance 1(2012-2013)',
                   'Smoking status_Instance 2(2014+)',
                   'Smoking status_Instance 3(2019+)']

# Drop the specified columns
UKB_Smoking_Records.drop(columns=columns_to_drop, inplace=True)



columns_to_check = []
columns_to_check = ['Light smokers_Instance 0(2006-2010)',
                    'Light smokers_Instance 0(2012-2013)',
                    'Light smokers_Instance 0(2014+)',
                    'Light smokers_Instance 0(2019+)']

# Create a new column 'Smoking Status' and fill it with non-NaN values from the specified columns
#UKB_Smoking_Records['Occassional Smoking'] = UKB_Smoking_Records[columns_to_check].apply(lambda row: next((value for value in row if not pd.isna(value)), np.nan), axis=1)


columns_to_drop = []
columns_to_drop = ['Light smokers_Instance 0(2006-2010)',
                    'Light smokers_Instance 0(2012-2013)',
                    'Light smokers_Instance 0(2014+)',
                    'Light smokers_Instance 0(2019+)']

# Drop the specified columns
UKB_Smoking_Records.drop(columns=columns_to_drop, inplace=True)



# Create dictionaries to store unique counts, row counts, NaN counts, and empty counts
unique_counts_UKB_Smoking_Records = {}
row_counts_UKB_Smoking_Records = {}
nan_counts_UKB_Smoking_Records = {}
empty_counts_UKB_Smoking_Records = {}
prefer_not_to_say_counts_UKB_Smoking_Records = {}

# Loop through columns and count unique items, row counts, NaN counts, and empty counts
for column_UKB_Smoking_Records in UKB_Smoking_Records.columns:
    unique_count_UKB_Smoking_Records = UKB_Smoking_Records[column_UKB_Smoking_Records].nunique()
    row_count_UKB_Smoking_Records = len(UKB_Smoking_Records[column_UKB_Smoking_Records])
    nan_count_UKB_Smoking_Records = UKB_Smoking_Records[column_UKB_Smoking_Records].isna().sum()  # Count NaN values
    empty_count_UKB_Smoking_Records = UKB_Smoking_Records[column_UKB_Smoking_Records].eq('').sum()  # Count empty string values
    prefer_not_to_say_count_UKB_Smoking_Records = UKB_Smoking_Records[column_UKB_Smoking_Records].eq('Prefer not to answer').sum()  

    unique_counts_UKB_Smoking_Records[column_UKB_Smoking_Records] = [unique_count_UKB_Smoking_Records]
    row_counts_UKB_Smoking_Records[column_UKB_Smoking_Records] = [row_count_UKB_Smoking_Records]
    nan_counts_UKB_Smoking_Records[column_UKB_Smoking_Records] = [nan_count_UKB_Smoking_Records]
    empty_counts_UKB_Smoking_Records[column_UKB_Smoking_Records] = [empty_count_UKB_Smoking_Records]
    prefer_not_to_say_counts_UKB_Smoking_Records[column_UKB_Smoking_Records] = [prefer_not_to_say_count_UKB_Smoking_Records]




    

# Create DataFrames from the dictionaries
unique_counts_UKB_Smoking_Record = []
row_counts_UKB_Smoking_Record = []
nan_counts_UKB_Smoking_Record = []
empty_counts_UKB_Smoking_Record = []
prefer_not_to_say_counts_UKB_Smoking_Record =[]

unique_counts_UKB_Smoking_Record = pd.DataFrame(unique_counts_UKB_Smoking_Records, index=['Unique Count'])
row_counts_UKB_Smoking_Record = pd.DataFrame(row_counts_UKB_Smoking_Records, index=['Row Count'])
nan_counts_UKB_Smoking_Record = pd.DataFrame(nan_counts_UKB_Smoking_Records, index=['NaN Count'])
empty_counts_UKB_Smoking_Record = pd.DataFrame(empty_counts_UKB_Smoking_Records, index=['Empty Count'])
prefer_not_to_say_counts_UKB_Smoking_Record = pd.DataFrame(prefer_not_to_say_counts_UKB_Smoking_Records, index=['Prefer not to answer'])

# Concatenate the DataFrames
result_UKB_Smoking_Records = []
result_UKB_Smoking_Records = pd.concat([unique_counts_UKB_Smoking_Record, row_counts_UKB_Smoking_Record, nan_counts_UKB_Smoking_Record, empty_counts_UKB_Smoking_Record,prefer_not_to_say_counts_UKB_Smoking_Record])

# Display the combined DataFrame
print("UKB_Smoking_Records:")
print()
display(result_UKB_Smoking_Records)



# Display unique items under the column "Smoking Status"
unique_smoking_status = []
unique_smoking_status = UKB_Smoking_Records['Smoking Status'].unique()
# Print the unique items
display(unique_smoking_status)


# Display unique items under the column "Smoking Status"
#unique_smoking_status = []
#unique_smoking_status = UKB_Smoking_Records['Occassional Smoking'].unique()
# Print the unique items
#display(unique_smoking_status)



# Display the updated DataFrame
#UKB_Smoking_Records.head(3)


# In[ ]:


#file_path = []

## Specify the file path where you want to save the CSV file
#file_path = 'Smoking Status Record Dataset.csv'

## Use the to_csv method to save the DataFrame as a CSV file
#UKB_Smoking_Records.to_csv(file_path, index=False)  # Set index=False to exclude the index column


# **3c. Remove rows with NaN and "Prefer not to answer" values from the DataFrame named "UKB_Smoking_Records"**

# In[ ]:


# Remove rows with NaN values in the "Smoking Status" column
UKB_Smoking_Records = UKB_Smoking_Records.dropna(subset=["Smoking Status"])

# Filter out rows with "Prefer not to answer" values in the "Smoking Status" column
UKB_Smoking_Records = UKB_Smoking_Records[UKB_Smoking_Records["Smoking Status"] != "Prefer not to answer"]

# Reset index
UKB_Smoking_Records.reset_index(drop=True, inplace=True)

# Create dictionaries to store unique counts, row counts, NaN counts, and empty counts
unique_counts_UKB_Smoking_Records = {}
row_counts_UKB_Smoking_Records = {}
nan_counts_UKB_Smoking_Records = {}
empty_counts_UKB_Smoking_Records = {}
prefer_not_to_say_counts_UKB_Smoking_Records = {}

# Loop through columns and count unique items, row counts, NaN counts, and empty counts
for column_UKB_Smoking_Records in UKB_Smoking_Records.columns:
    unique_count_UKB_Smoking_Records = UKB_Smoking_Records[column_UKB_Smoking_Records].nunique()
    row_count_UKB_Smoking_Records = len(UKB_Smoking_Records[column_UKB_Smoking_Records])
    nan_count_UKB_Smoking_Records = UKB_Smoking_Records[column_UKB_Smoking_Records].isna().sum()  # Count NaN values
    empty_count_UKB_Smoking_Records = UKB_Smoking_Records[column_UKB_Smoking_Records].eq('').sum()  # Count empty string values
    prefer_not_to_say_count_UKB_Smoking_Records = UKB_Smoking_Records[column_UKB_Smoking_Records].eq('Prefer not to answer').sum()  

    unique_counts_UKB_Smoking_Records[column_UKB_Smoking_Records] = [unique_count_UKB_Smoking_Records]
    row_counts_UKB_Smoking_Records[column_UKB_Smoking_Records] = [row_count_UKB_Smoking_Records]
    nan_counts_UKB_Smoking_Records[column_UKB_Smoking_Records] = [nan_count_UKB_Smoking_Records]
    empty_counts_UKB_Smoking_Records[column_UKB_Smoking_Records] = [empty_count_UKB_Smoking_Records]
    prefer_not_to_say_counts_UKB_Smoking_Records[column_UKB_Smoking_Records] = [prefer_not_to_say_count_UKB_Smoking_Records]




    

# Create DataFrames from the dictionaries
unique_counts_UKB_Smoking_Record = []
row_counts_UKB_Smoking_Record = []
nan_counts_UKB_Smoking_Record = []
empty_counts_UKB_Smoking_Record = []
prefer_not_to_say_counts_UKB_Smoking_Record =[]

unique_counts_UKB_Smoking_Record = pd.DataFrame(unique_counts_UKB_Smoking_Records, index=['Unique Count'])
row_counts_UKB_Smoking_Record = pd.DataFrame(row_counts_UKB_Smoking_Records, index=['Row Count'])
nan_counts_UKB_Smoking_Record = pd.DataFrame(nan_counts_UKB_Smoking_Records, index=['NaN Count'])
empty_counts_UKB_Smoking_Record = pd.DataFrame(empty_counts_UKB_Smoking_Records, index=['Empty Count'])
prefer_not_to_say_counts_UKB_Smoking_Record = pd.DataFrame(prefer_not_to_say_counts_UKB_Smoking_Records, index=['Prefer not to answer'])

# Concatenate the DataFrames
result_UKB_Smoking_Records = []
result_UKB_Smoking_Records = pd.concat([unique_counts_UKB_Smoking_Record, row_counts_UKB_Smoking_Record, nan_counts_UKB_Smoking_Record, empty_counts_UKB_Smoking_Record,prefer_not_to_say_counts_UKB_Smoking_Record])

# Display the combined DataFrame
#print("UKB_Smoking_Records:")
print()
#display(result_UKB_Smoking_Records)



# Display unique items under the column "Smoking Status"
unique_smoking_status = []
unique_smoking_status = UKB_Smoking_Records['Smoking Status'].unique()
# Print the unique items
#display(unique_smoking_status)
print()

# Count occurrences of unique values in the 'Smoking Status' column
smoking_status_counts = UKB_Smoking_Records['Smoking Status'].value_counts()
print()

# Display the counts
#print("Counts of unique values in the 'Smoking Status' column:")
#display(smoking_status_counts)

#UKB_Smoking_Records.head(3)


# **3d. Combine ICD10 codes dataset with UKB Smoking Dataset**

# In[ ]:


Combined_ICD10_codes_and_UKB_Smoking_Records = []
Combined_ICD10_codes_and_UKB_Smoking_Records = pd.merge(All_ICD10_with_Diseases_Dates_Data,UKB_Smoking_Records,   on="Participant ID", how="left")



# Create dictionaries to store unique counts, row counts, NaN counts, and empty counts
unique_counts_Combined_ICD10_codes_and_UKB_Smoking_Records = {}
row_counts_Combined_ICD10_codes_and_UKB_Smoking_Records = {}
nan_counts_Combined_ICD10_codes_and_UKB_Smoking_Records = {}
empty_counts_Combined_ICD10_codes_and_UKB_Smoking_Records = {}
prefer_not_to_say_counts_Combined_ICD10_codes_and_UKB_Smoking_Records = {}

# Loop through columns and count unique items, row counts, NaN counts, and empty counts
for column_Combined_ICD10_codes_and_UKB_Smoking_Records in Combined_ICD10_codes_and_UKB_Smoking_Records.columns:
    unique_count_Combined_ICD10_codes_and_UKB_Smoking_Records = Combined_ICD10_codes_and_UKB_Smoking_Records[column_Combined_ICD10_codes_and_UKB_Smoking_Records].nunique()
    row_count_Combined_ICD10_codes_and_UKB_Smoking_Records = len(Combined_ICD10_codes_and_UKB_Smoking_Records[column_Combined_ICD10_codes_and_UKB_Smoking_Records])
    nan_count_Combined_ICD10_codes_and_UKB_Smoking_Records = Combined_ICD10_codes_and_UKB_Smoking_Records[column_Combined_ICD10_codes_and_UKB_Smoking_Records].isna().sum()  # Count NaN values
    empty_count_Combined_ICD10_codes_and_UKB_Smoking_Records = Combined_ICD10_codes_and_UKB_Smoking_Records[column_Combined_ICD10_codes_and_UKB_Smoking_Records].eq('').sum()  # Count empty string values
    prefer_not_to_say_count_Combined_ICD10_codes_and_UKB_Smoking_Records = Combined_ICD10_codes_and_UKB_Smoking_Records[column_Combined_ICD10_codes_and_UKB_Smoking_Records].eq('Prefer not to answer').sum()  

    unique_counts_Combined_ICD10_codes_and_UKB_Smoking_Records[column_Combined_ICD10_codes_and_UKB_Smoking_Records] = [unique_count_Combined_ICD10_codes_and_UKB_Smoking_Records]
    row_counts_Combined_ICD10_codes_and_UKB_Smoking_Records[column_Combined_ICD10_codes_and_UKB_Smoking_Records] = [row_count_Combined_ICD10_codes_and_UKB_Smoking_Records]
    nan_counts_Combined_ICD10_codes_and_UKB_Smoking_Records[column_Combined_ICD10_codes_and_UKB_Smoking_Records] = [nan_count_Combined_ICD10_codes_and_UKB_Smoking_Records]
    empty_counts_Combined_ICD10_codes_and_UKB_Smoking_Records[column_Combined_ICD10_codes_and_UKB_Smoking_Records] = [empty_count_Combined_ICD10_codes_and_UKB_Smoking_Records]
    prefer_not_to_say_counts_Combined_ICD10_codes_and_UKB_Smoking_Records[column_Combined_ICD10_codes_and_UKB_Smoking_Records] = [prefer_not_to_say_count_Combined_ICD10_codes_and_UKB_Smoking_Records]




    

# Create DataFrames from the dictionaries
unique_counts_Combined_ICD10_codes_and_UKB_Smoking_Record = []
row_counts_Combined_ICD10_codes_and_UKB_Smoking_Record = []
nan_counts_Combined_ICD10_codes_and_UKB_Smoking_Record = []
empty_counts_Combined_ICD10_codes_and_UKB_Smoking_Record = []
prefer_not_to_say_counts_Combined_ICD10_codes_and_UKB_Smoking_Record =[]

unique_counts_Combined_ICD10_codes_and_UKB_Smoking_Record = pd.DataFrame(unique_counts_Combined_ICD10_codes_and_UKB_Smoking_Records, index=['Unique Count'])
row_counts_Combined_ICD10_codes_and_UKB_Smoking_Record = pd.DataFrame(row_counts_Combined_ICD10_codes_and_UKB_Smoking_Records, index=['Row Count'])
nan_counts_Combined_ICD10_codes_and_UKB_Smoking_Record = pd.DataFrame(nan_counts_Combined_ICD10_codes_and_UKB_Smoking_Records, index=['NaN Count'])
empty_counts_Combined_ICD10_codes_and_UKB_Smoking_Record = pd.DataFrame(empty_counts_Combined_ICD10_codes_and_UKB_Smoking_Records, index=['Empty Count'])
prefer_not_to_say_counts_Combined_ICD10_codes_and_UKB_Smoking_Record = pd.DataFrame(prefer_not_to_say_counts_Combined_ICD10_codes_and_UKB_Smoking_Records, index=['Prefer not to answer'])

# Concatenate the DataFrames
result_Combined_ICD10_codes_and_UKB_Smoking_Records = []
result_Combined_ICD10_codes_and_UKB_Smoking_Records = pd.concat([unique_counts_Combined_ICD10_codes_and_UKB_Smoking_Record, row_counts_Combined_ICD10_codes_and_UKB_Smoking_Record, nan_counts_Combined_ICD10_codes_and_UKB_Smoking_Record, empty_counts_Combined_ICD10_codes_and_UKB_Smoking_Record,prefer_not_to_say_counts_Combined_ICD10_codes_and_UKB_Smoking_Record])

# Display the combined DataFrame
print("Combined_ICD10_codes_and_UKB_Smoking_Records:")
display(result_Combined_ICD10_codes_and_UKB_Smoking_Records)
print()


# Total number of participants
total_participants = []
total_participants = 440014

# Drop duplicate Participant ID rows to get unique participants
unique_participants = []
unique_participants = Combined_ICD10_codes_and_UKB_Smoking_Records.drop_duplicates(subset=['Participant ID'])



# Display unique items under the column "Smoking Status"
unique_smoking_status = []
unique_smoking_status = unique_participants['Smoking Status'].unique()
# Print the unique items
display(unique_smoking_status)
print()


# Count occurrences of unique values in the 'Smoking Status' column
smoking_status_counts = []
smoking_status_counts = unique_participants['Smoking Status'].value_counts()

# Calculate the percentage for each ethnicity
smoking_status_percentages = []
smoking_status_percentages = (smoking_status_counts / total_participants) * 100

# Combine counts and percentages
smoking_status_counts_with_percentages = []
smoking_status_counts_with_percentages = smoking_status_counts.astype(str) + " (" + smoking_status_percentages.round(2).astype(str) + "%)"



# Display the counts
#print("Counts of unique values in the 'Smoking Status' column:")
#display(smoking_status_counts_with_percentages)
#print()


#Combined_ICD10_codes_and_UKB_Smoking_Records.head(3)


# <div style="background-color: #d3f5d3; padding: 10px;">
#     <h2><center>5. Importing UK Biobank Dataset (BMI Records)-for UKB</center></h2>
# </div>

# In[ ]:


All_ICD10_with_Diseases_Dates_Data = []
All_ICD10_with_Diseases_Dates_Data = pd.read_csv('Dataset with ICD10 and Diseases Names and Death Records.csv')
#All_ICD10_with_Diseases_Dates_Data.head(3)


# In[ ]:


UKB_BMI_Records = []
UKB_BMI_Records = pd.read_csv('UK_biobank_BMI_data.csv')

# Rename multiple variables
UKB_BMI_Records = UKB_BMI_Records.rename(columns={"eid": "Participant ID", 
                        "21001-0.0": "Body mass index (BMI)_Instance 0(2006-2010)",
                        "21001-1.0": "Body mass index (BMI)_Instance 1(2012-2013)",
                        "21001-2.0": "Body mass index (BMI)_Instance 2(2014+)",
                        "21001-3.0": "Body mass index (BMI)_Instance 3(2019+)"})

UKB_BMI_Records = UKB_BMI_Records.drop_duplicates()

# Create dictionaries to store unique counts, row counts, NaN counts, and empty counts
unique_counts_UKB_BMI_Records = {}
row_counts_UKB_BMI_Records = {}
nan_counts_UKB_BMI_Records = {}
empty_counts_UKB_BMI_Records = {}

# Loop through columns and count unique items, row counts, NaN counts, and empty counts
for column_UKB_BMI_Records in UKB_BMI_Records.columns:
    unique_count_UKB_BMI_Records = UKB_BMI_Records[column_UKB_BMI_Records].nunique()
    row_count_UKB_BMI_Records = len(UKB_BMI_Records[column_UKB_BMI_Records])
    nan_count_UKB_BMI_Records = UKB_BMI_Records[column_UKB_BMI_Records].isna().sum()  # Count NaN values
    empty_count_UKB_BMI_Records = UKB_BMI_Records[column_UKB_BMI_Records].eq('').sum()  # Count empty string values

    unique_counts_UKB_BMI_Records[column_UKB_BMI_Records] = [unique_count_UKB_BMI_Records]
    row_counts_UKB_BMI_Records[column_UKB_BMI_Records] = [row_count_UKB_BMI_Records]
    nan_counts_UKB_BMI_Records[column_UKB_BMI_Records] = [nan_count_UKB_BMI_Records]
    empty_counts_UKB_BMI_Records[column_UKB_BMI_Records] = [empty_count_UKB_BMI_Records]

# Create DataFrames from the dictionaries
unique_counts_UKB_BMI_Record = []
row_counts_UKB_BMI_Record = []
nan_counts_UKB_BMI_Record = []
empty_counts_UKB_BMI_Record = []

unique_counts_UKB_BMI_Record = pd.DataFrame(unique_counts_UKB_BMI_Records, index=['Unique Count'])
row_counts_UKB_BMI_Record = pd.DataFrame(row_counts_UKB_BMI_Records, index=['Row Count'])
nan_counts_UKB_BMI_Record = pd.DataFrame(nan_counts_UKB_BMI_Records, index=['NaN Count'])
empty_counts_UKB_BMI_Record = pd.DataFrame(empty_counts_UKB_BMI_Records, index=['Empty Count'])

# Concatenate the DataFrames
result_UKB_BMI_Records = []
result_UKB_BMI_Records = pd.concat([unique_counts_UKB_BMI_Record, row_counts_UKB_BMI_Record, nan_counts_UKB_BMI_Record, empty_counts_UKB_BMI_Record])

# Display the combined DataFrame
#print("UKB_BMI_Records:")
#print()
#display(result_UKB_BMI_Records)


#UKB_BMI_Records.head(3)


# **4a. I combined the all the columns named "Body mass index (BMI)_Instance"**

# In[ ]:


columns_to_check = []
columns_to_check = ['Body mass index (BMI)_Instance 0(2006-2010)',
                    'Body mass index (BMI)_Instance 1(2012-2013)',
                    'Body mass index (BMI)_Instance 2(2014+)',
                    'Body mass index (BMI)_Instance 3(2019+)']

# Create a new column 'Body mass index (BMI)' and fill it with non-NaN values from the specified columns
UKB_BMI_Records['Body mass index (BMI)'] = UKB_BMI_Records[columns_to_check].apply(lambda row: next((value for value in row if not pd.isna(value)), np.nan), axis=1)


columns_to_drop = []
columns_to_drop = ['Body mass index (BMI)_Instance 0(2006-2010)',
                    'Body mass index (BMI)_Instance 1(2012-2013)',
                    'Body mass index (BMI)_Instance 2(2014+)',
                    'Body mass index (BMI)_Instance 3(2019+)']

# Drop the specified columns
UKB_BMI_Records.drop(columns=columns_to_drop, inplace=True)



# Create dictionaries to store unique counts, row counts, NaN counts, and empty counts
unique_counts_UKB_BMI_Records = {}
row_counts_UKB_BMI_Records = {}
nan_counts_UKB_BMI_Records = {}
empty_counts_UKB_BMI_Records = {}

# Loop through columns and count unique items, row counts, NaN counts, and empty counts
for column_UKB_BMI_Records in UKB_BMI_Records.columns:
    unique_count_UKB_BMI_Records = UKB_BMI_Records[column_UKB_BMI_Records].nunique()
    row_count_UKB_BMI_Records = len(UKB_BMI_Records[column_UKB_BMI_Records])
    nan_count_UKB_BMI_Records = UKB_BMI_Records[column_UKB_BMI_Records].isna().sum()  # Count NaN values
    empty_count_UKB_BMI_Records = UKB_BMI_Records[column_UKB_BMI_Records].eq('').sum()  # Count empty string values

    unique_counts_UKB_BMI_Records[column_UKB_BMI_Records] = [unique_count_UKB_BMI_Records]
    row_counts_UKB_BMI_Records[column_UKB_BMI_Records] = [row_count_UKB_BMI_Records]
    nan_counts_UKB_BMI_Records[column_UKB_BMI_Records] = [nan_count_UKB_BMI_Records]
    empty_counts_UKB_BMI_Records[column_UKB_BMI_Records] = [empty_count_UKB_BMI_Records]

# Create DataFrames from the dictionaries
unique_counts_UKB_BMI_Record = []
row_counts_UKB_BMI_Record = []
nan_counts_UKB_BMI_Record = []
empty_counts_UKB_BMI_Record = []

unique_counts_UKB_BMI_Record = pd.DataFrame(unique_counts_UKB_BMI_Records, index=['Unique Count'])
row_counts_UKB_BMI_Record = pd.DataFrame(row_counts_UKB_BMI_Records, index=['Row Count'])
nan_counts_UKB_BMI_Record = pd.DataFrame(nan_counts_UKB_BMI_Records, index=['NaN Count'])
empty_counts_UKB_BMI_Record = pd.DataFrame(empty_counts_UKB_BMI_Records, index=['Empty Count'])

# Concatenate the DataFrames
result_UKB_BMI_Records = []
result_UKB_BMI_Records = pd.concat([unique_counts_UKB_BMI_Record, row_counts_UKB_BMI_Record, nan_counts_UKB_BMI_Record, empty_counts_UKB_BMI_Record])

# Display the combined DataFrame
#print("UKB_BMI_Records:")
#print()
#display(result_UKB_BMI_Records)


#UKB_BMI_Records.head(3)


# **4b. Remove the "NaN" or missing values from BMI column**

# In[ ]:


# Remove rows with NaN values in the "Body mass index (BMI)" column
UKB_BMI_Records = UKB_BMI_Records.dropna(subset=["Body mass index (BMI)"])

# Reset index
UKB_BMI_Records.reset_index(drop=True, inplace=True)


# Create dictionaries to store unique counts, row counts, NaN counts, and empty counts
unique_counts_UKB_BMI_Records = {}
row_counts_UKB_BMI_Records = {}
nan_counts_UKB_BMI_Records = {}
empty_counts_UKB_BMI_Records = {}

# Loop through columns and count unique items, row counts, NaN counts, and empty counts
for column_UKB_BMI_Records in UKB_BMI_Records.columns:
    unique_count_UKB_BMI_Records = UKB_BMI_Records[column_UKB_BMI_Records].nunique()
    row_count_UKB_BMI_Records = len(UKB_BMI_Records[column_UKB_BMI_Records])
    nan_count_UKB_BMI_Records = UKB_BMI_Records[column_UKB_BMI_Records].isna().sum()  # Count NaN values
    empty_count_UKB_BMI_Records = UKB_BMI_Records[column_UKB_BMI_Records].eq('').sum()  # Count empty string values

    unique_counts_UKB_BMI_Records[column_UKB_BMI_Records] = [unique_count_UKB_BMI_Records]
    row_counts_UKB_BMI_Records[column_UKB_BMI_Records] = [row_count_UKB_BMI_Records]
    nan_counts_UKB_BMI_Records[column_UKB_BMI_Records] = [nan_count_UKB_BMI_Records]
    empty_counts_UKB_BMI_Records[column_UKB_BMI_Records] = [empty_count_UKB_BMI_Records]

# Create DataFrames from the dictionaries
unique_counts_UKB_BMI_Record = []
row_counts_UKB_BMI_Record = []
nan_counts_UKB_BMI_Record = []
empty_counts_UKB_BMI_Record = []

unique_counts_UKB_BMI_Record = pd.DataFrame(unique_counts_UKB_BMI_Records, index=['Unique Count'])
row_counts_UKB_BMI_Record = pd.DataFrame(row_counts_UKB_BMI_Records, index=['Row Count'])
nan_counts_UKB_BMI_Record = pd.DataFrame(nan_counts_UKB_BMI_Records, index=['NaN Count'])
empty_counts_UKB_BMI_Record = pd.DataFrame(empty_counts_UKB_BMI_Records, index=['Empty Count'])

# Concatenate the DataFrames
result_UKB_BMI_Records = []
result_UKB_BMI_Records = pd.concat([unique_counts_UKB_BMI_Record, row_counts_UKB_BMI_Record, nan_counts_UKB_BMI_Record, empty_counts_UKB_BMI_Record])

# Display the combined DataFrame
#print("UKB_BMI_Records:")
#print()
#display(result_UKB_BMI_Records)


#UKB_BMI_Records.head(3)


# **4c. Define the BMI range**

# In[ ]:


# Define a function to map BMI values to BMI ranges
def map_bmi_range(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi <= 24.9:
        return "Healthy Weight"
    elif 25.0 <= bmi <= 29.9:
        return "Overweight"
    else:
        return "Obesity"

# Apply the function to create the 'BMI Range' column
UKB_BMI_Records['BMI Range'] = UKB_BMI_Records['Body mass index (BMI)'].apply(map_bmi_range)

# Count occurrences of each BMI range
bmi_range_counts = UKB_BMI_Records['BMI Range'].value_counts()

# Display the counts
#print("Counts for each BMI range:")
#display(bmi_range_counts)

# Display the DataFrame with the new 'BMI Range' column
#UKB_BMI_Records.head(3)


# In[ ]:


#file_path = []

## Specify the file path where you want to save the CSV file
#file_path = 'BMI Range Record Dataset.csv'

## Use the to_csv method to save the DataFrame as a CSV file
#UKB_BMI_Records.to_csv(file_path, index=False)  # Set index=False to exclude the index column


# **4e. Combine BMI Records with ICD10 Codes Structured dataset**

# In[ ]:


Combined_ICD10_codes_and_UKB_BMI_Records = []
Combined_ICD10_codes_and_UKB_BMI_Records = pd.merge(All_ICD10_with_Diseases_Dates_Data,UKB_BMI_Records,   on="Participant ID", how="left")



# Create dictionaries to store unique counts, row counts, NaN counts, and empty counts
unique_counts_Combined_ICD10_codes_and_UKB_BMI_Records = {}
row_counts_Combined_ICD10_codes_and_UKB_BMI_Records = {}
nan_counts_Combined_ICD10_codes_and_UKB_BMI_Records = {}
empty_counts_Combined_ICD10_codes_and_UKB_BMI_Records = {}
prefer_not_to_say_counts_Combined_ICD10_codes_and_UKB_BMI_Records = {}

# Loop through columns and count unique items, row counts, NaN counts, and empty counts
for column_Combined_ICD10_codes_and_UKB_BMI_Records in Combined_ICD10_codes_and_UKB_BMI_Records.columns:
    unique_count_Combined_ICD10_codes_and_UKB_BMI_Records = Combined_ICD10_codes_and_UKB_BMI_Records[column_Combined_ICD10_codes_and_UKB_BMI_Records].nunique()
    row_count_Combined_ICD10_codes_and_UKB_BMI_Records = len(Combined_ICD10_codes_and_UKB_BMI_Records[column_Combined_ICD10_codes_and_UKB_BMI_Records])
    nan_count_Combined_ICD10_codes_and_UKB_BMI_Records = Combined_ICD10_codes_and_UKB_BMI_Records[column_Combined_ICD10_codes_and_UKB_BMI_Records].isna().sum()  # Count NaN values
    empty_count_Combined_ICD10_codes_and_UKB_BMI_Records = Combined_ICD10_codes_and_UKB_BMI_Records[column_Combined_ICD10_codes_and_UKB_BMI_Records].eq('').sum()  # Count empty string values
    prefer_not_to_say_count_Combined_ICD10_codes_and_UKB_BMI_Records = Combined_ICD10_codes_and_UKB_BMI_Records[column_Combined_ICD10_codes_and_UKB_BMI_Records].eq('Prefer not to answer').sum()  

    unique_counts_Combined_ICD10_codes_and_UKB_BMI_Records[column_Combined_ICD10_codes_and_UKB_BMI_Records] = [unique_count_Combined_ICD10_codes_and_UKB_BMI_Records]
    row_counts_Combined_ICD10_codes_and_UKB_BMI_Records[column_Combined_ICD10_codes_and_UKB_BMI_Records] = [row_count_Combined_ICD10_codes_and_UKB_BMI_Records]
    nan_counts_Combined_ICD10_codes_and_UKB_BMI_Records[column_Combined_ICD10_codes_and_UKB_BMI_Records] = [nan_count_Combined_ICD10_codes_and_UKB_BMI_Records]
    empty_counts_Combined_ICD10_codes_and_UKB_BMI_Records[column_Combined_ICD10_codes_and_UKB_BMI_Records] = [empty_count_Combined_ICD10_codes_and_UKB_BMI_Records]
    prefer_not_to_say_counts_Combined_ICD10_codes_and_UKB_BMI_Records[column_Combined_ICD10_codes_and_UKB_BMI_Records] = [prefer_not_to_say_count_Combined_ICD10_codes_and_UKB_BMI_Records]




    

# Create DataFrames from the dictionaries
unique_counts_Combined_ICD10_codes_and_UKB_BMI_Record = []
row_counts_Combined_ICD10_codes_and_UKB_BMI_Record = []
nan_counts_Combined_ICD10_codes_and_UKB_BMI_Record = []
empty_counts_Combined_ICD10_codes_and_UKB_BMI_Record = []
prefer_not_to_say_counts_Combined_ICD10_codes_and_UKB_BMI_Record =[]

unique_counts_Combined_ICD10_codes_and_UKB_BMI_Record = pd.DataFrame(unique_counts_Combined_ICD10_codes_and_UKB_BMI_Records, index=['Unique Count'])
row_counts_Combined_ICD10_codes_and_UKB_BMI_Record = pd.DataFrame(row_counts_Combined_ICD10_codes_and_UKB_BMI_Records, index=['Row Count'])
nan_counts_Combined_ICD10_codes_and_UKB_BMI_Record = pd.DataFrame(nan_counts_Combined_ICD10_codes_and_UKB_BMI_Records, index=['NaN Count'])
empty_counts_Combined_ICD10_codes_and_UKB_BMI_Record = pd.DataFrame(empty_counts_Combined_ICD10_codes_and_UKB_BMI_Records, index=['Empty Count'])
prefer_not_to_say_counts_Combined_ICD10_codes_and_UKB_BMI_Record = pd.DataFrame(prefer_not_to_say_counts_Combined_ICD10_codes_and_UKB_BMI_Records, index=['Prefer not to answer'])

# Concatenate the DataFrames
result_Combined_ICD10_codes_and_UKB_BMI_Records = []
result_Combined_ICD10_codes_and_UKB_BMI_Records = pd.concat([unique_counts_Combined_ICD10_codes_and_UKB_BMI_Record, row_counts_Combined_ICD10_codes_and_UKB_BMI_Record, nan_counts_Combined_ICD10_codes_and_UKB_BMI_Record, empty_counts_Combined_ICD10_codes_and_UKB_BMI_Record,prefer_not_to_say_counts_Combined_ICD10_codes_and_UKB_BMI_Record])

# Display the combined DataFrame
print("Combined_ICD10_codes_and_UKB_BMI_Records:")
display(result_Combined_ICD10_codes_and_UKB_BMI_Records)
print()
display(Combined_ICD10_codes_and_UKB_BMI_Records.head(3))
print()


# Total number of participants
total_participants = []
total_participants = 440014

# Drop duplicate Participant ID rows to get unique participants
unique_participants = []
unique_participants = Combined_ICD10_codes_and_UKB_BMI_Records.drop_duplicates(subset=['Participant ID'])



# Display unique items under the column "BMI Range"
unique_BMI_status = []
unique_BMI_status = unique_participants['BMI Range'].unique()
# Print the unique items
display(unique_BMI_status)
print()


# Count occurrences of unique values in the 'BMI Range' column
BMI_status_counts = []
BMI_status_counts = unique_participants['BMI Range'].value_counts()

# Calculate the percentage 
BMI_status_percentages = []
BMI_status_percentages = (BMI_status_counts / total_participants) * 100

# Combine counts and percentages
BMI_status_counts_with_percentages = []
BMI_status_counts_with_percentages = BMI_status_counts.astype(str) + " (" + BMI_status_percentages.round(2).astype(str) + "%)"



# Display the counts
#print("Counts of unique values in the 'BMI Range' column:")
#display(BMI_status_counts_with_percentages)
#print()


# <div style="background-color: #d3f5d3; padding: 10px;">
#     <h2><center>5. Importing UK Biobank Dataset (IMD Records) - for UKB</center></h2>
# </div>

# In[ ]:


All_ICD10_with_Diseases_Dates_Data = []
All_ICD10_with_Diseases_Dates_Data = pd.read_csv('Dataset with ICD10 and Diseases Names and Death Records.csv')
#All_ICD10_with_Diseases_Dates_Data.head(3)


# In[ ]:


UKB_IMD_Records = []
UKB_IMD_Records = pd.read_csv('UK_biobank_IMD_data.csv')

# Rename multiple variables
UKB_IMD_Records = UKB_IMD_Records.rename(columns={"eid": "Participant ID", 
                        "26410-0.0": "Index of Multiple Deprivation (England)"})

UKB_IMD_Records = UKB_IMD_Records.drop_duplicates()


# Create dictionaries to store unique counts, row counts, NaN counts, and empty counts
unique_counts_UKB_IMD_Records = {}
row_counts_UKB_IMD_Records = {}
nan_counts_UKB_IMD_Records = {}
empty_counts_UKB_IMD_Records = {}

# Loop through columns and count unique items, row counts, NaN counts, and empty counts
for column_UKB_IMD_Records in UKB_IMD_Records.columns:
    unique_count_UKB_IMD_Records = UKB_IMD_Records[column_UKB_IMD_Records].nunique()
    row_count_UKB_IMD_Records = len(UKB_IMD_Records[column_UKB_IMD_Records])
    nan_count_UKB_IMD_Records = UKB_IMD_Records[column_UKB_IMD_Records].isna().sum()  # Count NaN values
    empty_count_UKB_IMD_Records = UKB_IMD_Records[column_UKB_IMD_Records].eq('').sum()  # Count empty string values

    unique_counts_UKB_IMD_Records[column_UKB_IMD_Records] = [unique_count_UKB_IMD_Records]
    row_counts_UKB_IMD_Records[column_UKB_IMD_Records] = [row_count_UKB_IMD_Records]
    nan_counts_UKB_IMD_Records[column_UKB_IMD_Records] = [nan_count_UKB_IMD_Records]
    empty_counts_UKB_IMD_Records[column_UKB_IMD_Records] = [empty_count_UKB_IMD_Records]

# Create DataFrames from the dictionaries
unique_counts_UKB_IMD_Record = []
row_counts_UKB_IMD_Record = []
nan_counts_UKB_IMD_Record = []
empty_counts_UKB_IMD_Record = []

unique_counts_UKB_IMD_Record = pd.DataFrame(unique_counts_UKB_IMD_Records, index=['Unique Count'])
row_counts_UKB_IMD_Record = pd.DataFrame(row_counts_UKB_IMD_Records, index=['Row Count'])
nan_counts_UKB_IMD_Record = pd.DataFrame(nan_counts_UKB_IMD_Records, index=['NaN Count'])
empty_counts_UKB_IMD_Record = pd.DataFrame(empty_counts_UKB_IMD_Records, index=['Empty Count'])

# Concatenate the DataFrames
result_UKB_IMD_Records = []
result_UKB_IMD_Records = pd.concat([unique_counts_UKB_IMD_Record, row_counts_UKB_IMD_Record, nan_counts_UKB_IMD_Record, empty_counts_UKB_IMD_Record])

# Display the combined DataFrame
#print("UKB_IMD_Records:")
#print()
#display(result_UKB_IMD_Records)



#UKB_IMD_Records.head(3)


# **5a. Remove the "NaN" or missing values from Index of Multiple Deprivation (England) column**

# In[ ]:


# Remove rows with NaN values in the "Index of Multiple Deprivation (England)" column
UKB_IMD_Records = UKB_IMD_Records.dropna(subset=["Index of Multiple Deprivation (England)"])

# Reset index
UKB_IMD_Records.reset_index(drop=True, inplace=True)


# Create dictionaries to store unique counts, row counts, NaN counts, and empty counts
unique_counts_UKB_IMD_Records = {}
row_counts_UKB_IMD_Records = {}
nan_counts_UKB_IMD_Records = {}
empty_counts_UKB_IMD_Records = {}

# Loop through columns and count unique items, row counts, NaN counts, and empty counts
for column_UKB_IMD_Records in UKB_IMD_Records.columns:
    unique_count_UKB_IMD_Records = UKB_IMD_Records[column_UKB_IMD_Records].nunique()
    row_count_UKB_IMD_Records = len(UKB_IMD_Records[column_UKB_IMD_Records])
    nan_count_UKB_IMD_Records = UKB_IMD_Records[column_UKB_IMD_Records].isna().sum()  # Count NaN values
    empty_count_UKB_IMD_Records = UKB_IMD_Records[column_UKB_IMD_Records].eq('').sum()  # Count empty string values

    unique_counts_UKB_IMD_Records[column_UKB_IMD_Records] = [unique_count_UKB_IMD_Records]
    row_counts_UKB_IMD_Records[column_UKB_IMD_Records] = [row_count_UKB_IMD_Records]
    nan_counts_UKB_IMD_Records[column_UKB_IMD_Records] = [nan_count_UKB_IMD_Records]
    empty_counts_UKB_IMD_Records[column_UKB_IMD_Records] = [empty_count_UKB_IMD_Records]

# Create DataFrames from the dictionaries
unique_counts_UKB_IMD_Record = []
row_counts_UKB_IMD_Record = []
nan_counts_UKB_IMD_Record = []
empty_counts_UKB_IMD_Record = []

unique_counts_UKB_IMD_Record = pd.DataFrame(unique_counts_UKB_IMD_Records, index=['Unique Count'])
row_counts_UKB_IMD_Record = pd.DataFrame(row_counts_UKB_IMD_Records, index=['Row Count'])
nan_counts_UKB_IMD_Record = pd.DataFrame(nan_counts_UKB_IMD_Records, index=['NaN Count'])
empty_counts_UKB_IMD_Record = pd.DataFrame(empty_counts_UKB_IMD_Records, index=['Empty Count'])

# Concatenate the DataFrames
result_UKB_IMD_Records = []
result_UKB_IMD_Records = pd.concat([unique_counts_UKB_IMD_Record, row_counts_UKB_IMD_Record, nan_counts_UKB_IMD_Record, empty_counts_UKB_IMD_Record])

# Display the combined DataFrame
#print("UKB_IMD_Records:")
#print()
#display(result_UKB_IMD_Records)
#print()


#UKB_IMD_Records.head(3)


# **5b. Maximum and minum range of the Index of Multiple Deprivation(IMD)**

# In[ ]:


# Remove rows with NaN values in the "Index of Multiple Deprivation (England)" column
UKB_IMD_Records = UKB_IMD_Records.dropna(subset=["Index of Multiple Deprivation (England)"])

# Reset index
UKB_IMD_Records.reset_index(drop=True, inplace=True)


# Create dictionaries to store unique counts, row counts, NaN counts, and empty counts
unique_counts_UKB_IMD_Records = {}
row_counts_UKB_IMD_Records = {}
nan_counts_UKB_IMD_Records = {}
empty_counts_UKB_IMD_Records = {}

# Loop through columns and count unique items, row counts, NaN counts, and empty counts
for column_UKB_IMD_Records in UKB_IMD_Records.columns:
    unique_count_UKB_IMD_Records = UKB_IMD_Records[column_UKB_IMD_Records].nunique()
    row_count_UKB_IMD_Records = len(UKB_IMD_Records[column_UKB_IMD_Records])
    nan_count_UKB_IMD_Records = UKB_IMD_Records[column_UKB_IMD_Records].isna().sum()  # Count NaN values
    empty_count_UKB_IMD_Records = UKB_IMD_Records[column_UKB_IMD_Records].eq('').sum()  # Count empty string values

    unique_counts_UKB_IMD_Records[column_UKB_IMD_Records] = [unique_count_UKB_IMD_Records]
    row_counts_UKB_IMD_Records[column_UKB_IMD_Records] = [row_count_UKB_IMD_Records]
    nan_counts_UKB_IMD_Records[column_UKB_IMD_Records] = [nan_count_UKB_IMD_Records]
    empty_counts_UKB_IMD_Records[column_UKB_IMD_Records] = [empty_count_UKB_IMD_Records]

# Create DataFrames from the dictionaries
unique_counts_UKB_IMD_Record = []
row_counts_UKB_IMD_Record = []
nan_counts_UKB_IMD_Record = []
empty_counts_UKB_IMD_Record = []

unique_counts_UKB_IMD_Record = pd.DataFrame(unique_counts_UKB_IMD_Records, index=['Unique Count'])
row_counts_UKB_IMD_Record = pd.DataFrame(row_counts_UKB_IMD_Records, index=['Row Count'])
nan_counts_UKB_IMD_Record = pd.DataFrame(nan_counts_UKB_IMD_Records, index=['NaN Count'])
empty_counts_UKB_IMD_Record = pd.DataFrame(empty_counts_UKB_IMD_Records, index=['Empty Count'])

# Concatenate the DataFrames
result_UKB_IMD_Records = []
result_UKB_IMD_Records = pd.concat([unique_counts_UKB_IMD_Record, row_counts_UKB_IMD_Record, nan_counts_UKB_IMD_Record, empty_counts_UKB_IMD_Record])

# Display the combined DataFrame
#print("UKB_IMD_Records:")
#print()
#display(result_UKB_IMD_Records)
#print()


#UKB_IMD_Records.head(3)


# **5c. Maximum and minum range of the Index of Multiple Deprivation(IMD)**

# In[ ]:


# Assuming 'UKB_IMD_Records' is the DataFrame containing the data
maximum_value = UKB_IMD_Records['Index of Multiple Deprivation (England)'].max()
minimum_value = UKB_IMD_Records['Index of Multiple Deprivation (England)'].min()

#print("Maximum value:", maximum_value)
#print("Minimum value:", minimum_value)


# **5d. Define the 5 Quartiles for IMD**
# 
# lower the IMD Score, Higher the depriviation level

# In[ ]:


def assign_imd_quintile(imd_value):
    if imd_value <= 20:
        return 1
    elif imd_value <= 40:
        return 2
    elif imd_value <= 60:
        return 3
    elif imd_value <= 80:
        return 4
    else:
        return 5

# Apply the function to create the 'IMD_quintile' column
UKB_IMD_Records['IMD_quintile'] = UKB_IMD_Records['Index of Multiple Deprivation (England)'].apply(assign_imd_quintile)

# Count occurrences of each quintile
quintile_counts = []
quintile_counts = UKB_IMD_Records['IMD_quintile'].value_counts().sort_index()

# Convert the counts to a DataFrame
quintile_counts_df = []
quintile_counts_df = pd.DataFrame({'IMD_quintile': quintile_counts.index, 'Count': quintile_counts.values})

#display(quintile_counts_df)


# Display the DataFrame with IMD quintiles assigned
#UKB_IMD_Records.head(3)


# In[ ]:


#file_path = []

## Specify the file path where you want to save the CSV file
#file_path = 'IMD Records with IMD_Quintile.csv'


## Use the to_csv method to save the DataFrame as a CSV file
#UKB_IMD_Records.to_csv(file_path, index=False)  # Set index=False to exclude the index column


# **5e. Combine IMD Records with ICD10 Codes Structured dataset**

# In[ ]:


Combined_ICD10_codes_and_UKB_IMD_Records = []
Combined_ICD10_codes_and_UKB_IMD_Records = pd.merge(All_ICD10_with_Diseases_Dates_Data,UKB_IMD_Records,   on="Participant ID", how="left")



# Create dictionaries to store unique counts, row counts, NaN counts, and empty counts
unique_counts_Combined_ICD10_codes_and_UKB_IMD_Records = {}
row_counts_Combined_ICD10_codes_and_UKB_IMD_Records = {}
nan_counts_Combined_ICD10_codes_and_UKB_IMD_Records = {}
empty_counts_Combined_ICD10_codes_and_UKB_IMD_Records = {}
prefer_not_to_say_counts_Combined_ICD10_codes_and_UKB_IMD_Records = {}

# Loop through columns and count unique items, row counts, NaN counts, and empty counts
for column_Combined_ICD10_codes_and_UKB_IMD_Records in Combined_ICD10_codes_and_UKB_IMD_Records.columns:
    unique_count_Combined_ICD10_codes_and_UKB_IMD_Records = Combined_ICD10_codes_and_UKB_IMD_Records[column_Combined_ICD10_codes_and_UKB_IMD_Records].nunique()
    row_count_Combined_ICD10_codes_and_UKB_IMD_Records = len(Combined_ICD10_codes_and_UKB_IMD_Records[column_Combined_ICD10_codes_and_UKB_IMD_Records])
    nan_count_Combined_ICD10_codes_and_UKB_IMD_Records = Combined_ICD10_codes_and_UKB_IMD_Records[column_Combined_ICD10_codes_and_UKB_IMD_Records].isna().sum()  # Count NaN values
    empty_count_Combined_ICD10_codes_and_UKB_IMD_Records = Combined_ICD10_codes_and_UKB_IMD_Records[column_Combined_ICD10_codes_and_UKB_IMD_Records].eq('').sum()  # Count empty string values
    prefer_not_to_say_count_Combined_ICD10_codes_and_UKB_IMD_Records = Combined_ICD10_codes_and_UKB_IMD_Records[column_Combined_ICD10_codes_and_UKB_IMD_Records].eq('Prefer not to answer').sum()  

    unique_counts_Combined_ICD10_codes_and_UKB_IMD_Records[column_Combined_ICD10_codes_and_UKB_IMD_Records] = [unique_count_Combined_ICD10_codes_and_UKB_IMD_Records]
    row_counts_Combined_ICD10_codes_and_UKB_IMD_Records[column_Combined_ICD10_codes_and_UKB_IMD_Records] = [row_count_Combined_ICD10_codes_and_UKB_IMD_Records]
    nan_counts_Combined_ICD10_codes_and_UKB_IMD_Records[column_Combined_ICD10_codes_and_UKB_IMD_Records] = [nan_count_Combined_ICD10_codes_and_UKB_IMD_Records]
    empty_counts_Combined_ICD10_codes_and_UKB_IMD_Records[column_Combined_ICD10_codes_and_UKB_IMD_Records] = [empty_count_Combined_ICD10_codes_and_UKB_IMD_Records]
    prefer_not_to_say_counts_Combined_ICD10_codes_and_UKB_IMD_Records[column_Combined_ICD10_codes_and_UKB_IMD_Records] = [prefer_not_to_say_count_Combined_ICD10_codes_and_UKB_IMD_Records]




    

# Create DataFrames from the dictionaries
unique_counts_Combined_ICD10_codes_and_UKB_IMD_Record = []
row_counts_Combined_ICD10_codes_and_UKB_IMD_Record = []
nan_counts_Combined_ICD10_codes_and_UKB_IMD_Record = []
empty_counts_Combined_ICD10_codes_and_UKB_IMD_Record = []
prefer_not_to_say_counts_Combined_ICD10_codes_and_UKB_IMD_Record =[]

unique_counts_Combined_ICD10_codes_and_UKB_IMD_Record = pd.DataFrame(unique_counts_Combined_ICD10_codes_and_UKB_IMD_Records, index=['Unique Count'])
row_counts_Combined_ICD10_codes_and_UKB_IMD_Record = pd.DataFrame(row_counts_Combined_ICD10_codes_and_UKB_IMD_Records, index=['Row Count'])
nan_counts_Combined_ICD10_codes_and_UKB_IMD_Record = pd.DataFrame(nan_counts_Combined_ICD10_codes_and_UKB_IMD_Records, index=['NaN Count'])
empty_counts_Combined_ICD10_codes_and_UKB_IMD_Record = pd.DataFrame(empty_counts_Combined_ICD10_codes_and_UKB_IMD_Records, index=['Empty Count'])
prefer_not_to_say_counts_Combined_ICD10_codes_and_UKB_IMD_Record = pd.DataFrame(prefer_not_to_say_counts_Combined_ICD10_codes_and_UKB_IMD_Records, index=['Prefer not to answer'])

# Concatenate the DataFrames
result_Combined_ICD10_codes_and_UKB_IMD_Records = []
result_Combined_ICD10_codes_and_UKB_IMD_Records = pd.concat([unique_counts_Combined_ICD10_codes_and_UKB_IMD_Record, row_counts_Combined_ICD10_codes_and_UKB_IMD_Record, nan_counts_Combined_ICD10_codes_and_UKB_IMD_Record, empty_counts_Combined_ICD10_codes_and_UKB_IMD_Record,prefer_not_to_say_counts_Combined_ICD10_codes_and_UKB_IMD_Record])

# Display the combined DataFrame
#print("Combined_ICD10_codes_and_UKB_IMD_Records:")
#display(result_Combined_ICD10_codes_and_UKB_IMD_Records)
print()
#display(Combined_ICD10_codes_and_UKB_IMD_Records.head(3))
print()


# Total number of participants
total_participants = []
total_participants = 440014

# Drop duplicate Participant ID rows to get unique participants
unique_participants = []
unique_participants = Combined_ICD10_codes_and_UKB_IMD_Records.drop_duplicates(subset=['Participant ID'])



# Display unique items under the column "IMD_quintile"
unique_IMD_status = []
unique_IMD_status = unique_participants['IMD_quintile'].unique()
# Print the unique items
#display(unique_IMD_status)
#print()


# Count occurrences of unique values in the 'IMD_quintile' column
IMD_status_counts = []
IMD_status_counts = unique_participants['IMD_quintile'].value_counts()

# Calculate the percentage 
IMD_status_percentages = []
IMD_status_percentages = (IMD_status_counts / total_participants) * 100

# Combine counts and percentages
IMD_status_counts_with_percentages = []
IMD_status_counts_with_percentages = IMD_status_counts.astype(str) + " (" + IMD_status_percentages.round(2).astype(str) + "%)"



# Display the counts
#print("Counts of unique values in the 'IMD_quintile' column:")
#display(IMD_status_counts_with_percentages)
#print()


# <div style="background-color: #d3f5d3; padding: 10px;">
#     <h2><center>7. Death/ ALive Records according to Age Groups (for UKB)</center></h2>
# </div>

# In[ ]:


All_ICD10_with_Diseases_Dates_Data = []
All_ICD10_with_Diseases_Dates_Data = pd.read_csv('Dataset with ICD10 and Diseases Names and Death Records.csv')
#All_ICD10_with_Diseases_Dates_Data.head(3)


# In[ ]:


# Total number of participants
total_participants = []
total_participants = 440014


# Drop duplicate Participant ID rows to get unique participants
unique_participants = []
unique_participants = All_ICD10_with_Diseases_Dates_Data.drop_duplicates(subset=['Participant ID'])

# Count occurrences of unique values in the 'Alive / Dead' column
total_alive_dead_counts = []
total_alive_dead_counts = unique_participants['Alive / Dead'].value_counts()

# Calculate the percentage 
total_alive_dead_percentages = []
total_alive_dead_percentages = (total_alive_dead_counts / total_participants) * 100

# Combine counts and percentages
total_alive_dead_counts_with_percentages = []
total_alive_dead_counts_with_percentages = total_alive_dead_counts.astype(str) + " (" + total_alive_dead_percentages.round(2).astype(str) + "%)"



# Display the counts
#print("Counts of unique values in the 'Alive / Dead' column:")
#display(total_alive_dead_counts_with_percentages)
#print()
#print()

# Assume the DataFrame is already loaded as All_ICD10_with_Diseases_Dates_Data

# Define the age ranges
bins = [30, 40, 50, 60, 70, 80, 90, 100]
labels = ["30 - 40", "41 - 50", "51 - 60", "61 - 70", "71 - 80", "81 - 90", "91 - 100"]

# Create a new column 'Age Range' with the defined bins
All_ICD10_with_Diseases_Dates_Data['Age Range'] = pd.cut(All_ICD10_with_Diseases_Dates_Data['Individual Age'], bins=bins, labels=labels, right=False)

# Total number of participants
total_participants = []
total_participants = 440014


# Drop duplicate Participant ID rows to get unique participants
unique_participants = []
unique_participants = All_ICD10_with_Diseases_Dates_Data.drop_duplicates(subset=['Participant ID'])

# Separate the counts for 'Alive' and 'Dead' within each age range
alive_counts = []
dead_counts = []
alive_counts = unique_participants[unique_participants['Alive / Dead'] == 'Alive']['Age Range'].value_counts().sort_index()
dead_counts = unique_participants[unique_participants['Alive / Dead'] == 'Dead']['Age Range'].value_counts().sort_index()

# Calculate the percentages
alive_percentages = []
dead_percentages = []
alive_percentages = (alive_counts / total_participants) * 100
dead_percentages = (dead_counts / total_participants) * 100

# Combine counts and percentages for 'Alive'
alive_counts_with_percentages = alive_counts.astype(str) + " (" + alive_percentages.round(2).astype(str) + "%)"

# Combine counts and percentages for 'Dead'
dead_counts_with_percentages = []
dead_counts_with_percentages = dead_counts.astype(str) + " (" + dead_percentages.round(2).astype(str) + "%)"

# Display the counts and percentages for 'Alive'
#print("Counts and percentages for 'Alive' in each age range:")
#display(alive_counts_with_percentages)
#print()
#print()

# Display the counts and percentages for 'Dead'
#print("Counts and percentages for 'Dead' in each age range:")
#display(dead_counts_with_percentages)
#print()


# <div style="background-color: #d3f5f5; padding: 10px;">
#     <h2><center>Extract PH Patients Data with ICD10 Codes (I27.0, I27.2, I27.9) (for UKB)</center></h2>
# </div>

# In[ ]:


import pandas as pd
Dataset_with_ICD10_and_Diseases_Names_and_Death_Records = []
Dataset_with_ICD10_and_Diseases_Names_and_Death_Records = pd.read_csv('Dataset with ICD10 and Diseases Names and Death Records.csv')
#Dataset_with_ICD10_and_Diseases_Names_and_Death_Records.head(3)


# **Extract rows where the "Combined ICD10 Codes" column has one of the specified values ('I27.0','I27.2','I27.9')**

# In[ ]:


# List of values to filter
Identify_PH_Patients_using_ICD10_codes = []
Identify_PH_Patients_using_ICD10_codes = ['I27.0','I27.2','I27.9']

# Extract rows where the "Item" column has one of the specified values
PH_Patients_using_ICD10_codes_Dataset = []

PH_Patients_using_ICD10_codes_Dataset = Dataset_with_ICD10_and_Diseases_Names_and_Death_Records[(Dataset_with_ICD10_and_Diseases_Names_and_Death_Records['Combined ICD10 Codes'].isin(Identify_PH_Patients_using_ICD10_codes))]# | (Complete_dataset['Drug Name'].notna())]
#PH_Patients_using_ICD10_codes_Dataset.head(3)


# **Replace 'Combined ICD10 Codes' with the actual column name (PH Group)**

# In[ ]:


column_name = [] 
column_name = 'Combined ICD10 Codes'

icd10_to_ph_group = []
icd10_to_ph_group = {'I27.0': 'Primary PH','I27.2': 'Other Secondary PH','I27.9': 'Secondary PH'}
# Create the 'PH Group' column based on the mapping
PH_Patients_using_ICD10_codes_Dataset['PH Group'] = PH_Patients_using_ICD10_codes_Dataset[column_name].map(icd10_to_ph_group)
#PH_Patients_using_ICD10_codes_Dataset.head(3)


# **create the columns for of PH Patients (I27.0 = Primary PH, I27.2 = Other Secondary PH, I27.9 = Secondary PH) in the dataset**

# In[ ]:


# Create new columns
PH_Patients_using_ICD10_codes_Dataset
PH_Patients_using_ICD10_codes_Dataset['Primary PH'] = np.nan
PH_Patients_using_ICD10_codes_Dataset['Other Secondary PH'] = np.nan
PH_Patients_using_ICD10_codes_Dataset['Secondary PH'] = np.nan

# Update the new columns based on the values in the 'Combined ICD10 Codes' column
PH_Patients_using_ICD10_codes_Dataset.loc[PH_Patients_using_ICD10_codes_Dataset['Combined ICD10 Codes'] == 'I27.0', 'Primary PH'] = 'I27.0'
PH_Patients_using_ICD10_codes_Dataset.loc[PH_Patients_using_ICD10_codes_Dataset['Combined ICD10 Codes'] == 'I27.2', 'Other Secondary PH'] = 'I27.2'
PH_Patients_using_ICD10_codes_Dataset.loc[PH_Patients_using_ICD10_codes_Dataset['Combined ICD10 Codes'] == 'I27.9', 'Secondary PH'] = 'I27.9'
#PH_Patients_using_ICD10_codes_Dataset.head(3)


# **Stored the cleaned and structured records of PH pateints and also display the records summary**
# 

# In[ ]:


#### Specify the file path where you want to save the CSV file
#file_path = []
#file_path = 'PH Pateints Data May 2024.csv'

#### Use the to_csv method to save the DataFrame as a CSV file
#PH_Patients_using_ICD10_codes_Dataset.to_csv(file_path, index=False)  # Set index=False to exclude the index column


PH_Patients_using_ICD10_codes_Dataset = []
PH_Patients_using_ICD10_codes_Dataset = pd.read_csv('PH Pateints Data May 2024.csv')


# Create dictionaries to store unique counts, row counts, NaN counts, and empty counts
unique_counts_PH_Patients_using_ICD10_codes_Dataset = {}
row_counts_PH_Patients_using_ICD10_codes_Dataset = {}
nan_counts_PH_Patients_using_ICD10_codes_Dataset = {}
empty_counts_PH_Patients_using_ICD10_codes_Dataset = {}

# Loop through columns and count unique items, row counts, NaN counts, and empty counts
for column_PH_Patients_using_ICD10_codes_Dataset in PH_Patients_using_ICD10_codes_Dataset.columns:
    unique_count_PH_Patients_using_ICD10_codes_Dataset = PH_Patients_using_ICD10_codes_Dataset[column_PH_Patients_using_ICD10_codes_Dataset].nunique()
    row_count_PH_Patients_using_ICD10_codes_Dataset = len(PH_Patients_using_ICD10_codes_Dataset[column_PH_Patients_using_ICD10_codes_Dataset])
    nan_count_PH_Patients_using_ICD10_codes_Dataset = PH_Patients_using_ICD10_codes_Dataset[column_PH_Patients_using_ICD10_codes_Dataset].isna().sum()  # Count NaN values
    empty_count_PH_Patients_using_ICD10_codes_Dataset = PH_Patients_using_ICD10_codes_Dataset[column_PH_Patients_using_ICD10_codes_Dataset].eq('').sum()  # Count empty string values

    unique_counts_PH_Patients_using_ICD10_codes_Dataset[column_PH_Patients_using_ICD10_codes_Dataset] = [unique_count_PH_Patients_using_ICD10_codes_Dataset]
    row_counts_PH_Patients_using_ICD10_codes_Dataset[column_PH_Patients_using_ICD10_codes_Dataset] = [row_count_PH_Patients_using_ICD10_codes_Dataset]
    nan_counts_PH_Patients_using_ICD10_codes_Dataset[column_PH_Patients_using_ICD10_codes_Dataset] = [nan_count_PH_Patients_using_ICD10_codes_Dataset]
    empty_counts_PH_Patients_using_ICD10_codes_Dataset[column_PH_Patients_using_ICD10_codes_Dataset] = [empty_count_PH_Patients_using_ICD10_codes_Dataset]

# Create DataFrames from the dictionaries
unique_counts_PH_Patients_using_ICD10_codes_Datasets = []
row_counts_PH_Patients_using_ICD10_codes_Datasets = []
nan_counts_PH_Patients_using_ICD10_codes_Datasets = []
empty_counts_PH_Patients_using_ICD10_codes_Datasets = []

unique_counts_PH_Patients_using_ICD10_codes_Datasets = pd.DataFrame(unique_counts_PH_Patients_using_ICD10_codes_Dataset, index=['Unique Count'])
row_counts_PH_Patients_using_ICD10_codes_Datasets = pd.DataFrame(row_counts_PH_Patients_using_ICD10_codes_Dataset, index=['Row Count'])
nan_counts_PH_Patients_using_ICD10_codes_Datasets = pd.DataFrame(nan_counts_PH_Patients_using_ICD10_codes_Dataset, index=['NaN Count'])
empty_counts_PH_Patients_using_ICD10_codes_Datasets = pd.DataFrame(empty_counts_PH_Patients_using_ICD10_codes_Dataset, index=['Empty Count'])

# Concatenate the DataFrames
result_PH_Patients_using_ICD10_codes_Dataset = []
result_PH_Patients_using_ICD10_codes_Dataset = pd.concat([unique_counts_PH_Patients_using_ICD10_codes_Datasets, row_counts_PH_Patients_using_ICD10_codes_Datasets, nan_counts_PH_Patients_using_ICD10_codes_Datasets, empty_counts_PH_Patients_using_ICD10_codes_Datasets])

# Display the combined DataFrame
#print("PH Patients using ICD10 codes & Drugs Names:")
#print()
#display(result_PH_Patients_using_ICD10_codes_Dataset)
#print()
#print()
#PH_Patients_using_ICD10_codes_Dataset.head(3)


# <div style="background-color: #d3f5f5; padding: 10px;">
#     <h2><center>Sex and Ethnicity Counts for PH Patients </center></h2>
# </div>

# In[ ]:


import pandas as pd
PH_Patients_Records = []
PH_Patients_Records = pd.read_csv('PH Pateints Data May 2024.csv')

# Drop the 'Individual Age' and 'Age Range' columns
PH_Patients_Records.drop(columns=['Individual Age', 'Age Range'], inplace=True)

# Convert 'Combined ICD10 Diagnosis Date' to datetime
PH_Patients_Records['Combined ICD10 Diagnosis Date'] = pd.to_datetime(PH_Patients_Records['Combined ICD10 Diagnosis Date'], errors='coerce')

# Compute the new 'Individual Age' based on the 'Year of Birth' and 'Combined ICD10 Diagnosis Date'
PH_Patients_Records['PH Individual Age'] = PH_Patients_Records.apply(
    lambda row: row['Combined ICD10 Diagnosis Date'].year - int(row['Year of Birth']) if pd.notnull(row['Combined ICD10 Diagnosis Date']) else np.nan,
    axis=1
)

# Function to calculate age range
def calculate_age_range(age):
    if pd.isnull(age):
        return ""
    if age < 20:
        return "0 - 19"
    elif age < 30:
        return "20 - 29"
    elif age < 40:
        return "30 - 40"
    elif age < 50:
        return "41 - 50"
    elif age < 60:
        return "51 - 60"
    elif age < 70:
        return "61 - 70"
    elif age < 80:
        return "71 - 80"
    elif age < 90:
        return "81 - 90"
    else:
        return "91+"

# Calculate the 'PH Age Range' based on the new 'PH Individual Age'
PH_Patients_Records['PH Age Range'] = PH_Patients_Records['PH Individual Age'].apply(calculate_age_range)

#PH_Patients_Records.head(3)


# In[ ]:


# Total number of participants
total_participants = []
total_participants = 2727



# Drop duplicate Participant ID rows to get unique participants
unique_participants = []
unique_participants = PH_Patients_Records.drop_duplicates(subset=['Participant ID'])



# Count the number of each sex
sex_counts = []
sex_counts = unique_participants['Sex'].value_counts()

# Calculate the percentage for each ethnicity
sex_percentages = []
sex_percentages = (sex_counts / total_participants) * 100

# Combine counts and percentages
sex_counts_with_percentages = []
sex_counts_with_percentages = sex_counts.astype(str) + " (" + sex_percentages.round(2).astype(str) + "%)"



# Count the number of missing (NaN) values in each column
missing_counts = []
missing_counts = unique_participants.isna().sum()

# Get unique items in the "Ethnicity" column
unique_ethnicities = []
unique_ethnicities = unique_participants['Ethnicity'].unique()

# Count the number of each unique ethnicity
ethnicity_counts = []
ethnicity_counts = unique_participants['Ethnicity'].value_counts()



# Calculate the percentage for each ethnicity
ethnicity_percentages = []
ethnicity_percentages = (ethnicity_counts / total_participants) * 100

# Combine counts and percentages
ethnicity_counts_with_percentages = []
ethnicity_counts_with_percentages = ethnicity_counts.astype(str) + " (" + ethnicity_percentages.round(2).astype(str) + "%)"


# Print the counts
#print("Sex Counts with Percentages:")
#print(sex_counts_with_percentages)
#print()
#print("\nEthnicity Counts with Percentages:")
#print(ethnicity_counts_with_percentages)
#print()
#print("\nMissing Values Counts:")
#print(missing_counts)


# <div style="background-color: #d3f5f5; padding: 10px;">
#     <h2><center>Age Groups Counts for PH Patients </center></h2>
# </div>

# In[ ]:


#PH_Patients_Records.head(3)


# In[ ]:


# Total number of participants
total_participants = []
total_participants = 2727

# Drop duplicate Participant ID rows to get unique participants
unique_participants = []
unique_participants = PH_Patients_Records.drop_duplicates(subset=['Participant ID'])


# Count occurrences of each age range
age_range_counts = []
age_range_counts = unique_participants['PH Age Range'].value_counts().sort_index()

# Calculate percentages
age_range_percentages = (age_range_counts / total_participants) * 100

# Display the results
for age_range, count in age_range_counts.items():
    percentage = age_range_percentages[age_range]
    print(f"{age_range} : {count} ({percentage:.2f} %)")


# <div style="background-color: #d3f5f5; padding: 10px;">
#     <h2><center>IMD Counts for PH Patients </center></h2>
# </div>

# In[ ]:


#PH_Patients_Records.head(3)


# In[ ]:


IMD_Records_with_IMD_Quintile = []
IMD_Records_with_IMD_Quintile = pd.read_csv('IMD Records with IMD_Quintile.csv')
#IMD_Records_with_IMD_Quintile.head(3)


# **Combine The "IMD Records with Quintiles" with "PH patients Records dataset"**

# In[ ]:


PH_Patients_Records_and_IMD_Records_with_IMD_Quintile = []
PH_Patients_Records_and_IMD_Records_with_IMD_Quintile = pd.merge(PH_Patients_Records,IMD_Records_with_IMD_Quintile,   on="Participant ID", how="left")



# Create dictionaries to store unique counts, row counts, NaN counts, and empty counts
unique_counts_PH_Patients_Records_and_IMD_Records_with_IMD_Quintile = {}
row_counts_PH_Patients_Records_and_IMD_Records_with_IMD_Quintile = {}
nan_counts_PH_Patients_Records_and_IMD_Records_with_IMD_Quintile = {}
empty_counts_PH_Patients_Records_and_IMD_Records_with_IMD_Quintile = {}
prefer_not_to_say_counts_PH_Patients_Records_and_IMD_Records_with_IMD_Quintile = {}

# Loop through columns and count unique items, row counts, NaN counts, and empty counts
for column_PH_Patients_Records_and_IMD_Records_with_IMD_Quintile in PH_Patients_Records_and_IMD_Records_with_IMD_Quintile.columns:
    unique_count_PH_Patients_Records_and_IMD_Records_with_IMD_Quintile = PH_Patients_Records_and_IMD_Records_with_IMD_Quintile[column_PH_Patients_Records_and_IMD_Records_with_IMD_Quintile].nunique()
    row_count_PH_Patients_Records_and_IMD_Records_with_IMD_Quintile = len(PH_Patients_Records_and_IMD_Records_with_IMD_Quintile[column_PH_Patients_Records_and_IMD_Records_with_IMD_Quintile])
    nan_count_PH_Patients_Records_and_IMD_Records_with_IMD_Quintile = PH_Patients_Records_and_IMD_Records_with_IMD_Quintile[column_PH_Patients_Records_and_IMD_Records_with_IMD_Quintile].isna().sum()  # Count NaN values
    empty_count_PH_Patients_Records_and_IMD_Records_with_IMD_Quintile = PH_Patients_Records_and_IMD_Records_with_IMD_Quintile[column_PH_Patients_Records_and_IMD_Records_with_IMD_Quintile].eq('').sum()  # Count empty string values
    prefer_not_to_say_count_PH_Patients_Records_and_IMD_Records_with_IMD_Quintile = PH_Patients_Records_and_IMD_Records_with_IMD_Quintile[column_PH_Patients_Records_and_IMD_Records_with_IMD_Quintile].eq('Prefer not to answer').sum()  

    unique_counts_PH_Patients_Records_and_IMD_Records_with_IMD_Quintile[column_PH_Patients_Records_and_IMD_Records_with_IMD_Quintile] = [unique_count_PH_Patients_Records_and_IMD_Records_with_IMD_Quintile]
    row_counts_PH_Patients_Records_and_IMD_Records_with_IMD_Quintile[column_PH_Patients_Records_and_IMD_Records_with_IMD_Quintile] = [row_count_PH_Patients_Records_and_IMD_Records_with_IMD_Quintile]
    nan_counts_PH_Patients_Records_and_IMD_Records_with_IMD_Quintile[column_PH_Patients_Records_and_IMD_Records_with_IMD_Quintile] = [nan_count_PH_Patients_Records_and_IMD_Records_with_IMD_Quintile]
    empty_counts_PH_Patients_Records_and_IMD_Records_with_IMD_Quintile[column_PH_Patients_Records_and_IMD_Records_with_IMD_Quintile] = [empty_count_PH_Patients_Records_and_IMD_Records_with_IMD_Quintile]
    prefer_not_to_say_counts_PH_Patients_Records_and_IMD_Records_with_IMD_Quintile[column_PH_Patients_Records_and_IMD_Records_with_IMD_Quintile] = [prefer_not_to_say_count_PH_Patients_Records_and_IMD_Records_with_IMD_Quintile]




    

# Create DataFrames from the dictionaries
unique_counts_PH_Patients_Records_and_IMD_Records_with_IMD_Quintiles = []
row_counts_PH_Patients_Records_and_IMD_Records_with_IMD_Quintiles = []
nan_counts_PH_Patients_Records_and_IMD_Records_with_IMD_Quintiles = []
empty_counts_PH_Patients_Records_and_IMD_Records_with_IMD_Quintiles = []
prefer_not_to_say_counts_PH_Patients_Records_and_IMD_Records_with_IMD_Quintiles =[]

unique_counts_PH_Patients_Records_and_IMD_Records_with_IMD_Quintiles = pd.DataFrame(unique_counts_PH_Patients_Records_and_IMD_Records_with_IMD_Quintile, index=['Unique Count'])
row_counts_PH_Patients_Records_and_IMD_Records_with_IMD_Quintiles = pd.DataFrame(row_counts_PH_Patients_Records_and_IMD_Records_with_IMD_Quintile, index=['Row Count'])
nan_counts_PH_Patients_Records_and_IMD_Records_with_IMD_Quintiles = pd.DataFrame(nan_counts_PH_Patients_Records_and_IMD_Records_with_IMD_Quintile, index=['NaN Count'])
empty_counts_PH_Patients_Records_and_IMD_Records_with_IMD_Quintiles = pd.DataFrame(empty_counts_PH_Patients_Records_and_IMD_Records_with_IMD_Quintile, index=['Empty Count'])
prefer_not_to_say_counts_PH_Patients_Records_and_IMD_Records_with_IMD_Quintiles = pd.DataFrame(prefer_not_to_say_counts_PH_Patients_Records_and_IMD_Records_with_IMD_Quintile, index=['Prefer not to answer'])

# Concatenate the DataFrames
result_PH_Patients_Records_and_IMD_Records_with_IMD_Quintile = []
result_PH_Patients_Records_and_IMD_Records_with_IMD_Quintile = pd.concat([unique_counts_PH_Patients_Records_and_IMD_Records_with_IMD_Quintiles, row_counts_PH_Patients_Records_and_IMD_Records_with_IMD_Quintiles, nan_counts_PH_Patients_Records_and_IMD_Records_with_IMD_Quintiles, empty_counts_PH_Patients_Records_and_IMD_Records_with_IMD_Quintiles,prefer_not_to_say_counts_PH_Patients_Records_and_IMD_Records_with_IMD_Quintiles])

# Display the combined DataFrame
#print("PH_Patients_Records_and_IMD_Records_with_IMD_Quintile:")
#display(result_PH_Patients_Records_and_IMD_Records_with_IMD_Quintile)
print()
#print()
#display(PH_Patients_Records_and_IMD_Records_with_IMD_Quintile.head(3))
#print()
#print()


# Total number of participants
total_participants = []
total_participants = 2727

# Drop duplicate Participant ID rows to get unique participants
unique_participants = []
unique_participants = PH_Patients_Records_and_IMD_Records_with_IMD_Quintile.drop_duplicates(subset=['Participant ID'])



# Display unique items under the column "IMD_quintile"
unique_IMD_status = []
unique_IMD_status = unique_participants['IMD_quintile'].unique()
# Print the unique items
#display(unique_IMD_status)
#print()
#print()


# Count occurrences of unique values in the 'IMD_quintile' column
IMD_status_counts = []
IMD_status_counts = unique_participants['IMD_quintile'].value_counts()

# Calculate the percentage 
IMD_status_percentages = []
IMD_status_percentages = (IMD_status_counts / total_participants) * 100

# Combine counts and percentages
IMD_status_counts_with_percentages = []
IMD_status_counts_with_percentages = IMD_status_counts.astype(str) + " (" + IMD_status_percentages.round(2).astype(str) + "%)"



# Display the counts
#print("Counts of unique values in the 'IMD_quintile' column:")
#display(IMD_status_counts_with_percentages)
#print()


# <div style="background-color: #d3f5f5; padding: 10px;">
#     <h2><center>Smoking Status Counts for PH Patients </center></h2>
# </div>

# In[ ]:


#PH_Patients_Records.head(3)


# In[ ]:


Smoking_Status_Records = []
Smoking_Status_Records = pd.read_csv('Smoking Status Record Dataset.csv')
#Smoking_Status_Records.head(3)


# **Combine "Smoking Status Records" with PH Patients records**

# In[ ]:


PH_Patients_Records_and_Smoking_Status_Records = []
PH_Patients_Records_and_Smoking_Status_Records = pd.merge(PH_Patients_Records,Smoking_Status_Records,   on="Participant ID", how="left")



# Create dictionaries to store unique counts, row counts, NaN counts, and empty counts
unique_counts_PH_Patients_Records_and_Smoking_Status_Records = {}
row_counts_PH_Patients_Records_and_Smoking_Status_Records = {}
nan_counts_PH_Patients_Records_and_Smoking_Status_Records = {}
empty_counts_PH_Patients_Records_and_Smoking_Status_Records = {}
prefer_not_to_say_counts_PH_Patients_Records_and_Smoking_Status_Records = {}

# Loop through columns and count unique items, row counts, NaN counts, and empty counts
for column_PH_Patients_Records_and_Smoking_Status_Records in PH_Patients_Records_and_Smoking_Status_Records.columns:
    unique_count_PH_Patients_Records_and_Smoking_Status_Records = PH_Patients_Records_and_Smoking_Status_Records[column_PH_Patients_Records_and_Smoking_Status_Records].nunique()
    row_count_PH_Patients_Records_and_Smoking_Status_Records = len(PH_Patients_Records_and_Smoking_Status_Records[column_PH_Patients_Records_and_Smoking_Status_Records])
    nan_count_PH_Patients_Records_and_Smoking_Status_Records = PH_Patients_Records_and_Smoking_Status_Records[column_PH_Patients_Records_and_Smoking_Status_Records].isna().sum()  # Count NaN values
    empty_count_PH_Patients_Records_and_Smoking_Status_Records = PH_Patients_Records_and_Smoking_Status_Records[column_PH_Patients_Records_and_Smoking_Status_Records].eq('').sum()  # Count empty string values
    prefer_not_to_say_count_PH_Patients_Records_and_Smoking_Status_Records = PH_Patients_Records_and_Smoking_Status_Records[column_PH_Patients_Records_and_Smoking_Status_Records].eq('Prefer not to answer').sum()  

    unique_counts_PH_Patients_Records_and_Smoking_Status_Records[column_PH_Patients_Records_and_Smoking_Status_Records] = [unique_count_PH_Patients_Records_and_Smoking_Status_Records]
    row_counts_PH_Patients_Records_and_Smoking_Status_Records[column_PH_Patients_Records_and_Smoking_Status_Records] = [row_count_PH_Patients_Records_and_Smoking_Status_Records]
    nan_counts_PH_Patients_Records_and_Smoking_Status_Records[column_PH_Patients_Records_and_Smoking_Status_Records] = [nan_count_PH_Patients_Records_and_Smoking_Status_Records]
    empty_counts_PH_Patients_Records_and_Smoking_Status_Records[column_PH_Patients_Records_and_Smoking_Status_Records] = [empty_count_PH_Patients_Records_and_Smoking_Status_Records]
    prefer_not_to_say_counts_PH_Patients_Records_and_Smoking_Status_Records[column_PH_Patients_Records_and_Smoking_Status_Records] = [prefer_not_to_say_count_PH_Patients_Records_and_Smoking_Status_Records]




    

# Create DataFrames from the dictionaries
unique_counts_PH_Patients_Records_and_Smoking_Status_Record = []
row_counts_PH_Patients_Records_and_Smoking_Status_Record = []
nan_counts_PH_Patients_Records_and_Smoking_Status_Record = []
empty_counts_PH_Patients_Records_and_Smoking_Status_Record = []
PH_Patients_Records_and_Smoking_Status_Record =[]

unique_counts_PH_Patients_Records_and_Smoking_Status_Record = pd.DataFrame(unique_counts_PH_Patients_Records_and_Smoking_Status_Records, index=['Unique Count'])
row_counts_PH_Patients_Records_and_Smoking_Status_Record = pd.DataFrame(row_counts_PH_Patients_Records_and_Smoking_Status_Records, index=['Row Count'])
nan_counts_PH_Patients_Records_and_Smoking_Status_Record = pd.DataFrame(nan_counts_PH_Patients_Records_and_Smoking_Status_Records, index=['NaN Count'])
empty_counts_PH_Patients_Records_and_Smoking_Status_Record = pd.DataFrame(empty_counts_PH_Patients_Records_and_Smoking_Status_Records, index=['Empty Count'])
prefer_not_to_say_counts_PH_Patients_Records_and_Smoking_Status_Record = pd.DataFrame(prefer_not_to_say_counts_PH_Patients_Records_and_Smoking_Status_Records, index=['Prefer not to answer'])

# Concatenate the DataFrames
result_PH_Patients_Records_and_Smoking_Status_Records = []
result_PH_Patients_Records_and_Smoking_Status_Records = pd.concat([unique_counts_PH_Patients_Records_and_Smoking_Status_Record, row_counts_PH_Patients_Records_and_Smoking_Status_Record, nan_counts_PH_Patients_Records_and_Smoking_Status_Record, empty_counts_PH_Patients_Records_and_Smoking_Status_Record,prefer_not_to_say_counts_PH_Patients_Records_and_Smoking_Status_Record])

# Display the combined DataFrame
#print("PH_Patients_Records_and_Smoking_Status_Records:")
#display(result_PH_Patients_Records_and_Smoking_Status_Records)
#print()
#print()


# Total number of participants
total_participants = []
total_participants = 2727

# Drop duplicate Participant ID rows to get unique participants
unique_participants = []
unique_participants = PH_Patients_Records_and_Smoking_Status_Records.drop_duplicates(subset=['Participant ID'])



# Display unique items under the column "Smoking Status"
unique_smoking_status = []
unique_smoking_status = unique_participants['Smoking Status'].unique()
# Print the unique items
#display(unique_smoking_status)
#print()
#print()


# Count occurrences of unique values in the 'Smoking Status' column
smoking_status_counts = []
smoking_status_counts = unique_participants['Smoking Status'].value_counts()

# Calculate the percentage for each ethnicity
smoking_status_percentages = []
smoking_status_percentages = (smoking_status_counts / total_participants) * 100

# Combine counts and percentages
smoking_status_counts_with_percentages = []
smoking_status_counts_with_percentages = smoking_status_counts.astype(str) + " (" + smoking_status_percentages.round(2).astype(str) + "%)"



# Display the counts
#print("Counts of unique values in the 'Smoking Status' column:")
#display(smoking_status_counts_with_percentages)
#print()


#PH_Patients_Records_and_Smoking_Status_Records.head(3)


# <div style="background-color: #d3f5f5; padding: 10px;">
#     <h2><center>Body Mass Index (BMI) Counts for PH Patients </center></h2>
# </div>

# In[ ]:


#PH_Patients_Records.head(3)


# In[ ]:


BMI_Range_Record_Dataset = []
BMI_Range_Record_Dataset = pd.read_csv('BMI Range Record Dataset.csv')
#BMI_Range_Record_Dataset.head(3)


# In[ ]:


PH_Patients_Records_and_BMI_Range_Record_Dataset = []
PH_Patients_Records_and_BMI_Range_Record_Dataset = pd.merge(PH_Patients_Records,BMI_Range_Record_Dataset,   on="Participant ID", how="left")



# Create dictionaries to store unique counts, row counts, NaN counts, and empty counts
unique_counts_PH_Patients_Records_and_BMI_Range_Record_Dataset = {}
row_counts_PH_Patients_Records_and_BMI_Range_Record_Dataset = {}
nan_counts_PH_Patients_Records_and_BMI_Range_Record_Dataset = {}
empty_counts_PH_Patients_Records_and_BMI_Range_Record_Dataset = {}
prefer_not_to_say_counts_PH_Patients_Records_and_BMI_Range_Record_Dataset = {}

# Loop through columns and count unique items, row counts, NaN counts, and empty counts
for column_PH_Patients_Records_and_BMI_Range_Record_Dataset in PH_Patients_Records_and_BMI_Range_Record_Dataset.columns:
    unique_count_PH_Patients_Records_and_BMI_Range_Record_Dataset = PH_Patients_Records_and_BMI_Range_Record_Dataset[column_PH_Patients_Records_and_BMI_Range_Record_Dataset].nunique()
    row_count_PH_Patients_Records_and_BMI_Range_Record_Dataset = len(PH_Patients_Records_and_BMI_Range_Record_Dataset[column_PH_Patients_Records_and_BMI_Range_Record_Dataset])
    nan_count_PH_Patients_Records_and_BMI_Range_Record_Dataset = PH_Patients_Records_and_BMI_Range_Record_Dataset[column_PH_Patients_Records_and_BMI_Range_Record_Dataset].isna().sum()  # Count NaN values
    empty_count_PH_Patients_Records_and_BMI_Range_Record_Dataset = PH_Patients_Records_and_BMI_Range_Record_Dataset[column_PH_Patients_Records_and_BMI_Range_Record_Dataset].eq('').sum()  # Count empty string values
    prefer_not_to_say_count_PH_Patients_Records_and_BMI_Range_Record_Dataset = PH_Patients_Records_and_BMI_Range_Record_Dataset[column_PH_Patients_Records_and_BMI_Range_Record_Dataset].eq('Prefer not to answer').sum()  

    unique_counts_PH_Patients_Records_and_BMI_Range_Record_Dataset[column_PH_Patients_Records_and_BMI_Range_Record_Dataset] = [unique_count_PH_Patients_Records_and_BMI_Range_Record_Dataset]
    row_counts_PH_Patients_Records_and_BMI_Range_Record_Dataset[column_PH_Patients_Records_and_BMI_Range_Record_Dataset] = [row_count_PH_Patients_Records_and_BMI_Range_Record_Dataset]
    nan_counts_PH_Patients_Records_and_BMI_Range_Record_Dataset[column_PH_Patients_Records_and_BMI_Range_Record_Dataset] = [nan_count_PH_Patients_Records_and_BMI_Range_Record_Dataset]
    empty_counts_PH_Patients_Records_and_BMI_Range_Record_Dataset[column_PH_Patients_Records_and_BMI_Range_Record_Dataset] = [empty_count_PH_Patients_Records_and_BMI_Range_Record_Dataset]
    prefer_not_to_say_counts_PH_Patients_Records_and_BMI_Range_Record_Dataset[column_PH_Patients_Records_and_BMI_Range_Record_Dataset] = [prefer_not_to_say_count_PH_Patients_Records_and_BMI_Range_Record_Dataset]




    

# Create DataFrames from the dictionaries
unique_counts_PH_Patients_Records_and_BMI_Range_Record_Datasets = []
row_counts_PH_Patients_Records_and_BMI_Range_Record_Datasets = []
nan_counts_PH_Patients_Records_and_BMI_Range_Record_Datasets = []
empty_counts_PH_Patients_Records_and_BMI_Range_Record_Datasets = []
prefer_not_to_say_counts_PH_Patients_Records_and_BMI_Range_Record_Datasets =[]

unique_counts_PH_Patients_Records_and_BMI_Range_Record_Datasets = pd.DataFrame(unique_counts_PH_Patients_Records_and_BMI_Range_Record_Dataset, index=['Unique Count'])
row_counts_PH_Patients_Records_and_BMI_Range_Record_Datasets = pd.DataFrame(row_counts_PH_Patients_Records_and_BMI_Range_Record_Dataset, index=['Row Count'])
nan_counts_PH_Patients_Records_and_BMI_Range_Record_Datasets = pd.DataFrame(nan_counts_PH_Patients_Records_and_BMI_Range_Record_Dataset, index=['NaN Count'])
empty_counts_PH_Patients_Records_and_BMI_Range_Record_Datasets = pd.DataFrame(empty_counts_PH_Patients_Records_and_BMI_Range_Record_Dataset, index=['Empty Count'])
prefer_not_to_say_counts_PH_Patients_Records_and_BMI_Range_Record_Datasets = pd.DataFrame(prefer_not_to_say_counts_PH_Patients_Records_and_BMI_Range_Record_Dataset, index=['Prefer not to answer'])

# Concatenate the DataFrames
result_PH_Patients_Records_and_BMI_Range_Record_Dataset = []
result_PH_Patients_Records_and_BMI_Range_Record_Dataset = pd.concat([unique_counts_PH_Patients_Records_and_BMI_Range_Record_Datasets, row_counts_PH_Patients_Records_and_BMI_Range_Record_Datasets, nan_counts_PH_Patients_Records_and_BMI_Range_Record_Datasets, empty_counts_PH_Patients_Records_and_BMI_Range_Record_Datasets,prefer_not_to_say_counts_PH_Patients_Records_and_BMI_Range_Record_Datasets])

# Display the combined DataFrame
#print("PH_Patients_Records_and_BMI_Range_Record_Dataset:")
#display(result_PH_Patients_Records_and_BMI_Range_Record_Dataset)
print()
#print()
#display(PH_Patients_Records_and_BMI_Range_Record_Dataset.head(3))
#print()
#print()


# Total number of participants
total_participants = []
total_participants = 2727

# Drop duplicate Participant ID rows to get unique participants
unique_participants = []
unique_participants = PH_Patients_Records_and_BMI_Range_Record_Dataset.drop_duplicates(subset=['Participant ID'])



# Display unique items under the column "BMI Range"
unique_BMI_status = []
unique_BMI_status = unique_participants['BMI Range'].unique()
# Print the unique items
#display(unique_BMI_status)
print()
print()


# Count occurrences of unique values in the 'BMI Range' column
BMI_status_counts = []
BMI_status_counts = unique_participants['BMI Range'].value_counts()

# Calculate the percentage 
BMI_status_percentages = []
BMI_status_percentages = (BMI_status_counts / total_participants) * 100

# Combine counts and percentages
BMI_status_counts_with_percentages = []
BMI_status_counts_with_percentages = BMI_status_counts.astype(str) + " (" + BMI_status_percentages.round(2).astype(str) + "%)"



# Display the counts
#print("Counts of unique values in the 'BMI Range' column:")
#display(BMI_status_counts_with_percentages)
#print()


# <div style="background-color: #d3f5f5; padding: 10px;">
#     <h2><center>Age Specific Mortality Counts for PH Patients </center></h2>
# </div>

# In[ ]:


#PH_Patients_Records.head(3)


# In[ ]:


# Total number of participants
total_participants = []
total_participants = 2727


# Drop duplicate Participant ID rows to get unique participants
unique_participants = []
unique_participants = PH_Patients_Records.drop_duplicates(subset=['Participant ID'])

# Count occurrences of unique values in the 'Alive / Dead' column
total_alive_dead_counts = []
total_alive_dead_counts = unique_participants['Alive / Dead'].value_counts()

# Calculate the percentage 
total_alive_dead_percentages = []
total_alive_dead_percentages = (total_alive_dead_counts / total_participants) * 100

# Combine counts and percentages
total_alive_dead_counts_with_percentages = []
total_alive_dead_counts_with_percentages = total_alive_dead_counts.astype(str) + " (" + total_alive_dead_percentages.round(2).astype(str) + "%)"



# Display the counts
print("Counts of unique values in the 'Alive / Dead' column:")
display(total_alive_dead_counts_with_percentages)
print()
print()

# Assume the DataFrame is already loaded as All_ICD10_with_Diseases_Dates_Data

# Define the age ranges
bins = [30, 40, 50, 60, 70, 80, 90, 100]
labels = ["30 - 40", "41 - 50", "51 - 60", "61 - 70", "71 - 80", "81 - 90", "91 - 100"]

# Create a new column 'Age Range' with the defined bins
PH_Patients_Records['PH Age Range'] = pd.cut(PH_Patients_Records['PH Individual Age'], bins=bins, labels=labels, right=False)

# Total number of participants
total_participants = []
total_participants = 2727


# Drop duplicate Participant ID rows to get unique participants
unique_participants = []
unique_participants = PH_Patients_Records.drop_duplicates(subset=['Participant ID'])

# Separate the counts for 'Alive' and 'Dead' within each age range
alive_counts = []
dead_counts = []
alive_counts = unique_participants[unique_participants['Alive / Dead'] == 'Alive']['PH Age Range'].value_counts().sort_index()
dead_counts = unique_participants[unique_participants['Alive / Dead'] == 'Dead']['PH Age Range'].value_counts().sort_index()

# Calculate the percentages
alive_percentages = []
dead_percentages = []
alive_percentages = (alive_counts / total_participants) * 100
dead_percentages = (dead_counts / total_participants) * 100

# Combine counts and percentages for 'Alive'
alive_counts_with_percentages = alive_counts.astype(str) + " (" + alive_percentages.round(2).astype(str) + "%)"

# Combine counts and percentages for 'Dead'
dead_counts_with_percentages = []
dead_counts_with_percentages = dead_counts.astype(str) + " (" + dead_percentages.round(2).astype(str) + "%)"

# Display the counts and percentages for 'Alive'
#print("Counts and percentages for 'Alive' in each age range:")
#display(alive_counts_with_percentages)
#print()
#print()

# Display the counts and percentages for 'Dead'
#print("Counts and percentages for 'Dead' in each age range:")
#display(dead_counts_with_percentages)
#print()


# <div style="background-color: #d3f5f5; padding: 10px;">
#     <h2><center>Matched Control Cohort </center></h2>
# </div>

# In[ ]:


All_ICD10_with_Diseases_Dates_Data = []
All_ICD10_with_Diseases_Dates_Data = pd.read_csv('Dataset with ICD10 and Diseases Names and Death Records.csv')
#All_ICD10_with_Diseases_Dates_Data.head(3)


# In[ ]:


Smoking = []
Smoking = pd.read_csv('Smoking Status Record Dataset.csv')
#Smoking.head(3)


# In[ ]:


BMI = []
BMI = pd.read_csv('BMI Range Record Dataset.csv')
#BMI.head(3)


# In[ ]:


IMD = []
IMD = pd.read_csv('IMD Records with IMD_Quintile.csv')
#IMD.head(3)


# In[ ]:


Combined_ICD10_codes_and_UKB_IMD_Records = []
Combined_ICD10_codes_and_UKB_IMD_Records = pd.merge(All_ICD10_with_Diseases_Dates_Data,Smoking,   on="Participant ID", how="left")
Combined_ICD10_codes_and_UKB_IMD_Records = pd.merge(Combined_ICD10_codes_and_UKB_IMD_Records,BMI,   on="Participant ID", how="left")
Combined_ICD10_codes_and_UKB_IMD_Records = pd.merge(Combined_ICD10_codes_and_UKB_IMD_Records,IMD,   on="Participant ID", how="left")




# Create dictionaries to store unique counts, row counts, NaN counts, and empty counts
unique_counts_Combined_ICD10_codes_and_UKB_IMD_Records = {}
row_counts_Combined_ICD10_codes_and_UKB_IMD_Records = {}
nan_counts_Combined_ICD10_codes_and_UKB_IMD_Records = {}
empty_counts_Combined_ICD10_codes_and_UKB_IMD_Records = {}
prefer_not_to_say_counts_Combined_ICD10_codes_and_UKB_IMD_Records = {}

# Loop through columns and count unique items, row counts, NaN counts, and empty counts
for column_Combined_ICD10_codes_and_UKB_IMD_Records in Combined_ICD10_codes_and_UKB_IMD_Records.columns:
    unique_count_Combined_ICD10_codes_and_UKB_IMD_Records = Combined_ICD10_codes_and_UKB_IMD_Records[column_Combined_ICD10_codes_and_UKB_IMD_Records].nunique()
    row_count_Combined_ICD10_codes_and_UKB_IMD_Records = len(Combined_ICD10_codes_and_UKB_IMD_Records[column_Combined_ICD10_codes_and_UKB_IMD_Records])
    nan_count_Combined_ICD10_codes_and_UKB_IMD_Records = Combined_ICD10_codes_and_UKB_IMD_Records[column_Combined_ICD10_codes_and_UKB_IMD_Records].isna().sum()  # Count NaN values
    empty_count_Combined_ICD10_codes_and_UKB_IMD_Records = Combined_ICD10_codes_and_UKB_IMD_Records[column_Combined_ICD10_codes_and_UKB_IMD_Records].eq('').sum()  # Count empty string values
    prefer_not_to_say_count_Combined_ICD10_codes_and_UKB_IMD_Records = Combined_ICD10_codes_and_UKB_IMD_Records[column_Combined_ICD10_codes_and_UKB_IMD_Records].eq('Prefer not to answer').sum()  

    unique_counts_Combined_ICD10_codes_and_UKB_IMD_Records[column_Combined_ICD10_codes_and_UKB_IMD_Records] = [unique_count_Combined_ICD10_codes_and_UKB_IMD_Records]
    row_counts_Combined_ICD10_codes_and_UKB_IMD_Records[column_Combined_ICD10_codes_and_UKB_IMD_Records] = [row_count_Combined_ICD10_codes_and_UKB_IMD_Records]
    nan_counts_Combined_ICD10_codes_and_UKB_IMD_Records[column_Combined_ICD10_codes_and_UKB_IMD_Records] = [nan_count_Combined_ICD10_codes_and_UKB_IMD_Records]
    empty_counts_Combined_ICD10_codes_and_UKB_IMD_Records[column_Combined_ICD10_codes_and_UKB_IMD_Records] = [empty_count_Combined_ICD10_codes_and_UKB_IMD_Records]
    prefer_not_to_say_counts_Combined_ICD10_codes_and_UKB_IMD_Records[column_Combined_ICD10_codes_and_UKB_IMD_Records] = [prefer_not_to_say_count_Combined_ICD10_codes_and_UKB_IMD_Records]




    

# Create DataFrames from the dictionaries
unique_counts_Combined_ICD10_codes_and_UKB_IMD_Record = []
row_counts_Combined_ICD10_codes_and_UKB_IMD_Record = []
nan_counts_Combined_ICD10_codes_and_UKB_IMD_Record = []
empty_counts_Combined_ICD10_codes_and_UKB_IMD_Record = []
prefer_not_to_say_counts_Combined_ICD10_codes_and_UKB_IMD_Record =[]

unique_counts_Combined_ICD10_codes_and_UKB_IMD_Record = pd.DataFrame(unique_counts_Combined_ICD10_codes_and_UKB_IMD_Records, index=['Unique Count'])
row_counts_Combined_ICD10_codes_and_UKB_IMD_Record = pd.DataFrame(row_counts_Combined_ICD10_codes_and_UKB_IMD_Records, index=['Row Count'])
nan_counts_Combined_ICD10_codes_and_UKB_IMD_Record = pd.DataFrame(nan_counts_Combined_ICD10_codes_and_UKB_IMD_Records, index=['NaN Count'])
empty_counts_Combined_ICD10_codes_and_UKB_IMD_Record = pd.DataFrame(empty_counts_Combined_ICD10_codes_and_UKB_IMD_Records, index=['Empty Count'])
prefer_not_to_say_counts_Combined_ICD10_codes_and_UKB_IMD_Record = pd.DataFrame(prefer_not_to_say_counts_Combined_ICD10_codes_and_UKB_IMD_Records, index=['Prefer not to answer'])

# Concatenate the DataFrames
result_Combined_ICD10_codes_and_UKB_IMD_Records = []
result_Combined_ICD10_codes_and_UKB_IMD_Records = pd.concat([unique_counts_Combined_ICD10_codes_and_UKB_IMD_Record, row_counts_Combined_ICD10_codes_and_UKB_IMD_Record, nan_counts_Combined_ICD10_codes_and_UKB_IMD_Record, empty_counts_Combined_ICD10_codes_and_UKB_IMD_Record,prefer_not_to_say_counts_Combined_ICD10_codes_and_UKB_IMD_Record])

# Display the combined DataFrame
#print("Combined_ICD10_codes_and_UKB_IMD_Records:")
#display(result_Combined_ICD10_codes_and_UKB_IMD_Records)
#print()
#print()
#display(Combined_ICD10_codes_and_UKB_IMD_Records.head(3))
#print()


# In[ ]:


#file_path = []

## Specify the file path where you want to save the CSV file
#file_path = 'Dataset for Matched Control Cohort.csv'

## Use the to_csv method to save the DataFrame as a CSV file
#Combined_ICD10_codes_and_UKB_IMD_Records.to_csv(file_path, index=False)  # Set index=False to exclude the index column




