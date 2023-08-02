#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Ques 1) Create a function that takes a number as an argument and returns True or False depending on whether the number is 
# symmetrical or not. A number is symmetrical when it is the same as its reverse.


# In[2]:


def is_symmetrical(number):
    number_str = str(number)
    return number_str == number_str[::-1]


# In[3]:


is_symmetrical(7227)


# In[4]:


is_symmetrical(9939)


# In[5]:


# Ques 2) Given a string of numbers separated by a comma and space, return the product of the numbers.


# In[6]:


def multiply_nums(num_string):
    num_list = num_string.split(", ")
    numbers = [int(num) for num in num_list]
    product = 1
    for num in numbers:
        product *= int(num)
    return product


# In[7]:


multiply_nums("2, 3, 5")


# In[8]:


# Ques 3) Create a function that squares every digit of a number.


# In[9]:


def square_digits(number):
    squared = ""
    for i in str(number):
        square = int(i)**2
        squared += str(square)
    return int(squared)


# In[10]:


square_digits(9119)


# In[11]:


square_digits(3212)


# In[12]:


# Ques 4) Create a function that sorts a list and removes all duplicate items from it.


# In[13]:


def setify(input_list):
    sorted_list = sorted(input_list)
    unique_list = list(set(sorted_list))
    return unique_list


# In[14]:


setify([1, 3, 3, 5, 5])


# In[15]:


setify([5, 7, 8, 9, 10, 15])


# In[16]:


# Ques 5) Create a function that returns the mean of all digits.


# In[17]:


def mean(number):
    count = 0
    sum_ = 0
    for num in str(number):
        count +=1
        sum_ = sum_ + int(num)
    return sum_/count


# In[18]:


mean(42)


# In[19]:


mean(12345)


# In[20]:


mean(666)

