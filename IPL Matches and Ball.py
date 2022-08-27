#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns


# In[3]:


match_data = pd.read_csv("C:/Users/RAHUL/Desktop/python files/IPL Matches 2008-2020.csv")
ball_data = pd.read_csv("C:/Users/RAHUL/Desktop/python files/IPL Ball-by-Ball 2008-2020.csv")


# In[4]:


match_data.head()


# In[5]:


ball_data.head()


# In[6]:


match_data.isnull().sum()


# In[7]:


match_data.shape


# In[8]:


match_data.columns


# In[9]:


print('matches played so far= ',match_data.shape[0])


# In[10]:


print('\n Cities played at= ', match_data['city'].unique())


# In[11]:


print(' Total number of Teams participated= ',match_data['team1'].unique())


# In[12]:


match_data['Season'] = pd.DatetimeIndex(match_data['date']).year
match_data.head()


# In[13]:


match_per_season = match_data.groupby(['Season'])['id'].count().reset_index().rename(columns = {'id': 'matches'})
match_per_season


# In[81]:


#Plot to visualise the no. of matches held every season

sns.set_style('darkgrid')
sns.countplot(x='matches', data=match_per_season)
plt.title('No. of matches held every season\n')
plt.xlabel('\nSeason')
plt.ylabel('No. of matches held\n')
plt.show()


# In[14]:


#total player of the match

match_data['player_of_match'].value_counts()


# In[15]:


#histogram on player of the match vs players getting the player of the match

plt.figure(figsize=(8,5))
plt.bar(list(match_data['player_of_match'].value_counts()[0:5].keys()),list(match_data['player_of_match'].value_counts()[0:5]),color="g")
plt.show()


# In[16]:


match_data['result'].value_counts()


# In[17]:


#total teams winning the toss

match_data['toss_winner'].value_counts()


# In[18]:


#Extracting the records where the team Batting first won the match

batting_first = match_data[match_data['result']!= 'runs']


# In[19]:


batting_first.head()


# In[20]:


result_difference = match_data['result_margin']


# In[21]:


result_difference.head()


# In[22]:


batting_second = match_data[match_data['result']!= 'wickets']


# In[23]:


batting_second.head()


# In[24]:


#Histogram on Result Margin

plt.figure(figsize=(5,7))
plt.hist(match_data['result_margin'])
plt.show()


# In[25]:


ball_data['id'].unique()


# In[26]:


ball_data.head()


# In[27]:


match_1 = ball_data[ball_data['id']==335982]


# In[28]:


match_1.head()


# In[29]:


match_1.shape


# In[30]:


kkr = match_1[match_1['inning']==1]


# In[31]:


#Runs distributed on 0s,singles,4s,6s and Doubles by KKR

kkr['batsman_runs'].value_counts()


# In[32]:


kkr['dismissal_kind'].value_counts()


# In[33]:


#2nd Innings of RCB Batting

rcb = match_1[match_1['inning']==2]


# In[34]:


rcb.head()


# In[35]:


#Runs distributed on 0s,singles,4s,6s and Doubles by RCB

rcb['batsman_runs'].value_counts()


# In[36]:


#Type of Wickets fell

rcb['dismissal_kind'].value_counts()


# In[37]:


winner_team= match_data['winner'].value_counts()


# In[38]:


winner_team


# In[59]:


# plot for the above teams where we are able to see the percentage of teams winning

colors = sns.color_palette('bright')[0:10]
plt.pie(winner_team, labels = winner_team, colors = colors, autopct='%.0f%%')
plt.show()

# we can observe that 120 = Mumbai Indians


# In[42]:


# venues where the matches held

venues= match_data['venue'].value_counts().rename_axis('stadium').reset_index(name='count')
venues


# In[80]:


#plot where to observe matches played vs stadiums

sns.set_style('darkgrid')
sns.barplot(x= 'stadium', y ='count',data = venues)


# In[ ]:




