#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Ques 1) Write a Python program to Extract Unique values dictionary values?


# In[2]:


def extract_unique_values(dictionary):
    unique_values = set()
    for value in dictionary.values():
        if isinstance(value, list) or isinstance(value, set):
            unique_values.update(value)
        else:
            unique_values.add(value)
    return unique_values


# In[3]:


my_dict = {
    'key1': [1, 2, 3],
    'key2': [2,4,5,6] }

extract_unique_values(my_dict)


# In[4]:


# Ques 2) Write a Python program to find the sum of all items in a dictionary?


# In[5]:


def sum_items(dic):
    return sum(dic.values())


# In[6]:


di1 = {'num' : 1,
      "num1" : 1}

sum_items(di1)


# In[7]:


# Ques 3) Write a Python program to Merging two Dictionaries?


# In[8]:


def mer_dic(dic1, dic2):
    return dic1 | dic2


# In[9]:


dict_1 = {1: 'a', 2: 'b'}
dict_2 = {3: 'c', 4: 'd'}

mer_dic(dict_1, dict_2)


# In[10]:


# Ques 4) Write a Python program to convert key-values list to flat dictionary?


# In[11]:


def convert_to_flat_dict(key_value_list):
    flat_dict = {}
    for key, value in key_value_list:
        if isinstance(value, dict):
            nested_dict = convert_to_flat_dict(value.items())
            for nested_key, nested_value in nested_dict.items():
                flat_dict[f'{key}.{nested_key}'] = nested_value
        else:
            flat_dict[key] = value
    return flat_dict


# In[12]:


key_value_list = [
    ('name', 'sameer'),
    ('age', 20),
    ('address', {
        'street': '6, Vijay Vihar',
        'city': 'Delhi',
        'country': 'India'
    })]


convert_to_flat_dict(key_value_list)


# In[13]:


# Ques 5) Write a Python program to insertion at the beginning in OrderedDict?


# In[14]:


from collections import OrderedDict

# Function to insert element at the beginning
def insert_at_beginning(ordered_dict, key, value):
    ordered_dict[key] = value
    ordered_dict.move_to_end(key, last=False)


# In[15]:


ordered_dict = OrderedDict()

#insert elements
ordered_dict['apple'] = 3
ordered_dict['banana'] = 5
ordered_dict['orange'] = 2

# Insert an element at the beginning
insert_at_beginning(ordered_dict, 'grape', 4)

# Print the updated OrderedDict
print(ordered_dict)


# In[16]:


# Ques 6) Write a Python program to check order of character in string using OrderedDict()?


# In[17]:


from collections import OrderedDict

def check_character_order(string):
    char_dict = OrderedDict()

    # Iterate through the characters in the string
    for char in string:
        if char not in char_dict:
            char_dict[char] = None

    for char in string:
        if char in char_dict and char_dict[char] is None:
            char_dict[char] = len(char_dict)

    values = list(char_dict.values())
    return values == sorted(values)


# In[18]:


string1 = "hello"
print(check_character_order(string1)) 

string2 = "world"
print(check_character_order(string2))  


# In[19]:


# Ques 7) Write a Python program to sort Python Dictionaries by Key or Value?


# In[20]:


def sort_dict_by_key(dictionary):
    sorted_dict = dict(sorted(dictionary.items(), key=lambda item: item[0]))
    return sorted_dict

def sort_dict_by_value(dictionary):
    sorted_dict = dict(sorted(dictionary.items(), key=lambda item: item[1]))
    return sorted_dict


# In[21]:


my_dict = {'apple': 3, 'banana': 1, 'orange': 2}


sorted_by_key = sort_dict_by_key(my_dict)
print("Sorted by Key :", sorted_by_key)


sorted_by_value = sort_dict_by_value(my_dict)
print("Sorted by Value:", sorted_by_value)

