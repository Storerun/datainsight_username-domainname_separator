#!/usr/bin/env python
# coding: utf-8

# In[ ]:


a=input("PLEASE ENTER YOUR EMAIL: " )
if '@' in a:
    user_name= a.split('@')[0]
    dormain_name= a.split('@')[1]
    print("your username is: "+ user_name+ " and your domain name is: " + dormain_name)
else:
    print("your email is not valid.")

    


# In[ ]:




