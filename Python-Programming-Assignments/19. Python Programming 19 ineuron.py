#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Ques 1) Create a function that takes a string and returns a string in which each character is repeated once.


# In[2]:


def double_char(string):
    double_string = ""
    for char in string:
        double_string += char*2
    return double_string


# In[3]:


double_char("String")


# In[4]:


double_char("Hello World")


# In[5]:


# Ques 2) Create a function that reverses a boolean value and returns the string "boolean expected" if 
# another variable type is given.


# In[6]:


def reverse(value):
    if type(value) == bool:
        return not value
    else:
        return "boolean expected"


# In[7]:


reverse(True)


# In[8]:


reverse(False)


# In[9]:


reverse(0)


# In[10]:


# Ques 3) Create a function that returns the thickness (in meters) of a piece of paper after folding it n
# number of times. The paper starts off with a thickness of 0.5mm.


# In[11]:


def num_layers(folds):
    return str(0.0005 * 2**folds) + "m"


# In[12]:


num_layers(1)


# In[13]:


num_layers(4)


# In[14]:


num_layers(21)


# In[15]:


# Ques 4) Create a function that takes a single string as argument and returns an ordered list containing
# the indices of all capital letters in the string.


# In[16]:


def index_of_caps(input_string):
    capital_indices = [index for index, char in enumerate(input_string) if char.isupper()]
    return capital_indices


# In[17]:


index_of_caps("eDaBiT")


# In[18]:


index_of_caps("eQuINoX")


# In[19]:


# Ques 5) Using list comprehensions, create a function that finds all even numbers from 1 to the given number.


# In[20]:


def find_even_nums(number):
    even_nums = [num for num in range(1,number+1) if num%2==0]
    return even_nums


# In[21]:


find_even_nums(8)


# In[22]:


find_even_nums(4)

