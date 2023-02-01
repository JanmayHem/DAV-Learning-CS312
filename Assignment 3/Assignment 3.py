#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Importing 
import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.graphics.gofplots import qqplot
from joypy import joyplot 


# ### 1. Present the data from the dataset using three appropriate plots explained in Class.

# In[2]:


# Reading and perprocessing the data frame
df = pd.read_csv('grains_production_india_from_2001_to_2017.csv')
df.fillna(0)
df1 = pd.melt(df, id_vars=['Year'], value_vars=['Food Grains (Cereals) - Rice (000 tonnes)',
                                          'Food Grains (Cereals) - Jowar (000 tonnes)',
                                          'Food Grains (Cereals) - Bajra (000 tonnes)',
                                          'Food Grains (Cereals) - Maize (000 tonnes)',
                                          'Food Grains (Cereals) - Ragi (000 tonnes)',
                                          'Food Grains (Cereals) - Small Millets (000 tonnes)',
                                          'Food Grains (Cereals) - Wheat (000 tonnes)',
                                          'Food Grains (Cereals) - Barley (000 tonnes)',
                                          'Food Grains (Cereals) - Total (000 tonnes)',
                                          'Food Grains (Pulses) - Gram (000 tonnes)',
                                          'Food Grains (Pulses) - Tur (000 tonnes)',
                                          'Food Grains (Pulses) - Other Pulses (000 tonnes)',
                                          'Food Grains (Pulses) - Total (000 tonnes)',
                                          'Food Grains - Total (000 tonnes)',
                                          'Oilseeds - Ground-nuts (000 tonnes)',
                                          'Oilseeds - Sesamum (000 tonnes)',
                                          'Oilseeds - Rapeseed and Mustard (000 tonnes)',
                                          'Oilseeds - Linseed (000 tonnes)',
                                          'Oilseeds - Castor seed (000 tonnes)',
                                          'Total Nine Oilseeds (000 tonnes)',
                                          'Cotton (000 Bales)',
                                          'Jute (000 Bales)',
                                          'Mesta (000 Bales)',
                                          'Tea (Million kgs)',
                                          'Coffee (000 MT)',
                                          'Natural Rubber (000 MT)',
                                          'Banana (000 tonnes)',
                                          'Sugarcane (000 tonnes)',
                                          'Tobacco (000 tonnes)',
                                          'Potatoes (000 tonnes)',
                                          'Black Pepper (000 tonnes)',
                                          'Chillies (000 tonnes)',
                                          'Ginger (000 tonnes)',
                                          'Coconut (000 tonnes)',
                                          'Turmeric (000 tonnes)'])
df1['Year'] = df1['Year'].apply(lambda x: x[:x.index("-")])
df1[["Year"]] = df1[["Year"]].apply(pd.to_numeric)
df1.head()


# In[3]:


# Plot 1 - point plot
fig, ax = plt.subplots(figsize=(16, 15))
ax = sns.pointplot(data=df, join=False)
plt.xticks(rotation=90);
ax.set_ylim(-1000,40000);


# In[4]:


# Plot 2 - box plot
fig, ax = plt.subplots(figsize=(16, 15))
sns.boxplot(data=df) 
plt.xticks(rotation=90);
ax.set_ylim(-1000,48000);


# In[5]:


# Plot 3 - violin plot
fig, ax = plt.subplots(figsize=(16, 15))
sns.violinplot(data=df)
plt.xticks(rotation=90);


# In[6]:


# Plot - strip + violin plot
fig, ax = plt.subplots(figsize=(16, 9));
plt.xticks(rotation=90);
sns.stripplot(x='variable', y='value', data=df1, ax=ax);
sns.violinplot(x='variable', y='value', data=df1,color="0.8", ax=ax);


# In[7]:


# Plot - joyplot
fig, axes = joyplot(df1, by="variable", column="Year", figsize=(16,20), overlap=0)


# In[8]:


# Plot trial - Lineplot (Tried this plot because it can be insightful)
fig, ax = plt.subplots(figsize=(16, 20))
ax = sns.lineplot(data=df1, x="Year", y="value", hue="variable");
h, l = ax.get_legend_handles_labels()
ax.set_ylim(-1000,48000)
ax.set_xlim(2000,2017)
ax.legend(loc='center left', bbox_to_anchor=(1, 0.5));

