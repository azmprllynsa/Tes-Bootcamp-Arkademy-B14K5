
# coding: utf-8

# In[46]:


from collections import Counter
def findDuplicates(string):
    output = Counter(string)
    print('Output :')
    
    for key in output.keys():
        if output.get(key) > 1:
            print(key + " = " + str(output.get(key)))
        if output.get(key) <1:
            print('Output tidak ada yang berulang')


# In[47]:


findDuplicates('nama saya ami')


# In[48]:


findDuplicates('1234')

