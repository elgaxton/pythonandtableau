# -*- coding: utf-8 -*-
"""
Created on Tue Apr 30 17:30:01 2024

@author: Gaxton Okobah
"""

import pandas as pd

# file_name = pd.read_csv('file.csv) <----- format of read_csv

data = pd.read_csv('transaction.csv')

data = pd.read_csv('transaction.csv',sep=';')

#summary of the data

data.info()

#working with calculation

#Defining variables

CostPerItem = 11.73
SellingPricePerItem  = 21.11
NumberofItemsPurchased = 6

#Mathematical operatoions on Tableau

ProfitPerItem = 21.11 - 11.73
ProfitPerItem = SellingPricePerItem - CostPerItem

ProfitPerTransaction = NumberofItemsPurchased * ProfitPerItem

CostPerTransaction = NumberofItemsPurchased * CostPerItem
SellingPricePerTransaction = NumberofItemsPurchased * SellingPricePerItem

#CostPerTransaction Column Calculation
# CostPerTransaction = NumberofItemsPurchased * CostPerItem
#variable = daraframe['column_name']

CostPerItem = data['CostPerItem']
NumberofItemsPurchased = data['NumberOfItemsPurchased']

CostPerTransaction = CostPerItem * NumberofItemsPurchased

#Adding new column to dataframe

data['CostPerTransaction'] = CostPerTransaction

#Sales Per Transaction

data['SalesPerTransaction'] = data['SellingPricePerItem'] * data['NumberOfItemsPurchased']

#Profit calculation = Sales - Cost

data['ProfitPerTransaction'] = data['SalesPerTransaction'] - data['CostPerTransaction']

#Markup = (Sales - Cost)/Cost

data['Markup'] = (data['SalesPerTransaction'] - data['CostPerTransaction']) /data['CostPerTransaction']

data['Markup'] = (data['ProfitPerTransaction']) /data['CostPerTransaction']

#Rounding Markup

# roundmarkup = round(data['Markup'],2)

data['Markup'] = round(data['Markup'],2)

#combining data fields

my_date = 'Day' +'-'+'Month'+'-'+'Year'

#my_date = data['Day'] +'-'

print(data['Day'].dtype)

#Change columns type

day = data['Day'].astype(str)
year = data['Year'].astype(str)

print(data['Year'].dtype)
my_date = day+'-' +data['Month']+'-'+year

data['date'] = my_date

#using iloc to view specific columns/ rows

data.iloc[0] #views the row with index = 0

data.iloc[0:3] #first three rows

data.iloc[5:] #last 5 rows

data.head(5) #brings in first 5 row

data.iloc[:,2] # brings in all rows and second column

data.iloc[4,2] #brings in fourth row and second column

#Using split to split the client keywords field
#new_var = column.str.split('sep', expand =true)

split_col = data['ClientKeywords'].str.split(',' , expand=True)

#creating new columns for the split in Client Keywords

data['ClientAge'] = split_col[0]

data['ClientType'] = split_col[1]

data['LengthofContract'] = split_col[2]

#using the replace function

data['ClientAge'] = data['ClientAge'].str.replace('[', '')

data['LengthofContract'] = data['LengthofContract'].str.replace(']','')


# using the lower function to change Item to lower case

data['ItemDescription'] =data['ItemDescription'].str.lower()

#How to merge files

#Bringin  in a new dataset


seasons = pd.read_csv('value_inc_seasons.csv',sep=';')
#merging files: merge_df = pd.merge(df_old, df_new, on = 'key')

data = pd.merge(data, seasons, on = 'Month')


# remove columns
#data = data.drop(columns = ['Clientage'])

#df = df.drop('columnname', axis =1)

data = data.drop('ClientKeywords', axis= 1)

data = data.drop(['Year','Month', 'Day'], axis= 1)

#Export into csv

data.to_csv('Sbits_Cleaned.csv', index = False)





