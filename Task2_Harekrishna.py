# Python Data Structure Assignment
# Section 1: Lists
# 1.	Create a List:
# Create a list containing the numbers 1 through 15. Print the list.
list1 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
print(list1)
# 2.	List of Strings:
# Create a list of your five favorite fruits. Print the list.
fruits = ['banana','apple','orange','mango','watermilon']
print(fruits)
# 3.	Accessing Elements:
# Given the list [10, 20, 30, 40, 50], print the first and last element using positive and negative indexing.
list2 = [10,20,30,40,50]
print(list2[0])
print(list2[-1])
# 4.	List Length:
# Create a list of any 5 items and print its length using the len() function.
items = [12,35,69,14,16]
print(len(items))
# 5.	Appending Elements:
# Start with an empty list and append the numbers 1, 2, and 3. Print the list.
empty_list =[]
empty_list.append(1)
print(empty_list)
empty_list.append(2)
print(empty_list)
empty_list.append(3)
print(empty_list)
# 6.	Inserting an Element:
# Given a list [1, 3, 4], insert the number 2 at the correct position so that the list becomes [1, 2, 3, 4].
ins = [1,3,4]
ins.insert(1,2)
print(ins)
# 7.	Removing an Element:
# Remove the number 3 from the list [1, 2, 3, 4, 5] using a list method and print the new list.
rem = [1,2,3,4,5]
rem.remove(3)
print(rem)
# 8.	Popping an Element:
# Given the list [10, 20, 30, 40], pop the last element and print the element and the updated list.
po = [10,20,30,40]
po.pop(3)
print(po)
# 9.	Slicing a List:
# Given the list [0, 1, 2, 3, 4, 5], print a slice that contains the elements from index 2 to 4.
sl = [0,1,2,3,4,5]
s2= sl[2:4]
print('Sliced element are:',s2)
# 10.	List Concatenation:
# Concatenate two lists, e.g., [1, 2, 3] and [4, 5, 6], and print the resulting list.
l1 = [1,2,3]
l2 = [4,5,6]
concatinate = l1 + l2
print(concatinate)
# 11.	Repeating a List:
# Create a list [1, 2] and print the list repeated three times.
rept = [1,2]
rept = rept*3
print(rept)
# 12.	Copying a List:
# Create a copy of a given list and print both the original and the copy.
org = ['arun','nisha','kirti']
cpy = org.copy()
print(org)
print(cpy)
# 13.	Clearing a List:
# Given any list, use a method to clear all its elements and then print the empty list.
safa = [14,5,19,12]
safa.clear()
print(safa)



# Section 2: Tuples
# 1.	Create a Tuple:
# Create a tuple containing the numbers 1, 2, and 3. Print the tuple.
tap = (1,2,3)
print(tap)
# 2.	Tuple of Strings:
# Create a tuple of three different color names and print it.
tap_col = ('organg','red','green')
print(tap_col)
# 3.	Accessing Tuple Elements:
# Given the tuple (10, 20, 30, 40), print the second element.
giv_tup = (10,20,30,40)
print(giv_tup[1])
# 4.	Tuple Slicing:
# Using the tuple (0, 1, 2, 3, 4), print a slice that contains elements from index 1 to 3.
diyeko = (0,1,2,3,4)
nikaleko = diyeko[1:3]
print(nikaleko)
# 5.	Concatenating Tuples:
# Concatenate two tuples, e.g., (1, 2) and (3, 4), and print the result.
pahilo = (1,2)
dosro = (3,4)
jodeko = pahilo + dosro
print(jodeko)
# 6.	Tuple Unpacking:
# Store the tuple ("Alice", 25, "New York") into three variables and print them.
deko_xa = ("Alice",25,"New York")
x = deko_xa[0]
y = deko_xa[1]
z = deko_xa[2]
print(x,y,z)
# 7.	Convert List to Tuple:
# Convert the list [1, 2, 3, 4] into a tuple and print the tuple.
listxa = [1,2,3,4]
print(tuple(listxa))
# 8.	Counting Occurrences:
# Given the tuple (1, 2, 2, 3, 2), count how many times the number 2 appears.
ganney = (1,2,2,3,2)
print(ganney.count(2))
# 9.	Finding an Index:
# In the tuple (10, 20, 30, 40), find the index of the element 30 and print it.
deko_xa = (10,20,30,40)
deko_xa.index(30)
print('index is:',deko_xa.index(30))
