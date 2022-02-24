#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

import warnings
warnings.filterwarnings('ignore')


# In[7]:


data=pd.read_csv('https://raw.githubusercontent.com/dmachlanski/CE888_2022/main/project/data/jobs.csv')
data.head()


# In[8]:


data.shape


# In[9]:


data.info()


# In[10]:


data.describe()


# In[11]:


data.dtypes


# In[12]:


data.columns


# In[13]:


cat_columns= ['x3','x4','x5','x6','x14','x15','x16','t','y','e']


# In[14]:


plt.figure(figsize=(19,10))
for i, column in zip(range(1,11), cat_columns):
    plt.subplot(2,5,i)
    plt.subplots_adjust(left = 0.1,
                       bottom = 0.1,
                       right = 0.9,
                       top = 0.9,
                       wspace = 0.4,
                       hspace = 0.4)
    sns.countplot(data[column])
    plt.title("Countplot of {}".format(column))
plt.savefig('Countplot_jobs.png')


# In[23]:


num_columns = ['x1','x2','x7','x8','x9','x10','x11','x12','x13','x17']


# In[33]:


plt.figure(figsize=(14,19))
def plot(col):
    sns.displot(data, x = col, binwidth = 1)
    plt.title('Distribution of {}'.format(col))
    plt.show()
    plt.savefig('Distribution of {}'.format(col))
    
for col in num_columns:
        plot(col)


# In[ ]:





# In[ ]:




