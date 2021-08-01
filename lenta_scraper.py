#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
from bs4 import BeautifulSoup


# In[2]:


response = requests.get("https://lenta.ru/")


# In[3]:


soup = BeautifulSoup(response.text, 'html.parser')


# In[4]:


soup.select('.titles')
titles = soup.select('.titles')
for title in titles:
    print (title.text.strip())


# In[5]:


soup.select('.rubric')
rubrics = soup.select('.rubric')
for rubric in rubrics:
    print (rubric.text.strip())


# In[6]:


len(titles)


# In[7]:


len(rubrics)


# In[9]:


stories = soup.find_all(class_ = 'item article')
for story in stories:
    print ('-----')
    print(story.select_one('.titles').text.strip())
    print(story.select_one('.titles').get('href'))
    try:
        print(story.select_one('.rubric').text.strip())
    except:
        print ('NaN')


# In[10]:


len(stories)


# In[11]:


stories = soup.find_all(class_ = 'item article')
rows = []
for story in stories:
    row = {}
    row['title'] = story.select_one('.titles').text.strip()
    row['href']= story.select_one('.titles').get('href')
    try:
        row['rubric']=story.select_one('.rubric').text.strip()
    except:
        pass
    rows.append(row)
rows


# In[12]:


import pandas as pd
df_lenta = pd.DataFrame(rows)
df_lenta


# In[13]:


df_lenta.to_csv('df_lenta.csv', index=False)

import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

message = Mail(
    from_email='FROM_EMAIL',
    to_emails='TO_EMAIL',
    subject='Sending with Twilio SendGrid is Fun',
    html_content='<strong>and easy to do anywhere, even with Python</strong>')
try:
    sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
    response = sg.send(message)
    print(response.status_code)
    print(response.body)
    print(response.headers)
except Exception as e:
    print(e.message)