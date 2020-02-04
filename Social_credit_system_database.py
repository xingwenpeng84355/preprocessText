#!/usr/bin/env python
# coding: utf-8

# In[1]:


#import nltk
#nltk.__version__

#get_ipython().magic(u'pwd')
#get_ipython().magic(u'cd "/Users/wayne/Dropbox/UMass Research/Social Credit System/China_SCS"')

import pandas as pd  #Pandas使用一个二维的数据结构DataFrame来表示表格式的数据，相比较于Numpy，
#Pandas可以存储混合的数据结构，同时使用NaN来表示缺失的数据，而不用像Numpy一样要手工处理缺失的数据，并且Pandas使用轴标签来表示行和列
import os
import glob
from glob import glob as gg
import re, datetime

from collections import defaultdict

import nltk
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import SpaceTokenizer
from nltk.tokenize import sent_tokenize
from nltk.corpus import stopwords

#from functools import partial

import re


# In[2]:


df = open("sample for 1 month.txt").read().split("文章编号:")# 通过文章编号进行切片


# In[3]:


data = pd.DataFrame(df) #
data.columns = ['raw_text']
#data["title"] = data["raw_text"].apply(lambda x: x.split("\n\n\n\n\n")[1])
data = data[~data['raw_text'].isnull()] 


# In[4]:


for index, row in data[0:15].iterrows():
    try:
        data.loc[index, 'title'] = data.loc[index, 'raw_text'].split("\n\n\n\n\n")[1].strip()
        data.loc[index, 'title'] = data.loc[index, 'title'].replace("\n\n\n  \n-----------------------------------------------------------------------------", "")
        data.loc[index, 'source'] = data.loc[index, 'title'].split("-")[0].strip()
        data.loc[index, 'link'] = data.loc[index, 'raw_text'].split("\n\n\n\n\n")[2].strip()
        data.loc[index, 'link'] = data.loc[index, 'link'].replace("文字快照：", "")
        data.loc[index, 'content'] = data.loc[index, 'raw_text'].split("\n\n\n\n\n")[3].strip()
        #data.loc[index, 'content'] = data.loc[index, 'content'].str.strip()
        data.loc[index, 'date'] = datetime.datetime.strptime(re.search('\d{4}-\d{2}-\d{2}', data.loc[index, 'title']).group(), '%Y-%m-%d').date()
    except: pass


# In[5]:


data.head(3)



# In[ ]:

data.to_csv('/Users/xingwenpeng/Desktop/nlp/test.csv');



# In[ ]:




