# -*- coding: utf-8 -*-
"""
Created on Thu May 16 13:59:14 2024

@author: Gaxton Okobah
"""

import pandas as pd

from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

#reading excel or xlsx files

data = pd.read_excel('articles.xlsx')


#summary of the data
data.describe()

#summary of the columns
data.info()

#Counting the number of articles by source
#format of groupby: df.groupby(['column_to_group])['column_to_count'].count()

data.groupby(['source_id'])['article_id'].count()

# number of reactions by publisher
data.groupby(['source_id'])['engagement_reaction_count'].sum()

#dropping a column

data = data.drop('engagement_comment_plugin_count' , axis =1)

#Functions in Python

def thisFunction():
    print ('This is my first function')
                
thisFunction()

#This is a function with variables

def aboutMe(name, surname, location):
    print('This is ' +name+ ' My surname is ' +surname+ ' I am from '+location)
    return name, surname, location
a = aboutMe('Gaxton', 'Okobah', 'Nigeria')


#Creating a keyword flag

keyword = 'crash'

# Lets create a for loop to isolate each title row
# =============================================================================
# 
# keyword_flag = []
# for x in range(0,10):
#     heading = data['title'][x]
#     if keyword in heading:
#         flag = 1
#     else:
#         flag = 0
#     keyword_flag.append(flag)
# =============================================================================
    
#creating a function

def keywordflag(keyword):
    length = len(data)
    keyword_flag = []
    for x in range(0,length):
        heading = data['title'][x]
        try:
            if keyword in heading:
                flag = 1
            else:
                flag = 0
        except:
            flag = 0
        keyword_flag.append(flag)
    return keyword_flag

keywordflag = keywordflag('murder')

#creating a new column in data dataframe

data['keyword_flag'] = pd.Series(keywordflag)

# from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

sent_int = SentimentIntensityAnalyzer()

text = data['title'][16]

sent = sent_int.polarity_scores(text)

neg = sent['neg']
pos = sent['pos']
neu = sent['neu']

#adding a for loop to extract sentiment per title

title_neg_sentiment = []
title_pos_sentiment = []
title_neu_sentiemnt = []

length = len(data)

for x in range(0,length):
    try:
        text = data['title'][x]
        sent_int = SentimentIntensityAnalyzer()
        sent = sent_int.polarity_scores(text)
        neg  = sent['neg']
        pos = sent['pos']
        neu = sent ['neu']
    except:
        neg = 0
        pos = 0
        neu = 0
    title_neg_sentiment.append(neg)
    title_pos_sentiment.append(pos)
    title_neu_sentiemnt.append(neu)

title_neg_sentiment = pd.Series(title_neg_sentiment)
title_pos_sentiment = pd.Series(title_pos_sentiment)
title_neu_sentiemnt = pd.Series(title_neu_sentiemnt)

data['title_neg_sentiment'] = title_neg_sentiment
data['title_pos_sentiment'] = title_pos_sentiment
data['title_neu_sentiemnt'] = title_neu_sentiemnt

#writing the data

data.to_excel('blogme_cleaned.xlsx', sheet_name ='blogmedata', index=False)





















