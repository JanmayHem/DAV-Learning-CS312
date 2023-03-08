#!/usr/bin/env python
# coding: utf-8

# In[1]:


'''
# CS312 - Data Analytics and Visualization
# Janmay Joshi
# 202051210
'''

# Importing libraries
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


# ###  Reading Data

# In[2]:


female_population = pd.read_csv('population_of_female.csv')
female_completion = pd.read_csv('primary_completion_rate_female.csv')


# #### 1. Create a column named “average_rate” in “primary_completion_rate_female.csv” that contains the average (over time) completion rate.

# In[3]:


female_completion['avgRate'] = female_completion.mean(axis=1, numeric_only=True)
df1 = female_completion[['Country Name', 'avgRate']]
df1.head()


# #### 2. Create a column named “Latest Population” in “population_of_female.csv” that contains the latest population of females in the country.

# In[4]:


female_population['Latest Population'] = female_population.iloc[:,-1]
female_population.head()


# #### 3. What is the weighted average of primary rates of different countries? The weight should be the Latest population of females in the country.

# In[5]:


wtAvg, sum = 0, 0
for i in range(len(female_completion)):
    if np.isnan(female_completion['avgRate'][i]):
        continue
    else:
        wtAvg += female_completion['avgRate'][i] * female_population['Latest Population'][i]
        sum += female_population['Latest Population'][i]
wtAvg /= sum
print(wtAvg)


# #### 4. What is the Median of average primary completion rate?

# In[6]:


median = female_completion['avgRate'].median()
print(median)


# #### 5. What is the InterQuartile Range of average primary completion rate?

# In[7]:


q1, q3 = female_completion['avgRate'].quantile([.25,.75])
iqr = q3-q1
print(iqr)


# #### 6. What is the Variance of average primary completion rate?

# In[8]:


variance = female_completion['avgRate'].var()
print(variance)

