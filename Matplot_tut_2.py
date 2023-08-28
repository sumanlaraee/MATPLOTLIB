#!/usr/bin/env python
# coding: utf-8

# In[22]:


import matplotlib.pyplot as plt 
get_ipython().run_line_magic('matplotlib', 'inline')


# In[23]:


x=[1, 2, 3, 4, 5, 6]
y=[40, 30, 60, 10, 23, 44]


# In[28]:


# here we are going to use list of format string that are supported check (matplotlib.org )
plt.plot(x, y, "g+--")    #order of g + and -- doesnt matter it works anyway


# In[31]:


#if we dont wanna use string literals we can use keywords 
plt.plot(x, y, color="yellow", marker="d", markersize=20)  #we can use hexadecimal for colors 


# In[34]:


plt.plot(x, y, color="red", marker="+", alpha=0.5) #alpha control visibility its transparency is between 0 and 1 


# In[ ]:




