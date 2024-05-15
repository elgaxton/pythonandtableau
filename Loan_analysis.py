# -*- coding: utf-8 -*-
"""
Created on Sat May 11 12:54:30 2024

@author: Gaxton Okobah
"""

import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Method 1 to read Json data
json_file = open('loan_data_json.json')
data = json.load(json_file)

#Method 2 to read json data

with open('loan_data_json.json') as json_file:
    data = json.load(json_file)
    

#transform to dataframe
loandata = pd.DataFrame(data)

#finding unoque values for the purpose column


#Describe the data
loandata.describe()

#describe the data for a specific column
loandata['int.rate'].describe()

loandata['fico'].describe()

loandata['dti'].describe()

# using EXP() to get annual income

income = np.exp(loandata['log.annual.inc'])

loandata['annualincome'] = income

#working with if statements



#FICO Score

fico = 250

if fico >= 300 and fico < 400:
    ficocat = 'Very Poor'
elif fico >= 400 and fico < 600:
    ficocat = 'Poor'
elif fico >= 601 and fico < 660:
    ficocat = 'Fair'
elif fico >= 660 and fico < 700:
    ficocat = 'Good'
elif fico >= 700:
    ficocat = 'Excellent'
else:
    ficocat = 'Unknown'
print (ficocat)



# Applying for loops to loan data 
#using first 10

length = len(loandata)
ficocat = []
for x in range(0,length):
    category = loandata['fico'][x]
    
    try:
        
        if category >= 300 and category < 400:
            cat = 'Very Poor'
        elif category >= 400 and category < 600:
            cat = 'Poor'
        elif category >= 601 and category < 660:
            cat = 'Fair'
        elif category >= 660 and category < 700:
            cat = 'Good'
        elif category >= 700:
            cat = 'Excellent'
        else:
            cat = 'Unknown'
    except:
        cat = 'Unknown'
    ficocat.append(cat)
    
ficocat = pd.Series(ficocat)

loandata['fico.category'] = ficocat


#df.loc as conditional statement
#df.loc[df[columname] condition, newcolumname] = 'value if the condition is met'

#for interest rates, a new column is wanted. rate > 0.12 then high, else low

loandata.loc[loandata['int.rate'] > 0.12, 'int.rate.type'] = 'High'
loandata.loc[loandata['int.rate'] <= 0.12, 'int.rate.type'] = 'Low'


#number of loans /rows by fico.category

catplot = loandata.groupby (['fico.category']).size()
catplot.plot.bar(color = 'green' , width =0.1)
plt.show()


purposeplot = loandata.groupby (['purpose']).size()
purposeplot.plot.bar(color = 'red' , width =0.2)
plt.show()


#scatter plots
ypoint = loandata['annualincome']
xpoint = loandata['dti']
plt.scatter(xpoint, ypoint, color ='#4caf50')
plt.show()



#writing to csv
loandata.to_csv('loan_cleaned.csv',index = True)































