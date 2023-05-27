#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Ques 1) Write a Python program to check if the given number is a Disarium Number?


# In[2]:


def is_disarium(num):
    temp = 0
    for i in range(len(str(num))):
        temp += int(str(num)[i]) ** (i + 1)
    return temp == num


# In[3]:


is_disarium(74)


# In[4]:


is_disarium(89)


# In[5]:


# Ques 2) Write a Python program to print all disarium numbers between 1 to 100?


# In[6]:


for i in range(1,101):
    if is_disarium(i) == True:
        print(i)


# In[7]:


# Ques 3) Write a Python program to check if the given number is Happy Number?


# In[8]:


def is_Happy_num(n):
    past = set()
    while n != 1:
        n = sum(int(i)**2 for i in str(n))
        if n in past:
            return False
        past.add(n)
    return True


# In[9]:


is_Happy_num(7)


# In[10]:


is_Happy_num(8)


# In[11]:


# Ques 4) Write a Python program to print all happy numbers between 1 and 100?


# In[12]:


for i in range(1,101):
    if is_Happy_num(i) == True:
        print(i)


# In[13]:


# Ques 5) Write a Python program to determine whether the given number is a Harshad Number?


# In[14]:


def harshad(n):
    if (n>0):
        a = 0
        b = n
        while b > 0:
            a = a +  b % 10
            b = b // 10
        return not n % a


# In[15]:


harshad(12)


# In[16]:


# Ques 6) Write a Python program to print all pronic numbers between 1 and 100?


# In[17]:


def isPronicNumber(ran):   
    for i in range(1,ran+1):
        for j in range(1, i+1):    
            #Checks for pronic number by multiplying consecutive numbers    
            if((j*(j+1)) == i):   
                print(i)


# In[18]:


isPronicNumber(100)

