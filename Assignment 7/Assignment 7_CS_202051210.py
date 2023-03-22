#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
from sklearn.model_selection import StratifiedShuffleSplit
import seaborn as sns


# In[2]:


df = pd.read_csv("weight-height.csv")

height_mean = round(df["Height"].mean(),3)
weight_mean = round(df["Weight"].mean(),3)

print("Population mean of height (Whole Data):",height_mean)
print("Population mean of weight (Whole Data):",weight_mean)


# #### 1) Perform Random Sampling by choosing 1000 samples from data. Compute the sample mean and population mean (from whole data) and then compute the error between both mean.

# In[3]:


sample1 = df.sample(n=1000).sort_index()
sample1_height_mean = round(sample1["Height"].mean(),3)
sample1_weight_mean = round(sample1["Weight"].mean(),3)

print("Population mean of height (Sample1 Data):",sample1_height_mean)
print("Population mean of weight (Sample1 Data):",sample1_weight_mean)


# In[4]:


Error1_height = abs(round(sample1_height_mean-height_mean,3))
Error1_weight = abs(round(sample1_weight_mean-weight_mean,3))
print("Error in height (Random Sampling):",Error1_height)
print("Error in weight (Random Sampling):",Error1_weight)


# #### 2) Perform Systematic Sampling by choosing 1000 samples from data. Compute the sample mean and population mean (from whole data) and then compute the error between both mean.

# In[5]:


def systematic_sampling(df, step): 
    indexes = np.arange(0,len(df),step=step)
    systematic_sample = df.iloc[indexes]
    return systematic_sample

sample2 = systematic_sampling(df, 10)
sample2_height_mean = round(sample2["Height"].mean(),3)
sample2_weight_mean = round(sample2["Weight"].mean(),3)

print("Population mean of height (Sample2 Data):",sample2_height_mean)
print("Population mean of weight (Sample2 Data):",sample2_weight_mean)


# In[6]:


Error2_height = abs(round(sample2_height_mean-height_mean,3))
Error2_weight = abs(round(sample2_weight_mean-weight_mean,3))
print("Error in height (Random Sampling):",Error2_height)
print("Error in weight (Random Sampling):",Error2_weight)


# #### 3) Perform Stratified Sampling by choosing 1000 samples from data. Compute the sample mean and population mean (from whole data) and then compute the error between both mean.

# In[7]:


split = StratifiedShuffleSplit(n_splits=1, test_size=1000)

for x, y in split.split(df, df['Gender']):
    sample3 = df.iloc[y]

sample3_height_mean = round(sample3["Height"].mean(),3)
sample3_weight_mean = round(sample3["Weight"].mean(),3)

print("Population mean of height (Sample3 Data):",sample3_height_mean)
print("Population mean of weight (Sample3 Data):",sample3_weight_mean)


# In[8]:


Error3_height = abs(round(sample3_height_mean-height_mean,3))
Error3_weight = abs(round(sample3_weight_mean-weight_mean,3))
print("Error in height (Random Sampling):",Error3_height)
print("Error in weight (Random Sampling):",Error3_weight)

