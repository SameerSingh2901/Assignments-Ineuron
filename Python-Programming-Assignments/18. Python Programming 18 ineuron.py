#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Ques 1) Create a function that takes a list of non-negative integers and strings and return a new list without the strings.


# In[2]:


def filter_list(list_:list):
    int_list = []
    for item in list_:
        if type(item) == int:
            int_list.append(item)
    return int_list


# In[3]:


filter_list([1, 2, "a", "b"])


# In[4]:


filter_list([1, 2, "aasf", "1", "123", 123])


# In[5]:


# Ques 2) The 'Reverser' takes a string as input and returns that string in reverse order, with the opposite case.


# In[6]:


def reverse(string):
    return string[::-1].swapcase()


# In[7]:


reverse("Hello World")


# In[8]:


reverse("ReVeRsE")


# In[9]:


# Ques 3) Your task is to unpack the list writeyourcodehere into three variables, being first, middle, and last, 
# with middle being everything in between the first and last element. Then print all three variables.


# In[10]:


def list_unpack(list_):
    first = list_[0]
    middle = list_[1:-1]
    last = list_[-1]
    return f"First = {first}, Middle = {middle}, Last = {last}"


# In[11]:


list_unpack([1,2,3,4,5,6,7,8])


# In[12]:


list_unpack([2,5,62,5,6,36,6])


# In[13]:


# Ques 4) Write a function that calculates the factorial of a number recursively.


# In[14]:


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


# In[15]:


factorial(5)


# In[16]:


factorial(3)


# In[17]:


# Ques 5) Write a function that moves all elements of one type to the end of the list.


# In[18]:


def move_to_end(list_, element):
    result_list = [ele for ele in list_ if ele != element]
    count = list_.count(element)
    result_list.extend([element]*count)
    return result_list


# In[19]:


move_to_end([1, 3, 2, 4, 4, 1], 1)


# In[20]:


move_to_end([7, 8, 9, 1, 2, 3, 4], 9)

