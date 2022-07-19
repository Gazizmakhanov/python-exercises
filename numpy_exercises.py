import numpy as np

a = np.array([4, 10, 12, 23, -2, -1, 0, 0, 0, -6, 3, -7])

a < 0
a[a < 0]

len(a[a < 0])

a[a < 0].shape

len(a[a > 0])

pos_nums = a[a > 0]

len(pos_nums[pos_nums % 2 == 0])

pos_nums[pos_nums % 2 == 0]

a[(a > 0) & (a % 2 == 0)]

len(a[(a + 3) > 0])

a_squared = a ** 2
In [21]:
a_squared.mean(), a_squared.std()

centered_a = a - a.mean()
In [23]:
centered_a.mean()

z_scores = centered_a / a.std()
In [ ]:
# equivalent: z_scores = (a - a.mean()) / a.std()
In [25]:
z_scores
Out[25]:
array([ 0.12403473,  0.86824314,  1.11631261,  2.48069469, -0.62017367,
       -0.49613894, -0.3721042 , -0.3721042 , -0.3721042 , -1.11631261,
        0.        , -1.24034735])
In [ ]:
# Copy the setup and exercise directions from More Numpy Practice into your numpy_exercises.py and add your solutions.
In [27]:
## Setup 1
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

type(a)
Out[28]:
list
In [29]:
sum(a)
Out[29]:
55
In [ ]:
# Exercise 2 - Make a variable named min_of_a to hold the minimum of all the numbers in the above list
In [30]:
min(a)
Out[30]:
1
In [ ]:
# Exercise 3 - Make a variable named max_of_a to hold the max number of all the numbers in the above list
In [31]:
max(a)
Out[31]:
10
In [ ]:
# Exercise 4 - Make a variable named mean_of_a to hold the average of all the numbers in the above list
In [33]:
sum(a) / len(a)
Out[33]:
5.5
In [ ]:
# Exercise 5 - Make a variable named product_of_a to hold the product of multiplying all the numbers in the above list together
In [34]:
prod_a = 1
for n in a:
    prod_a *= n
In [35]:
prod_a
Out[35]:
3628800
In [ ]:
# Exercise 6 - Make a variable named squares_of_a. It should hold each number in a squared like [1, 4, 9, 16, 25...]
In [36]:
[n ** 2 for n in a]
Out[36]:
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
In [ ]:
# Exercise 7 - Make a variable named odds_in_a. It should hold only the odd numbers
In [38]:
[n for n in a if n % 2 != 0]
Out[38]:
[1, 3, 5, 7, 9]
In [ ]:
# Exercise 8 - Make a variable named evens_in_a. It should hold only the evens.
In [39]:
[n for n in a if n % 2 == 0]
Out[39]:
[2, 4, 6, 8, 10]
In [45]:
# ## Setup 2: Consider what it would take to find the sum, min, max, average, sum, product, and list of squares for this list of two lists.
b = [
    [3, 4, 5],
    [6, 7, 8]
]
In [41]:
len(b)
Out[41]:
2
In [42]:
len(b[0])
Out[42]:
3
In [43]:
type(b)
Out[43]:
list
In [46]:
b2 = np.array(b)
In [47]:
# # Exercise 1 - refactor the following to use numpy. Use sum_of_b as the variable. 
# **Hint, you'll first need to make sure that the "b" variable is a numpy array**
sum_of_b = 0
for row in b:
    sum_of_b += sum(row)
