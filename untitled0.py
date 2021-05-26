#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  5 23:20:03 2021

@author: ozkan
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

fandango = pd.read_csv("fandango_scrape.csv")

x = fandango['VOTES']
y = fandango['RATING']

#plt.scatter(y,x)
#plt.ylabel('VOTES')
#plt.xlabel('RATING')

corre = fandango.corr()

fandango['YEAR'] = fandango['FILM'].apply(lambda title: title.split('(')[-1])
fandango['YEAR'] = fandango['YEAR'].apply(lambda x: x.replace(')',''))
count_per_year = fandango['YEAR'].value_counts()

#plt.hist(fandango['YEAR'])
#plt.xlabel('YEAR')
#plt.ylabel('count')
#plt.show()

highest_10_ratings = fandango.sort_values('VOTES',ascending=False)[:10]

zero_votes_sum = fandango.value_counts([fandango['VOTES']==0])

fan_reviewed = fandango.drop(fandango[fandango.VOTES==0].index)



#plt.figure(figsize=(10,4),dpi=150)
#sns.kdeplot(data=fan_reviewed,x='RATING',clip=[0,5],fill=True,label='True Rating')
#sns.kdeplot(data=fan_reviewed,x='STARS',clip=[0,5],fill=True,label='Stars Displayed')

#plt.legend(loc=(1.05,0.5))

fan_reviewed['STARS_DIFF'] = (fan_reviewed['STARS']-fan_reviewed['RATING']).round(2)

#sns.countplot(data=fan_reviewed,x='STARS_DIFF',palette='magma')

one_star_different = fan_reviewed[fan_reviewed['STARS_DIFF']==1]

all_sites = pd.read_csv('all_sites_scores.csv')
all_sites.info()
all_sites.describe()


#sns.scatterplot(data=all_sites,x='RottenTomatoes',y='RottenTomatoes_User')
#plt.xlim(0,100)
#plt.ylim(0,100)
all_sites['DIFF'] = all_sites['RottenTomatoes']-all_sites['RottenTomatoes_User']

mean_diff = all_sites['DIFF'].mad()




