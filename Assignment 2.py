#!/usr/bin/env python
# coding: utf-8

# In[ ]:


l=[]
for i in range(0,10):
    n=int(input())
    if(n%2==0):
        l.append(n)
print(l)

Exmp 1:Using if with List Comprehension
number_list = [ x for x in range(20) if x % 2 == 0]
print(number_list)

When we run the above program, the output will be:

[0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
The list ,number_list, will be populated by the items in range from 0-19 if the item's value is divisible by 2.

Exmp 2: Nested IF with List Comprehension
num_list = [y for y in range(100) if y % 2 == 0 if y % 5 == 0]
print(num_list)
When we run the above program, the output will be:

[0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
Here, list comprehension checks:

Is y divisible by 2 or not?
Is y divisible by 5 or not?
If y satisfies both conditions, y is appended to num_list.

Exmp 3: if...else With List Comprehension
obj = ["Even" if i%2==0 else "Odd" for i in range(10)]
print(obj)
When we run the above program, the output will be:

['Even', 'Odd', 'Even', 'Odd', 'Even', 'Odd', 'Even', 'Odd', 'Even', 'Odd']
Here, list comprehension will check the 10 numbers from 0 to 9. If i is divisible by 2, then Even is appended to the obj list. If not, Odd is appended.

Nested Loops in List Comprehension
Suppose, we need to compute the transpose of a matrix that requires nested for loop. Let’s see how it is done using normal for loop first.

Exmp 4: Transpose of Matrix using Nested Loops
transposed = []
matrix = [[1, 2, 3, 4], [4, 5, 6, 8]]

for i in range(len(matrix[0])):
    transposed_row = []

    for row in matrix:
        transposed_row.append(row[i])
    transposed.append(transposed_row)

print(transposed)
Output

[[1, 4], [2, 5], [3, 6], [4, 8]]
The above code use two for loops to find transpose of the matrix.

We can also perform nested iteration inside a list comprehension. In this section, we will find transpose of a matrix using nested loop inside list comprehension.

Example 8: Transpose of a Matrix using List Comprehension
matrix = [[1, 2], [3,4], [5,6], [7,8]]
transpose = [[row[i] for row in matrix] for i in range(2)]
print (transpose)
When we run the above program, the output will be:

[[1, 3, 5, 7], [2, 4, 6, 8]]
In above program, we have a variable matrix which have 4 rows and 2 columns.We need to find transpose of the matrix. For that, we used list comprehension.

**Note: The nested loops in list comprehension don’t work like normal nested loops. In the above program, for i in range(2) is executed before row[i] for row in matrix. Hence at first, a value is assigned to i then item directed by row[i] is appended in the transpose variable.

*****Key Points to Remember*****

List comprehension is an elegant way to define and create lists based on existing lists.
List comprehension is generally more compact and faster than normal functions and loops for creating list.
However, we should avoid writing very long list comprehensions in one line to ensure that code is user-friendly.
Remember, every list comprehension can be rewritten in for loop, but every for loop can’t be rewritten in the form of list comprehension.

# In[ ]:


n=int(input("Input:\n"))
dict1=dict()
for i in range(1,n+1):
    dict1[i]=i*i
print("Output:\n",dict1)


# In[ ]:


pos = {"x":0,"y":0}
n = int(input("Input\n"))
for i in range (n):
    move = input().split(" ")
    if move[0].lower() == "up":
        pos["y"] += int(move[1])
    elif move[0].lower() == "down":
        pos["y"] -= int(move[1])
    elif move[0].lower() == "left":
        pos["x"] -= int(move[1])
    elif move[0].lower() == "right":
        pos["x"] += int(move[1])
print("Output\n",int(round((pos["x"]**2 + pos["y"]**2)**0.5)))

