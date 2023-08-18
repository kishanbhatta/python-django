# ## Comparision Operators
#
# # Greater than
# 1 > 2
# # Less than
# 1 < 2
# #Greater than or Equal to
# 1 >= 1
# # Less than or Equal to
# 1 <= 4
# #Equality
# 1 == 1
# 1 == "1"
# 'hi' == 'bye'
# #Inequality
# 1 != 2
#
# #Logical Operators
# #AND
# (1 > 2) and (2 < 3)
#
# # OR
# (1 > 2) or (2 < 3)
#
# # Multiple Logical Operators
# (1 == 2) or (2 == 3) or (4 == 4)

# Basics of the if statement
if 1<2:
    print('First Block')
    if 20 < 3:
        print("Second Block")

# if else statement
if 1 == 1:
    if 1 < 2:
        print("hello")
    elif 3 == 3:
        print('elif ran')
    else:
        print('last')

# For Loops
seq = [1,2,3,4,5,6]
for item in seq:
    # Code here
    print(item)
    print('hello')

d = {"Sam":1,"Frank":2,"Dan":3}
for k in d:
    print(k)
    print(d[k])

# Tuples and Tuples Unpacking
mypairs = [(1,2), (3,4), (5,6)]
for item in mypairs:
    print(item)

for (tup1,tup2) in mypairs:
    print(tup2)
    print(tup1)

# While Loops
i = 1
while i<5:
    print("i is: {}".format(i))
    i = i+1

for item in range(10):
    print(item)

# List Comprehension

x = [1,2,3,4]

out = []
for num in x:
    out.append(num**2)
print(out)

# Smart way to write the list comprehension
x = [5,6,7,8,9]

out = [num**2 for num in x]
print(out)