In [50]:
sum_of_b
Out[50]:
33
In [49]:
b2.sum()
Out[49]:
33
In [52]:
# # Exercise 2 - refactor the following to use numpy. 
min_of_b = min(b[0]) if min(b[0]) <= min(b[1]) else min(b[1])  
In [53]:
min_of_b
Out[53]:
3
In [51]:
b2.min()
Out[51]:
3
In [19]:
# # Exercise 3 - refactor the following maximum calculation to find the answer with numpy.
max_of_b = max(b[0]) if max(b[0]) >= max(b[1]) else max(b[1])
In [54]:
b2.max()
Out[54]:
8
In [55]:
# # Exercise 4 - refactor the following using numpy to find the mean of b
mean_of_b = (sum(b[0]) + sum(b[1])) / (len(b[0]) + len(b[1]))
In [56]:
b2.mean()
Out[56]:
5.5
In [57]:
# # Exercise 5 - refactor the following to use numpy for calculating the product of all numbers multiplied together.
product_of_b = 1
for row in b:
    for number in row:
        product_of_b *= number
In [58]:
np.prod(b2)
Out[58]:
20160
In [ ]:
# # Exercise 6 - refactor the following to use numpy to find the list of squares 
squares_of_b = []
for row in b:
    for number in row:
        squares_of_b.append(number**2)
In [59]:
np.square(b2)
Out[59]:
array([[ 9, 16, 25],
       [36, 49, 64]])
In [60]:
# # Exercise 7 - refactor using numpy to determine the odds_in_b
odds_in_b = []
for row in b:
    for number in row:
        if(number % 2 != 0):
            odds_in_b.append(number)
            
In [61]:
b2[b2 % 2 != 0]
Out[61]:
array([3, 5, 7])
In [62]:
# # Exercise 8 - refactor the following to use numpy to filter only the even numbers
evens_in_b = []
for row in b:
    for number in row:
        if(number % 2 == 0):
            evens_in_b.append(number)
In [63]:
b2[b2 % 2 == 0]
Out[63]:
array([4, 6, 8])
In [64]:
# # Exercise 9 - print out the shape of the array b.
b2.shape
Out[64]:
(2, 3)
In [65]:
b2
Out[65]:
array([[3, 4, 5],
       [6, 7, 8]])
In [66]:
# size vs shape vs len
In [67]:
b2.size, b2.shape, len(b2)
Out[67]:
(6, (2, 3), 2)
In [69]:
b2
Out[69]:
array([[3, 4, 5],
       [6, 7, 8]])
In [68]:
# # Exercise 10 - transpose the array b.
b2.transpose()
Out[68]:
array([[3, 6],
       [4, 7],
       [5, 8]])
In [70]:
# # Exercise 11 - reshape the array b to be a single list of 6 numbers. (1 x 6)
In [71]:
b2.reshape(1,6)
Out[71]:
array([[3, 4, 5, 6, 7, 8]])
In [ ]:
# # Exercise 12 - reshape the array b to be a list of 6 lists, each containing only 1 number (6 x 1)
In [72]:
b2.reshape(6,1)
Out[72]:
array([[3],
       [4],
       [5],
       [6],
       [7],
       [8]])
In [73]:
# ## Setup 3
c = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
In [74]:
c = np.array(c)
In [ ]:
# # HINT, you'll first need to make sure that the "c" variable is a numpy array prior to using numpy array methods.
# # Exercise 1 - Find the min, max, sum, and product of c.
In [75]:
c.min(), c.max(), c.sum(), c.prod()
Out[75]:
(1, 9, 45, 362880)
In [ ]:
# # Exercise 2 - Determine the standard deviation of c.
In [79]:
c.std()
Out[79]:
2.581988897471611
In [ ]:
# # Exercise 3 - Determine the variance of c.
In [77]:
c.var()
Out[77]:
6.666666666666667
In [ ]:
# # Exercise 4 - Print out the shape of the array c
In [80]:
c.shape
Out[80]:
(3, 3)
In [ ]:
# # Exercise 5 - Transpose c and print out transposed result.
In [81]:
print(c.transpose())
[[1 4 7]
 [2 5 8]
 [3 6 9]]
In [ ]:
# # Exercise 6 - Get the dot product of the array c with c. 
In [82]:
np.dot(c, c)
Out[82]:
array([[ 30,  36,  42],
       [ 66,  81,  96],
       [102, 126, 150]])
