#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import seaborn as sns


# In[2]:


data = pd.read_csv("heart.csv")
data.head()


# ### 1. Plot correlogram to check relationship amongst various measures.
# ### 2. Draw Heat map to check relationships amongst various measures.

# In[3]:


g = sns.PairGrid(data[['age', 'trestbps','chol', 'fbs', 'oldpeak', 'ca', 'thal']])
g.map(sns.scatterplot);


# In[4]:


data.iloc[:,:-1].corr()


# In[5]:


ax = sns.heatmap(data.iloc[:,:-1].corr())

