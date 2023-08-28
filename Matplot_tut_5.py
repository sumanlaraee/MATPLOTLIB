#!/usr/bin/env python
# coding: utf-8

# In[1]:


# in previous codes we have seen barchart now we are going to use histogram 
import matplotlib.pyplot as plt 
get_ipython().run_line_magic('matplotlib', 'inline')


# In[9]:


blood_sugar=[100, 20, 49, 145, 133, 198]
# when we are working with histogram we need only single dimension array
plt.hist(blood_sugar, bins=3, rwidth=0.95)
#in histogram there is concept of bins or buckets(range) by default bin =10 and use realtive width to decide width related to bins 


# In[15]:


#so here we are gonna explore more about bins by providing it a range 
plt.hist(blood_sugar, bins=[80, 90, 125, 150] , color="orange", histtype="step")


# In[23]:


#for suppose we have two data samples one for man other for women 
blood_sugar_man=[113, 45, 190, 23, 118, 45, 66, 183, 44, 14, 77]
blood_sugar_women=[110, 55, 127, 82, 149, 33, 76, 116, 34, 87, 187]
plt.xlabel("sugar")
plt.ylabel("no: of patients")
plt.title("blood sugar Analysis")
plt.hist([blood_sugar_man,blood_sugar_women ], color=["green", "orange"], label=["men", "women"], orientation="horizontal")
plt.legend()


# In[ ]:




