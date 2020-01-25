
# coding: utf-8

# In[18]:


def findhighestProfit(A):
    datasahamptX = 0
    profit = 0
    for i in range(0, len(A)):
        for j in range (i + 1, len(A)):
            datasahamptX = max(datasahamptX, A[j] - A[i])
    
    if datasahamptX > profit:
      return datasahamptX
    else:
      return 'Tidak bisa mendapatkan profit pada hari-hari ini'


# In[19]:


prices = (29, 27, 11, 3)
print(findhighestProfit(prices))


# In[20]:


prices = [10, 2, 11, 20, 3, 5]
print(findhighestProfit(prices))

