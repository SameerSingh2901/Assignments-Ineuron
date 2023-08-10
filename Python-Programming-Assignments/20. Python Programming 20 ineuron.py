#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Ques 1) Create a function that takes a list of strings and integers, and filters out the list so that it returns 
# a list of integers only.


# In[2]:


def filter_list(list_:list):
    int_list = []
    for item in list_:
        if type(item) == int:
            int_list.append(item)
    return int_list


# In[3]:


filter_list([1, 2, 3, "a", "b", 4])


# In[4]:


filter_list(["Nothing", "here"])


# In[5]:


# Ques 2) Given a list of numbers, create a function which returns the list but with each element's index in the list added 
# to itself. This means you add 0 to the number at index 0, add 1 to the number at index 1, etc...


# In[6]:


def add_indexes(list_):
    for index,number in enumerate(list_):
        list_[index] = index+number
    return list_


# In[7]:


add_indexes([0, 0, 0, 0, 0])


# In[8]:


add_indexes([1, 2, 3, 4, 5])


# In[9]:


# Ques 3) Create a function that takes the height and radius of a cone as arguments and returns the
# volume of the cone rounded to the nearest hundredth. See the resources tab for the formula.


# In[10]:


def cone_volume(height, radius):
    volume = 3.14159 * radius**2 * height/3
    return round(volume, 2)


# In[11]:


cone_volume(3, 2)


# In[12]:


cone_volume(15, 6)


# In[13]:


# Ques 4) This Triangular Number Sequence is generated from a pattern of dots that form a triangle.
# The first 5 numbers of the sequence, or dots, are:
# 1, 3, 6, 10, 15
# This means that the first triangle has just one dot, the second one has three dots, the third one has 6 dots and so on.
# Write a function that gives the number of dots with its corresponding triangle number of the sequence.


# In[14]:


def triangle(n):
    if n <= 0:
        raise ValueError("Input should be a positive integer.")

    dots = n * (n + 1) // 2
    return dots


# In[15]:


triangle(6)


# In[16]:


triangle(215)


# In[17]:


# Ques 5) Create a function that takes a list of numbers between 1 and 10 (excluding one number) and returns the missing number.


# In[18]:


def missing_num(num_list):
    range_list = [1,2,3,4,5,6,7,8,9,10]
    for i in num_list:
        if i in range_list:
            range_list.remove(i)
    return int(range_list[0]) # because only one number is to be excluded and result should be in int


# In[19]:


missing_num([1, 2, 3, 4, 6, 7, 8, 9, 10])


# In[20]:


missing_num([7, 2, 3, 6, 5, 9, 1, 4, 8])

