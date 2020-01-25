
# coding: utf-8

# In[18]:


def count_handshake(input):
    result=0
    if input < 1:
        return 0
    else:
        for i in range(input):
            people= input-1
            print(people)
            for j in range(people-i):
                result +=1
        return result

