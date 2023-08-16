#Lists
mylist = [1, 2, 3]

mylist = ['stringadgasfd', 1,2,3,23.3, True, 'asdfg',[1,2,3,]]
print(len(mylist))

list = ["a", "b", "c", "d", "e"]
print(list[1:3])
print(list[-1])
print(list[:3])
print('before reassignment:')
print(list)

list[0] = 'NEW ITEM'
print("after reassignment:")
print(list)

# Adding something to the list

list.append('ITEM') # append will add item in the list
print(list)

list.append([1,2,3]) # this will add list iside a Lists which wi;; become [., ., ., ]
print(list)

#so to add the items in the list we have to use 'extend'
list.extend([1, 2, 3]) # this will add the number inside the list

listtwo = ['p', 'q', 'r']
list.extend(listtwo)
print(list)

# Remove something from the list
list1 = ['a', 'b', 'c', 'd', 'e']
item = list1.pop() # directly pops out last item from the list
print(list1)
print(item)

list1.pop(0) # to remove the index 0 item from the list
print(list1)

# To reverse the list
list1.reverse() # Reverse the list
print(list1)

# To sort the list
list2 = [50, 23, 56, 27, 36, 4, 54, 65,12, 17]
list2.sort()
print(list2)


# Nested List
mylist1 = [1, 2, ['x', 'y', 'z']]
print(mylist1[2][1]) #Index the Nested List. Depending upon how many nested list you have inside you can call them

# List (Matrix) Comprihension
matrix = [[1,2,3], [4,5,6], [7,8,9]]
first_col = [row[0] for row in matrix]
print(first_col)
