#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Ques 1) Create a function that takes three integer arguments (a, b, c) and returns the amount of integers which are of equal value.


# In[2]:


def equal(a, b, c):
    count = 0
    if a == b == c:
        count = 3
    elif a == b or a == c or b == c:
        count = 2
    return count


# In[3]:


# Examples
equal(3, 4, 1)


# In[4]:


equal(3, 4, 3)


# In[5]:


equal(1, 1, 1)


# In[6]:


# Ques 2) Write a function that converts a dictionary into a list of keys-values tuples.


# In[7]:


def dict_to_list(input_dict):
    return sorted(input_dict.items())


# In[8]:


dict_to_list({"D": 1, "B": 2, "C": 3})


# In[9]:


dict_to_list({"likes": 2, "dislikes": 3, "followers": 10})


# In[10]:


# Ques 3) Write a function that creates a dictionary with each (key, value) pair being the (lower case, upper case) versions of a letter, respectively.


# In[11]:


def mapping(inp_list):
    letter_dict = {}
    for item in inp_list:
        if type(item) == str and len(item) ==1:
            lowercase_letter = item.lower()
            letter_dict[lowercase_letter] = lowercase_letter.upper()
        else:
            raise ValueError("Each element of list much be a integer of length 1")
    return letter_dict


# In[12]:


mapping(["p", "s"])


# In[13]:


mapping(["a", "b", "c"])


# In[14]:


mapping(["a", "v", "y", "z"])


# In[15]:


# Ques 4) Write a function, that replaces all vowels in a string with a specified vowel.


# In[16]:


def vow_replace(input_string, specified_vowel):
    vowels = 'aeiouAEIOU'
    new_string = "".join(specified_vowel if char in vowels else char for char in input_string)
    return new_string


# In[17]:


vow_replace("apple and banana", "i")


# In[18]:


# Ques 5) Create a function that takes a string as input and capitalizes a letter if its ASCII code is even and returns its lower case version if its ASCII code is odd.


# In[19]:


def ascii_capitalize(input_string):
    result = ''
    for char in input_string:
        ascii_code = ord(char)
        if ascii_code % 2 == 0:
            result += char.upper()
        else:
            result += char.lower()
    return result


# In[20]:


ascii_capitalize("to be or not to be!")


# In[21]:


ascii_capitalize("THE LITTLE MERMAID")


# In[22]:


ascii_capitalize("Oh what a beautiful morning.")

