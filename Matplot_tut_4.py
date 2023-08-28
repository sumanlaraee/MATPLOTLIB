#!/usr/bin/env python
# coding: utf-8

# In[5]:


import matplotlib.pyplot as plt 
import numpy as np
get_ipython().run_line_magic('matplotlib', 'inline')
 


# In[18]:


company=["google", "microsoft", "insta", "fb"] #i have to convert strings into number so used numpy 
revenue =[90, 139, 86, 27]
profit=[40, 2, 34, 12]


# In[22]:


xposition=np.arange(len(company))
xposition


# In[23]:


plt.bar(yposition, revenue)


# In[24]:


# i have got some values on x axis so i have to convert to company names 
plt.xticks(yposition, company)
plt.xlabel("companies")
plt.ylabel("revenue")
plt.title("usa revenue model")
plt.bar(xposition, revenue ,label="revenue")
plt.bar(xposition, profit ,label="profit")
plt.legend()


# In[27]:


#in upper graph we can see profit is on same bar i wanna generate side by side bar chart 
plt.xticks(yposition, company)
plt.xlabel("companies")
plt.ylabel("revenue")
plt.title("usa revenue model")
plt.bar(xposition-0.2, revenue ,width=0.4 ,label="revenue")
plt.bar(xposition+0.2, profit ,width=0.4 ,label="profit")
plt.legend()


# In[29]:


# we have seen so far is perfect bar chart but some people prefer horizontal barchart
plt.xticks(yposition, company)
plt.xlabel("companies")
plt.ylabel("revenue")
plt.title("usa revenue model")
plt.barh(xposition-0.2, revenue  ,label="revenue")
plt.barh(xposition+0.2, profit  ,label="profit")
plt.legend()


# In[ ]:




