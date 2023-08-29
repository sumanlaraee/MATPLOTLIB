#!/usr/bin/env python
# coding: utf-8

# In[2]:


#for much piece / pie if for which expense 
import matplotlib.pyplot as plt 
get_ipython().run_line_magic('matplotlib', 'inline')


# In[3]:


exp_val=[400, 600, 300, 410, 250]
exp_labels=["Home rent", "food", "phone/internet bill", "car", "other utilities"]


# In[4]:


plt.pie(exp_val, labels=exp_labels)


# In[12]:


plt.axis("equal")
plt.pie(exp_val, labels=exp_labels, radius=1, autopct="%0.2f%%", shadow=True , explode=[0,0.2, 0, 0, 0], startangle=180)
plt.show()


# In[ ]:




