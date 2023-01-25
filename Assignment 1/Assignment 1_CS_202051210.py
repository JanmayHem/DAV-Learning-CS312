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
import json


# In[2]:


'''
1. Create two data frames by reading above two files.
''' 

df1 = pd.read_csv("district_level_service_msme.csv")
df1.head()


# In[3]:


df2 = json.load(open("district_level_manufacturing_msme.json"))
columns=pd.DataFrame(df2["fields"])["label"].tolist()
df2 = pd.DataFrame(df2["data"],columns=columns)
df2.head()


# In[4]:


'''
2. Find out total ”Small” Manufacturing MSME in India.
''' 

df1["MICRO"]=pd.to_numeric(df1["MICRO"])
df1["SMALL"]=pd.to_numeric(df1["SMALL"])
df1["MEDIUM"]=pd.to_numeric(df1["MEDIUM"])

df2["MICRO"]=pd.to_numeric(df2["MICRO"])
df2["SMALL"]=pd.to_numeric(df2["SMALL"])
df2["MEDIUM"]=pd.to_numeric(df2["MEDIUM"])
df2["Lg_Dist_Code"]=pd.to_numeric(df2["Lg_Dist_Code"])
df2["Total"]=pd.to_numeric(df2["Total"])
df2.head()


# In[5]:


small_sum1 = df1["SMALL"].sum()
small_sum2 = df2["SMALL"].sum()
# print("The sum of small1 MSME is:", small_sum1)
print("The sum of small2 MSME is:", small_sum2)


# In[6]:


'''
3.Create a dataframe having state wise total number of ”Micro”,”Small” and ”Medium” Services 
MSE (as shown below) and save the results as a CSV file.
''' 

data_source = {'State': df1["STATE_NAME"],
        'Micro': df1["MICRO"],
        'Small': df1["SMALL"],
        'Medium': df1["MEDIUM"]}
df3=pd.DataFrame(data_source)
df3=df3.groupby(by="State")[['Micro','Small','Medium']].sum()
df3.to_csv("MSME-Data.csv",index=False)
df3.head()


# In[7]:


'''
4. Join the both the data frame based on common STATE NAME, DISTRICT NAME, Lg Dist Code and 
Last Updated. The result should look like below. ”x” and ”y” in below image represent the
manufacturing MSME and service MSME respectively.
'''

df_merged = pd.merge(df2,df1, left_on=["STATE_NAME","Lg_Dist_Code","DISTRICT_NAME","Last_Updated"],right_on=["STATE_NAME","Lg_Dist_Code","DISTRICT_NAME","Last_Updated"])
df_merged


# In[8]:


'''
5. Create a Pivot Table having rows STATE NAME and columns Service and Manufacturing ”MSME” as shown
in below. Use ”Sum” to add up district wise number.
''' 

df_merged=df_merged.groupby("STATE_NAME")[["MEDIUM_x","MEDIUM_y","MICRO_x","MICRO_y","SMALL_x","SMALL_y"]].sum()
df_merged

