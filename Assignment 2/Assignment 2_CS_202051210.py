#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.graphics.gofplots import qqplot

pd.options.mode.chained_assignment = None


# ## Patient Attendance Data

# In[2]:


df1 = pd.read_csv("JK-Allopathic-Outpatient_attendance-May-2019.csv")
df1.head()


# In[3]:


'''
1. Compute total patient attendance for all district for all four range group and plot the bar
diagram. Set the bar plot parameters for better visualization.
'''

df_group1 = df1.groupby(by="District")[["No. of facilities by performance - 1 to 100", "No. of facilities by performance - 101 to 500", "No. of facilities by performance - 501 to 1000", "No. of facilities by performance - >1000"]].sum()
df_group1.plot(kind='barh', figsize=(16,20))


# In[4]:


'''
2. Compute total patient attendance for all district for each Facility Type (DH, CHC and SC) for all
four range groups and plot the staked bar diagram of three. Set the bar plot parameters for
better visualization.
'''

cols = ['District', 'Facility Type', 'Total No. of Facilities #']
df_group2 = df1[cols]
df_group2 = df_group2.pivot_table(index='District', columns='Facility Type', values='Total No. of Facilities #')
df_group2.plot(kind='bar', stacked=True, figsize=(16,9))


# In[5]:


'''
3. Plot group bar plot for Performance - Overall Average of different Facility Type (DH, CHC and
SC) of Anantnag, Jammu, Poonch, Reasi and Udhampur.
'''

df_group3 = df1.pivot_table('Performance - Overall Average **', index='District', columns='Facility Type')
df_group3 = df_group3.T[['Anantnag', 'Jammu', 'Poonch', 'Reasi','Udhampur']]
df_group3.plot(kind='bar', figsize=(16,9))


# In[6]:


'''
4. Present dot plot for Performance - Maximum of any 20 different district. Performance - Maxi
mum for different Facility Type should be combined appropriately using a aggregation function
for each district.
'''

df_group4 = df1.groupby(['District']).agg(Max = ('Performance - Maximum', 'max'))
df_group4 = df_group4.iloc[:20]
df_group4 = df_group4.reset_index()
fig, ax = plt.subplots(figsize=(16,9))
ax=sns.scatterplot(data=df_group4, x='District', y='Max');
ax.set_xticklabels(labels=df_group4['District'], rotation=30);


# ## Fifa Player Profile

# In[7]:


df2 = pd.read_csv("Fifa_player_football_data.csv")
df2.set_index(['ID'])


# In[8]:


'''
1. Present Age of various football players as histogram and kernel density plots. Set appropriate
parameters of the plot.
'''

df2_group1 = df2[["ID", "Name", "Age"]]
sns.histplot(data=df2_group1, x="Age", binwidth=1)


# In[9]:


sns.histplot(data=df2_group1, x="Age", binwidth=1, kde=True, color='y')


# In[10]:


'''
2. Present Age of various Football players as Kernel Density plots for each of FC Barcelona,
Chelsea, Juventus and Real Madrid Clubs. Set appropriate parameters of the plot.
'''

df2_group2 = df2.loc[df2['Club'].isin(['FC Barcelona','Chelsea','Juventus','Real Madrid'])]
plt.figure(figsize=(16,9))
sns.kdeplot(data=df2_group2, x="Age",hue="Club");


# In[11]:


'''
3. Plot Value of players as Stacked Histogram Preferred Foot wise (right and left).
'''

def change_val(row):
    value = row['Value'][1:]
    if 'K' in value:
        return float(value.replace('K',''))*1000
    if 'M' in value:
        return float(value.replace('M',''))*1000000
    return float(value)
df2_group3 = df2[['Value', 'Preferred Foot']]
df2_group3.loc[:, 'Value']=df2_group3.apply(change_val, axis=1)
bins=np.logspace(0, np.log10(df2_group3['Value'].max()), 70)
plt.figure(figsize=(16,9))
sns.histplot(data=df2_group3, x='Value', stat='count', hue='Preferred Foot', multiple='stack', bins=bins)
plt.xscale('log')


# In[12]:


'''
4. Check distribution of International Reputation using Q-Q plot.
'''

df2_group4 = df2['International Reputation']
plt.figure(figsize=(12,9))
ax = plt.gca()
qqplot(df2_group4,line='s', ax=ax)
plt.show()

