#!/usr/bin/env python
# coding: utf-8

# In[303]:


import pandas as pd
import numpy as np


# In[304]:


df1=pd.read_csv('food_data.csv', encoding= 'unicode_escape')


# In[305]:


df1.head()


# In[306]:


import datetime


# In[307]:


today = datetime.date.today()


# In[308]:


today


# In[309]:


ts=pd.Timestamp(today)


# In[310]:


ts


# In[311]:


df1['use by'] = pd.to_datetime(df1['use by'], errors='coerce')


# In[312]:


df1.info()


# In[313]:


ind=df1['use by'].index


# In[314]:


ind


# In[315]:


#df1['use by'] = df1['use by'].dt.strftime('%d/%m/%Y')


# In[316]:


df1.info()


# In[317]:


df1.head()


# In[318]:


l=[]
for x in df1['use by']:
    l.append((x-ts))


# In[319]:


l


# In[320]:


z=pd.Series(l)


# In[321]:


z


# In[322]:


df1['diff']=z


# In[323]:


df1.head()


# In[324]:


df1=df1.sort_values(by='diff',ascending=True)


# In[325]:


df1.head()


# In[ ]:




