#!/usr/bin/env python
# coding: utf-8

# # Analysis on Uber Data from NYC on April 2014 
# 

# In[1]:


get_ipython().run_line_magic('pylab', 'inline')
import pandas as pd 
import seaborn as sns

# load the CSV file 

data = pd.read_csv("/Users/MD/Downloads/uber-raw-data-apr14.csv");


# In[ ]:





# In[2]:


data.head()


# In[9]:


# convert date time and some usefull columns 

data["Date/Time"]=data["Date/Time"].map(pd.to_datetime)


# In[ ]:





# In[10]:


def get_day_month(dt):
    return dt.day

data["dom"]=data["Date/Time"].map(get_day_month)

def get_weekday(dt):
    return dt.weekday()
data["weekday"]=data["Date/Time"].map(get_weekday)

def get_hour(dt):
    return dt.hour
data["hour"]=data['Date/Time'].map(get_hour)


# In[8]:


data.tail()


# # Analysis 

# Analyse the Day of the month 

# In[7]:


hist(data.dom,bins=30,rwidth=0.8 ,range=(0.5,30.5),color="black")

xlabel('Date of the month ')
ylabel('Frequency')
title('Frequency by DOM - Uber - Apr 2014')


# In[11]:


def count_rows(rows):
    return len(rows)

by_date = data.groupby('dom').apply(count_rows)
by_date


# In[ ]:





# In[12]:


by_date_sorted = by_date.sort_values()
by_date_sorted


# In[13]:


bar(range(1,31),by_date_sorted)
xticks(range(1,31),by_date_sorted.index)
xlabel('Date of the month ')
ylabel('Frequency')
title('Frequency by DOM - Uber - Apr 2014')
("")


# # Analysis by hour 

# In[15]:


hist(data.hour,bins=24,range=(0,25),rwidth=0.8,color="g")
xlabel("Hour ")
ylabel('Frequency ')
xticks(range(-1,24))

("")


# ## Analyse by weekday 

# In[ ]:





# In[16]:


hist(data.weekday,bins=7,range=(-0.5,6.5),rwidth=0.8,color='orange',alpha=.4)
xticks(range(7),'Mon Tue Wed Thu Fri Sat Sun'.split())
("")


# In[ ]:





# In[ ]:





# # Cross analysis (hour & day of week )

# In[17]:


by_cross = data.groupby('weekday hour '.split()).apply(count_rows).unstack()


# In[18]:


by_cross


# In[19]:


sns.heatmap(by_cross,linewidths=.5)
("")


# # By lat and Ion 

# In[20]:


hist(data['Lat'],bins=100,range=(40.5,41));


# In[21]:


hist(data['Lon'],bins=100,range=(-74.1,-73.9));


# In[22]:


hist(data['Lat'],bins=100,range=(40.5,41),color='g',alpha=0.5,label='Longitude');
grid()
legend(loc='upper left')
twiny()
hist(data['Lon'],bins=100,range=(-74.1,-73.9),color='r',alpha=0.5,label='Latitude');
legend(loc="best")


# In[23]:


plot(data["Lat"],'.',ms=20,color="green")
xlim(0,100)


# In[ ]:





# In[ ]:




