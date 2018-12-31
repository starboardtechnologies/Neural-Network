
# coding: utf-8

# #Numpy Basics 

# In[5]:


import numpy as np


# In[ ]:


my_list = [,,]


# In[ ]:


type(np.array(my_list))


# In[ ]:


arr = np.array(my_list) 


# In[ ]:


np.arange(,)


# In[ ]:


np.zeroes()


# In[ ]:


np.zeroes(())


# In[ ]:


np.ones()


# In[ ]:


np.(())


# In[ ]:


np.linspace(,,)


# In[ ]:


np.random.randint(,)


# In[ ]:


np.random.randint(,,(,))


# In[ ]:


np.random.normal


# In[ ]:


np.random.seed(100)

np.random.randint(0,99,10)


# In[ ]:


np.random.seed(100)
arr = np.random.randint(0,99,10)


# In[ ]:


arr


# In[ ]:


arr.max()


# In[ ]:


arr.min()


# In[ ]:


arr.mean()


# In[ ]:


arr.argmax()


# In[ ]:


arr.reshape(,)


# In[ ]:


mat = np.arange(0,100).reshape(10,10) 


# In[ ]:


mat


# In[ ]:


mat[3,3]


# In[ ]:


mat[:,0]


# In[ ]:


mat[3,:]


# In[ ]:


mat[0:3,0:3]


# In[ ]:


mat > 66


# In[ ]:


my_filter = mat > 66


# In[ ]:


mat[my_filter]


# In[ ]:


mat[mat>66]

