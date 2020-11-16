#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
arr=np.arange(2,50,3)
print(arr)


# In[2]:


import numpy as np
list1=[]
print("Enter your 5 numbers in your 1st list:")
for i in range(5):
    n=int(input())
    list1.append(n)
a=np.array(list1)
list2=[]
print("Enter your 5 elements in your 2nd list:")
for i in range(5):
    m=int(input())
    list2.append(m)
b=np.array(list2)
c=np.concatenate([a, b])
print("After Concatination:\n",c)
d=np.sort(c)
print("Your sorted array:\n",d)


# In[3]:


import numpy as np
arr=np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12],[13,14,15]])
print(arr)
print("No. of dimensions of the given array is: ", arr.ndim)
print("Size of given array is: ", arr.size)


# In[4]:


import numpy as np
print("****** Converting 1-D array into 2D array******")
print()
#we can use np.newaxis to increase the dimension of one of the arrays so that NumPy can broadcast.
print("---By using 'np.newaxis' Method---\n")
# 1D array
arr = np.arange(4)
print(arr)
print("Shape of the Array: ",arr.shape)
# make it as row vector by inserting an axis along first dimension
row_vec = arr[np.newaxis, :]     # arr[None, :]
print("Row Vector:")
print("Shape of the array: ",row_vec.shape)
# make it as column vector by inserting an axis along second dimension
col_vec = arr[:, np.newaxis]     # arr[:, None]
print("Column Vector:")
print("Shape of the array: ",col_vec.shape)
print()
#There is another very similar functionality in NumPy: np.expand_dims, which can also be used to insert one dimension:
print("---By Using 'np.expand_dims' Method---\n")
a = np.arange(10)
print(a)
print(np.expand_dims(a, 1))  # like a[:, np.newaxis]
print(np.expand_dims(a, 0))
print()
print("---By Using 'reshape' Method---")
x1 = np.arange(1,10)
print(x1)
print(x1.shape)
print("Dimension: ",x1.ndim)
x1=np.arange(1,10).reshape(3,3)
print(x1)
print(x1.shape)
print("Dimension: ",x1.ndim)


# In[5]:


import numpy as np
a = np.array([[1, 2],
              [3, 4]])
b = np.array([[5, 6],
              [7, 8]])
print("Vertical stacking:\n", np.vstack((a, b)))
print("\nHorizontal stacking:\n", np.hstack((a, b)))


# In[6]:


import numpy as np
arr = np.array([11, 11, 12, 13, 14, 15, 16, 17, 12, 13, 11, 14, 18])
print('Original Numpy Array:\n ', arr)
uniqueValues, occurCount = np.unique(arr, return_counts=True)
print('Unique Values :\n ',uniqueValues)
print("Occurrence Count :\n ", occurCount)
print('Unique Values along with occurrence Count')
listOfUniqueValues = zip(uniqueValues, occurCount)
for elem in listOfUniqueValues:
   print(elem[0] , ' Occurs : ' , elem[1], ' times')


# In[ ]:




