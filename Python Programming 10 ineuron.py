#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Ques 1) Write a Python program to find sum of elements in list?


# In[2]:


def list_sum(li):
    sum_ = 0
    for i in li:
        sum_ = sum_+i
    return sum_


# In[3]:


li = [1,2,3,4,5]
print(list_sum(li))


# In[4]:


# Ques 2) Write a Python program to Multiply all numbers in the list?


# In[5]:


def list_mul(li):
    mul_ = 1
    for i in li:
        mul_ = mul_*i
    return mul_


# In[6]:


li_1 = [1,2,3,4,5,10]
print(list_mul(li_1))


# In[7]:


# Ques 3) Write a Python program to find smallest number in a list?


# In[8]:


def small(li):
    sm = li[0]
    for i in li:
        if i<sm:
            sm = i
    return "Smalles number of the list is - ", sm


# In[9]:


li_2  = [5,3,7]
print(small(li_2))


# In[10]:


# Ques 4) Write a Python program to find largest number in a list?


# In[11]:


def large(li):
    lg = li[0]
    for i in li:
        if i>lg:
            lg = i
    return "Largest number of the list is - ", lg


# In[12]:


li_3 = [2,4,2,45,6,3]
print(large(li_3))


# In[13]:


# Ques 5) Write a Python program to find second largest number in a list?


# In[14]:


def sec_large(li_):
    li_.sort()
    return li_[-1]


# In[15]:


li_4 = [1,5,2,4,3,6]

print(sec_large(li_4))


# In[16]:


# Ques 6) Write a Python program to find N largest elements from a list?


# In[17]:


def sec_num_large(li_,n):
    li_.sort(reverse=True)
    return li_[:n]


# In[18]:


li_5 = [1,5,2,4,3,6]

print(sec_num_large(li_5,5))


# In[19]:


# Ques 7) Write a Python program to print even numbers in a list?


# In[20]:


def pr_even(list_):
    for num in list_:
        if num % 2 == 0:
            print(num)


# In[21]:


li_6 = [1,2,3,4,5,6,7,8]

pr_even(li_6)


# In[22]:


# Ques 8) Write a Python program to print odd numbers in a List?


# In[23]:


def pr_odd(list_):
    for num in list_:
        if num % 2 != 0:
            print(num)


# In[24]:


pr_odd(li_6)


# In[25]:


# Ques 9) Write a Python program to Remove empty List from List?


# In[26]:


def rem_emp_list(li):
    list_ = [ele for ele in li if ele != []]
    return list_


# In[27]:


test_list = [5, 6, [], 3, [], [], 9]

rem_emp_list(test_list)


# In[28]:


# Ques 10) Write a Python program to Cloning or Copying a list?


# In[29]:


def copy_list(li):
    copy_l = []
    for i in li:
        copy_l.append(i)
    return copy_l


# In[30]:


test_list2 = [1,4,7,3,6,8,4]
copy_list(test_list2)


# In[31]:


# Ques 11) Write a Python program to Count occurrences of an element in a list?


# In[32]:


def count_ele(lst, x):
    count = 0
    for ele in lst:
        if (ele == x):
            count = count + 1
    return count


# In[33]:


lst = [8, 6, 8, 10, 8, 20, 10, 8, 8]
x = 8
print(f'{x} has occurred {count_ele(lst, x)} times')

