#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Ques 1) Create a function that takes three parameters where:
# - x is the start of the range (inclusive).
# - y is the end of the range (inclusive).
# - n is the divisor to be checked against.
# Return an ordered list with numbers in the range that are divisible by the third parameter n.
# Return an empty list if there are no numbers that are divisible by n. 


# In[2]:


def list_operation(x, y, n):
    num_list = []
    for num in range(x, y+1):
        if num%n==0:
            num_list.append(num)
    return sorted(num_list)


# In[3]:


list_operation(1, 10, 3)


# In[4]:


list_operation(7, 9, 2)


# In[5]:


# Ques 2) Create a function that takes in two lists and returns True if the second list follows the first list by one element, 
# and False otherwise. In other words, determine if the second list is the first list shifted to the right by 1.


# In[6]:


def simon_says(list1:list, list2:list):
    if len(list1) != len(list2):
        raise ValueError("Length of boht lists should be same")
    elif len(list1) < 2 or len(list2) < 2:
        raise IndexError("Minimum length of list should be 2")
    else:
        if list1[:-1] == list2[1:]:
            return True
        else:
            return False


# In[7]:


simon_says([1,2], [5,1])


# In[8]:


# Ques 3) A group of friends have decided to start a secret society. The name will be the first letter of each of their names, 
# sorted in alphabetical order. Create a function that takes in a list of names and returns the name of the secret society.


# In[9]:


def society_name(name_list):
    for name in name_list:
        if type(name) != str:
            raise ValueError("All elements of list should be string")
    society_name = ''.join(sorted(name[0] for name in name_list))
    return society_name


# In[10]:


society_name(["Adam", "Sarah", "Malcolm"])


# In[11]:


society_name(["Harry", "Newt", "Luna", "Cho"])


# In[12]:


# Ques 4) An isogram is a word that has no duplicate letters. Create a function that takes a string and
# returns either True or False depending on whether or not it's an "isogram".


# In[13]:


def is_isogram(string):
    string = string.lower()
    set_string = set()
    
    for letter in string:
        if letter in set_string:
            return False
        else:
            set_string.add(letter)
    return True


# In[14]:


is_isogram("Algorism")


# In[15]:


is_isogram("Consecutive")


# In[16]:


# Ques 5) Create a function that takes a string and returns True or False, depending on whether the characters are in order or not.


# In[17]:


def is_in_order(input_string):
    return input_string == ''.join(sorted(input_string))


# In[18]:


is_in_order("abc")


# In[19]:


is_in_order("edabit")

