#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Ques 1) Write a Python Program to find sum of array?


# In[2]:


def sum_arr(arr):
    sum_ = 0
    for i in arr:
        sum_ = sum_ + i

    return(sum_)


# In[3]:


arr = [1, 3, 4, 7]
print(sum_arr(arr))


# In[4]:


# Ques 2) Write a Python Program to find largest element in an array?


# In[5]:


def max_ele(arr):
    # initializing the variable with value 0  
    max_ = 0
    
    for i in range(1, len(arr)):
        if arr[i] > max_:
            max_ = arr[i]
    return max_


# In[6]:


arr_ = [10, 3, 4, 20, 9]

print(max_ele(arr_))


# In[7]:


# Ques 3) Write a Python Program for array rotation?


# In[8]:


def reverse(arr):
    reversed_list = arr[::-1]
    return reversed_list

def split_arr(arr, pos):
    p1_arr = arr[0:pos]
    p2_arr = arr[pos:]
    new_arr = p2_arr + p1_arr
    return new_arr


# In[9]:


lis = [1,2,3,4,5]
print("full rotation", reverse(lis))
print("rotation after a position - 2",split_arr(lis, 2))


# In[10]:


# Ques 4) Write a Python Program to Split the array and add the first part to the end?


# In[11]:


def split_arr(arr, pos):
    p1_arr = arr[0:pos]
    p2_arr = arr[pos:]
    new_arr = p2_arr + p1_arr
    return new_arr


# In[12]:


l = [1,2,3,4,5]
print(split_arr(l, 2))


# In[13]:


# Ques 5) Write a Python Program to check if given array is Monotonic?


# In[14]:


def ismonotone(a):
    n=len(a)
    if n==1:
        return True
    else:
        #check for monotone behaviour
        if all(a[i]>=a[i+1] for i in range(0,n-1) or a[i]<=a[i+1] for i in range(0,n-1)):
            return True
        else:
            return False


# In[15]:


A = [6, 5, 4, 2]
print(ismonotone(A))
b = [6, 2, 4, 2]
print(ismonotone(b))
c=[4,3,2]
print(ismonotone(c))
d=[1]
print(ismonotone(d))

