#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Ques 1) Write a Python Program to Add Two Matrices?


# In[2]:


def add_mat(mat1, mat2):
    if len(mat1) == len(mat2) and len(mat1[0]) == len(mat2[0]):
        sum_matrix = [[0] * len(mat1[0]) for i in range(len(mat1))]
        for i in range(len(mat1)):
           # iterate through columns
           for j in range(len(mat1[0])):
                sum_matrix[i][j] = mat1[i][j] + mat2[i][j]
    else:
        return "Matrix with different dimentions cannot be added"
    return sum_matrix


# In[3]:


x = [[1,1,1,1],
    [1,1,1,1],
    [1,1,1,1]]

Y = [[2,2,2,2],
    [2,2,2,2],
    [2,2,2,2]]

add_mat(x,Y)


# In[4]:


# Ques 2) Write a Python Program to Multiply Two Matrices?


# In[5]:


def mul_mat(mat1, mat2):
    if len(mat1[0]) == len(mat2):
        matrix = [[0] * len(mat2[0]) for i in range(len(mat1))]
        # iterate through rows of X
        for i in range(len(mat1)):
           # iterate through columns of Y
           for j in range(len(mat2[0])):
               # iterate through rows of Y
               for k in range(len(mat2)):
                    matrix[i][j] += mat1[i][k] * mat2[k][j]
    else:
        print("Matrices cannot be multiplied")
    return matrix


# In[6]:


# take a 3x3 matrix
A = [[12, 7, 3],
    [4, 5, 6],
    [7, 8, 9]]

# take a 3x4 matrix
B = [[5, 8, 1, 2],
    [6, 7, 3, 0],
    [4, 5, 9, 1]]

mul_mat(A,B)


# In[7]:


# Ques 3) Write a Python Program to Transpose a Matrix?


# In[8]:


def transpose_mat(mat):
    result = [[0] * len(mat) for i in range(len(mat[0]))]
    # iterate through rows
    for i in range(len(mat)):
       # iterate through columns
       for j in range(len(mat[0])):
            result[j][i] = mat[i][j]
    return result


# In[9]:


x = [[12,7],
    [4 ,5],
    [3 ,8]]

print(transpose_mat(x))


# In[10]:


# Ques 4) Write a Python Program to Sort Words in Alphabetic Order?


# In[11]:


def word_sort(string):
    words = [word.lower() for word in string.split()]
    words.sort()
    return  words


# In[12]:


string = input("Enter a String : ")

print(word_sort(string))


# In[13]:


# Ques 5) Write a Python Program to Remove Punctuation From a String?


# In[14]:


def rem_punctuation(string):
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    no_punct = ""
    for char in string:
        if char not in punctuations:
            no_punct = no_punct + char
    return no_punct


# In[15]:


string = input("Enter a String : ")

print(rem_punctuation(string))

