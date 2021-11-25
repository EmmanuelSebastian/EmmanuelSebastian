#!/usr/bin/env python
# coding: utf-8

# # Emmanuel Sebastian
# 100799374

# In[1]:


# 1. Import Python Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[2]:


# 2. Expand the number of columns
pd.set_option('max_columns', 500)


# In[3]:


# 3. Read dataset
youtubedata = pd.read_csv('./youtube_dataset.csv')
youtubedata.head()


# In[4]:


# 4. Bring top 1000 records in a dataframe
first_thousand = youtubedata.iloc[:1000,:]
first_thousand


# In[5]:


# 5. create a function to calculate the distribution of channeltype from the top 1000 records.
def dis_fn(df, channeltype):
    print(df.groupby(channeltype)[channeltype].count())
    df[channeltype].value_counts().plot(kind='bar')
dis_fn(first_thousand, 'channeltype')


# In[6]:


#6. Load only the top 1000 records of the original 4000 into a separate CSV file.
first_thousand.to_csv('Youtubedata-1000.csv')


# In[8]:


#7. Print saved first 1000 record in a seperate csv file.
df1 = pd.read_csv('./youtubedata-1000.csv')
df1


# In[ ]:




