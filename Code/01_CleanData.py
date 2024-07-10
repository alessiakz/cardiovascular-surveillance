#01_CleanData.py
    #this script is used to re-structure, clean and conduct initial data checks of data
#Created: 07.09.2024
#By: Alessia Kettlitz

#importing libraries
import pandas as pd, numpy as np, matplotlib as plt, seaborn as sns

from pyprojroot.here import here #importing here function for relative file paths

from joblib import dump, load #for saving dataframes

#importing data
data_raw = pd.read_csv(here('Raw_Data/National_Vital_Statistics_System__NVSS__-_National_Cardiovascular_Disease_Surveillance_Data_20240709.csv'))

#initial data exploration

#printing head of data
print(data_raw.head(50))

#printing summary information of dataframe
print(data_raw.info())
    #174,720 observations
    #30 variables

#basic stats for all variables in dataframe
print(data_raw.describe(include='all'))

#find all unique values in 'RowId' column - this will inform what to subset
unique_rowId = data_raw['RowId'].unique()
print(unique_rowId)

#filtering dataset to where RowId contains string 'Age-Standardized' - we will subset just to standardized estimates by age
data_filter = data_raw[(data_raw['RowId'].str.contains('Age-Standardized')) & (data_raw['BreakOutId'] == 'OVR01')]

print(data_filter)
#this reduces to 8736 rows - more manageable for this project for now!

print(data_filter.head(50))

print(data_filter.info())

#drop columns that will not be used
columns_to_drop = ['DataSource', 'PriorityArea1', 'PriorityArea2', 'PriorityArea3', 'PriorityArea4', 'Class', 'Break_Out_Category', 'Break_Out', 'ClassId', 'Data_Value_TypeID', 'BreakOutCategoryId', 'BreakOutId']
data_filter.drop(columns=columns_to_drop, inplace=True)

print(data_filter.head(50))

#compute descriptive statistics grouped by 'Question'
stats_by_question = data_filter.groupby(['YearStart', 'LocationAbbr', 'Question'])['Data_Value'].describe()

print(stats_by_question)

#data is now ready for visualizations!

#export dataframe to joblib file
dump(data_filter, here('Clean_Data/data.joblib'))

