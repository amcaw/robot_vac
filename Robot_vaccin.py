#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


df = pd.read_csv('https://epistat.sciensano.be/Data/COVID19BE_VACC.csv')


# In[3]:


df = pd.pivot_table(df, index = 'DATE', columns = 'DOSE', values = 'COUNT', aggfunc = 'sum')


# In[4]:


print.head()


# In[5]:


head()


# In[6]:


df.head()


# In[7]:


df['CumuleA'] = df['A'].cumsum().map('{0:g}'.format)
df['CumuleB'] = df['B'].cumsum().map('{0:g}'.format)
df['CumuleC'] = df['C'].cumsum().map('{0:g}'.format)


# In[8]:


df.head()


# In[9]:


df["A"] = df['CumuleA'] + df['CumuleC']
df["B"] = df['CumuleB'] + df['CumuleC']


# In[10]:


df.head()


# In[11]:


df.tail()


# In[ ]:


df.to_csv("/result.csv")

