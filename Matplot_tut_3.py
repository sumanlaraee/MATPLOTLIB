#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt 
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


days=[1, 2, 3, 4, 5, 6, 7]
max_t=[50 , 51, 52, 48, 47, 49, 46]
min_t=[43, 42, 40, 44, 33, 35, 37]
avg_t=[45 , 48, 48, 46, 40, 42, 42]


# In[20]:


# ploting all three graphs in one chart 
plt.xlabel("days")
plt.ylabel("temprature")
plt.title("weather forecating ")
plt.plot(days, max_t, label="max")
plt.plot(days, min_t, label="min")
plt.plot(days, avg_t, label="avg")
plt.legend(loc="upper left", shadow=True , fontsize="large" )  
#you can chnage location of legend its up to uh (loc ="best") where it best fits
plt.grid()


# In[ ]:




