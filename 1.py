
# coding: utf-8

# In[16]:


import json


# In[17]:


def myprofile():
    list_school = [{"name_school" : "SDN 13 Pringsewu", "year_in" : 2001, "year_out" : 2007, "major" : None},
                     {"name_school" : "SMPN 1 Pagelaran", "year_in" : 2007, "year_out" : 2010,"major" : None},
                     {"name_school" : "SMK Widya Yahya Gadingrejo", "year_in" : 2010, "year_out" : 2013,"major" : "Teknik Komputer Jaringan"},
                     {"name_school" : "Universitas Lampung", "year_in" : 2013, "year_out" : 2019, "major" : "Physics"}
                  ]
    skill_level = [{'skill name' : 'Python', 'level' : 'beginner'},
                   {'skill name' : 'C++', 'level' : 'beginner'}
                  ]
    Data = {
        'name' : 'Azmi Prilly Naisa',
        'age' : 23,
        'address' : 'Jl. Raya Pagelaran no. 369 Patoman II kec. Pagelaran, kab. Pringsewu, Lampung',
        'hobbies' : ['Design Graphic', 'swimming'],
        'is_married' : False,
        'list_school' : list_school,
        'skills' : skill_level,
        'interest_in_coding' : True
    }
    return Data


# In[18]:


with open('soal_no_1.json', 'w') as write_file:
    json.dump(myprofile(), write_file)

