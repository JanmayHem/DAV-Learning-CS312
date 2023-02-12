#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import transforms
from joypy import joyplot 
import squarify
import plotly.express as px 
from itertools import product


# In[2]:


milk_df = pd.read_csv("Milk_Production_2007_2012.csv", index_col='States/Uts')
milk_df.head()


# In[3]:


egg_df = pd.read_csv("Egg_Production_2007_2012.csv", index_col='States/Uts')
egg_df.columns = milk_df.columns
egg_df.head()


# In[4]:


merged_df = pd.concat([egg_df, milk_df], axis=1, keys=['Eggs', 'Milk'])
merged_df.fillna(0, inplace=True)
merged_df.head()


# In[5]:


eggtemp = egg_df.copy()
milktemp = milk_df.copy()
eggtemp.columns = pd.MultiIndex.from_product([egg_df.columns, ['Egg']])
milktemp.columns = pd.MultiIndex.from_product([milk_df.columns, ['Milk']])
merged_df1 = eggtemp[['2007-08']].join(milktemp[['2007-08']])
for year, item in eggtemp.columns[1:]:
    temp = eggtemp[[year]].join(milktemp[[year]])
    merged_df1 = merged_df1.join(temp)
merged_df1.fillna(0, inplace=True)
merged_df1.head()


# In[6]:


states = merged_df1[:35].index
cmap = plt.get_cmap("tab20c")
_, ax = plt.subplots(1, 2, figsize=(20, 10))
size=0.3

ax[0].pie(merged_df.loc[states, 'Eggs'].to_numpy().flatten(), radius=1-size, wedgeprops=dict(width=0.3, edgecolor='w'))
ax[0].pie(merged_df.loc[states, 'Eggs'].to_numpy().sum(axis=1), radius=1, wedgeprops=dict(width=0.3, edgecolor='w'), labels=states)
ax[0].legend(merged_df[['Eggs']].columns.get_level_values(1), loc='upper left', bbox_to_anchor=(1, 1), fontsize=12)

ax[1].pie(merged_df.loc[states, 'Milk'].to_numpy().flatten(), radius=1-size, wedgeprops=dict(width=0.3, edgecolor='w'))
ax[1].pie(merged_df.loc[states, 'Milk'].to_numpy().sum(axis=1), radius=1, wedgeprops=dict(width=0.3, edgecolor='w'), labels=states)
ax[1].legend(merged_df[['Milk']].columns.get_level_values(1), loc='upper left', bbox_to_anchor=(1, 1), fontsize=12);


# In[7]:


egg_df = merged_df['Eggs'].drop('All India').reset_index()
egg_df = egg_df.melt(id_vars='States/Uts', var_name='Year', value_name='Production')
fig = px.treemap(egg_df, path=['States/Uts', 'Year'], values='Production', color_continuous_scale='RdBu')
fig.show()


# In[8]:


milk_df = merged_df['Milk'].drop('All India').reset_index()
milk_df = milk_df.melt(id_vars='States/Uts', var_name='Year', value_name='Production')
fig = px.treemap(milk_df, path=['States/Uts', 'Year'], values='Production', color_continuous_scale='RdBu')
fig.show()


# In[ ]:




