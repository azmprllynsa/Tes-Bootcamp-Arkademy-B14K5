
# coding: utf-8

# In[9]:


def usernameValidity(username):
  import re
  unameRegex = re.compile(r'^[a-z._]{8,12}$')
  result = re.match(unameRegex,username)
  if result:
    return True
  else:
    return False


# In[10]:


def passwordValidity(password):
  import re
  passwordRegex = re.compile(r'[a-zA-Z0-9~!@#$%^&*]{9,9}$')
  result = re.match(passwordRegex,password)
  if result:
    return True
  else:
    return False