In [ ]:
# # Exercise 7 - Write the code necessary to sum up the result of c times c transposed. Answer should be 261
In [84]:
np.sum(c * c.transpose())
Out[84]:
261
In [ ]:
# # Exercise 8 - Write the code necessary to determine the product of c times c transposed. Answer should be 131681894400.
In [85]:
np.prod(c * c.transpose())
Out[85]:
131681894400
In [86]:
# ## Setup 4
d = [
    [90, 30, 45, 0, 120, 180],
    [45, -90, -30, 270, 90, 0],
    [60, 45, -45, 90, -45, 180]
]
d = np.array(d)
In [87]:
# # Exercise 1 - Find the sine of all the numbers in d
In [88]:
np.sin(d)
Out[88]:
array([[ 0.89399666, -0.98803162,  0.85090352,  0.        ,  0.58061118,
        -0.80115264],
       [ 0.85090352, -0.89399666,  0.98803162, -0.17604595,  0.89399666,
         0.        ],
       [-0.30481062,  0.85090352, -0.85090352,  0.89399666, -0.85090352,
        -0.80115264]])
In [ ]:
# # Exercise 2 - Find the cosine of all the numbers in d
In [89]:
np.cos(d)
Out[89]:
array([[-0.44807362,  0.15425145,  0.52532199,  1.        ,  0.81418097,
        -0.59846007],
       [ 0.52532199, -0.44807362,  0.15425145,  0.98438195, -0.44807362,
         1.        ],
       [-0.95241298,  0.52532199,  0.52532199, -0.44807362,  0.52532199,
        -0.59846007]])
In [ ]:
# # Exercise 3 - Find the tangent of all the numbers in d
In [90]:
np.tan(d)
Out[90]:
array([[-1.99520041, -6.4053312 ,  1.61977519,  0.        ,  0.71312301,
         1.33869021],
       [ 1.61977519,  1.99520041,  6.4053312 , -0.17883906, -1.99520041,
         0.        ],
       [ 0.32004039,  1.61977519, -1.61977519, -1.99520041, -1.61977519,
         1.33869021]])
In [ ]:
# # Exercise 4 - Find all the negative numbers in d
In [91]:
d[d < 0]
Out[91]:
array([-90, -30, -45, -45])
In [ ]:
# # Exercise 5 - Find all the positive numbers in d
In [92]:
d[d > 0]
Out[92]:
array([ 90,  30,  45, 120, 180,  45, 270,  90,  60,  45,  90, 180])
In [ ]:
# # Exercise 6 - Return an array of only the unique numbers in d.
In [95]:
np.unique(d)
Out[95]:
array([-90, -45, -30,   0,  30,  45,  60,  90, 120, 180, 270])
In [ ]:
# # Exercise 7 - Determine how many unique numbers there are in d.
In [96]:
len(np.unique(d))
Out[96]:
11
In [ ]:
# # Exercise 8 - Print out the shape of d.
In [97]:
d.shape
Out[97]:
(3, 6)
In [ ]:
# # Exercise 9 - Transpose and then print out the shape of d.
In [98]:
d.transpose().shape
Out[98]:
(6, 3)
In [99]:
d.size
Out[99]:
18
In [ ]:
# # Exercise 10 - Reshape d into an array of 9 x 2
In [100]:
np.reshape(d, (9,2))
Out[100]:
array([[ 90,  30],
       [ 45,   0],
       [120, 180],
       [ 45, -90],
       [-30, 270],
       [ 90,   0],
       [ 60,  45],
       [-45,  90],
       [-45, 180]])
In [101]:
d.reshape(9,2)
Out[101]:
array([[ 90,  30],
       [ 45,   0],
       [120, 180],
       [ 45, -90],
       [-30, 270],
       [ 90,   0],
       [ 60,  45],
       [-45,  90],
       [-45, 180]])


