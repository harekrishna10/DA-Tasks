# Integer & Float Mix
# •	Create an integer a and a float b.
a = 10
b = 19.79
# •	Perform addition, subtraction, multiplication, and division on them.
addition = a + b
subtraction = a - b
multiplication = a * b
division = a / b
# •	Print the results and observe the type of each result with type().
print(addition)
print(subtraction)
print(multiplication)
print(division)
print(type(addition))
print(type(subtraction))
print(type(multiplication))
print(type(division))
# Large Integers & Type
# •	Assign a very large integer to a variable (e.g., in the billions).
large_int = 12345678901234567890
# •	Print it and confirm its type is still int in Python or not.
print(large_int)
print(type(large_int)) # yes, its type is still in python.
# Complex Number Basics
# •	Create a complex number z = 3 + 4j.
z = 3 + 4j
# •	Print its real part, imaginary part, and confirm its type is complex.
print(z.real)
print(z.imag)
print(type(z))
# •	Perform a basic arithmetic operation with another complex number (e.g., (3 + 4j) + (1 + 2j)).
second = 1 + 2j
result = z + second
print(result)
# Boolean from Comparisons
# •	Create two variables, m = 10 and n = 15.
m = 10
n = 15
# •	Define status = (m > n) and print status.
status = (m > n)
print(status)
# •	Confirm type(status) is bool.
print(type(status)) # yes, type of status is bool.
# •	Assign status = (m != n) and print again.
status = (m != n)
print(status)
# String Creation & Indexing
# •	Create a string text = "HelloWorld".
text = "Helloworld"
# •	Print the first and last characters using positive and negative indexing.
print(text[0])
print(text[-1])
# •	Comment on the total length of the string.
print(len(text)) # Tottal lenth of text is 10.
# String Slicing
# •	With lang = "PythonProgramming", print the substring from index 2 to 8.
lang = "PythonProgramming"
print(lang[2:8])
# •	Print the substring from the start up to index 5.
print(lang[0:5])
# •	Print the entire string in reverse using slicing.
print(lang[::-1])
# String Methods
# •	Let phrase = " Hello, Python World! ".
phrase = " Hello, Python World!  "
# •	Demonstrate strip(), upper(), and replace() on this string.
print(phrase.strip())
print(phrase.upper())
nepal = phrase.replace("Python", "Nepal")
# •	Print the results and comment on immutability of strings in Python.
print(nepal) # string in python is immutable because changing single element of string is not possible.
# String Formatting
# •	Create two variables: name = "Rajesh" and score = 95.
name = "Rajesh"
score = 95
# •	Print: "Alice scored 95 points." using two methods (concatenation and an f-string or str.format()).
change = name.replace("Rajesh","Alice")
print(change)
print(change + "" , "scored" , score , "points.")
print(f"{change} scored {score} points.")
# Boolean Operations in Expressions
# •	Write a small expression using and, or, and not with boolean values.
# •	Example: result = not(True and False) or (5 > 3).
# •	Print result and explain how Python evaluated the expression.
result = not(True and False) or (5 > 3)
print(result) # here, python checks first not(True and False) then check (5 > 3) and if any condition match like 5 is greater than 3 so it prints True.
# List Creation & Access
# •	Create a list of 5 different integers.
# •	Print the first item, middle item, and last item using indexing.
lst = [1,2,3,4,5]
print(lst[0])
print(lst[2])
print(lst[4])
# List Insertion & Deletion
# •	Start with a list nums = [10, 20, 30, 40].
# •	Insert 25 at index 2.
# •	Remove the last element.
# •	Print the updated list.
nums = [10, 20, 30, 40]
nums.insert(2, 25)
nums.pop(-1)
print(nums)
# List Slicing
# •	Given letters = ["a", "b", "c", "d", "e"], print the slice that contains only ["b", "c", "d"].
letters = ["a", "b", "c", "d", "e"]
letter_slice = letters[1:4]
print(letter_slice)
# •	Print the slice that omits the first and the last element.
print(letter_slice[1:-1])
# Sorting & Reversing
# •	Create a list of random integers.
rand_int = [1,4,23,9,12]
# •	Sort the list in ascending order and print it.
rand_int.sort()
print(rand_int)
# •	Reverse the sorted list and print again.
print(rand_int[::-1])
# Combining Lists
# •	Let list1 = [1, 2, 3] and list2 = [4, 5, 6].
list1 = [1,2,3]
list2 = [4,5,6]
# •	Combine them into a single list and print.
# •	Demonstrate two ways: using + and using .extend().
list3 = list1 + list2
print(list3)
list1.extend(list2)
print(list1)
# Aggregating List Values
# •	Create a list of floats, e.g., [2.5, 3.6, 1.2, 5.0].
l_float = [2.5, 3.6, 1.2, 5.0]
# •	Print the sum, minimum, and maximum of that list using built-in functions.
print(sum(l_float))
print(min(l_float))
print(max(l_float))
# Tuple Creation
# •	Create a tuple t = (10, 20, "Hello", True).
t = (10, 20, "Hello", True)
# •	Print the tuple and confirm its type with type(t).
print(t)
print(type(t))
# Tuple Indexing & Slicing
# •	Print the first two elements of t using slicing.
f_element = t[0:2]
print(f_element)
# •	Print the last element of t using negative indexing.
print(t[-1])
# Tuple Unpacking
# •	Suppose t2 = ("Tom", 25, "Engineer").
t2 = ("Tom", 25, "Engineer")
# •	Unpack it into three separate variables: name, age, profession.
name = t2[0]
age = t2[1]
profession = t2[2]
# •	Print these variables individually.
print(name)
print(age)
print(profession)
# Attempt Tuple Mutation
# •	Try to change an element of t (t[0] = 999) and observe the error.
# •	In comments, explain why the error occurs.
# t[0] = 999
# print(t) # the error occurs because tuple is immutable which means we cannot change element of tuple once its created.
# Set Creation & Membership
# •	Create a set my_set = {1, 3, 5, 7}.
my_set = {1, 3, 5, 7}
# •	Check if 5 is in my_set.
print(5 in my_set)
# •	Check if 2 is not in my_set.
print(2 not in my_set)
# Add & Remove Elements
# •	Add 9 to my_set.
my_set.add(9)
# •	Remove 3 from my_set.
my_set.remove(3)
# •	Print the updated set.
print(my_set)
# Set Operations
# •	Create two sets: setA = {1, 2, 3} and setB = {3, 4, 5}.
setA = {1, 2, 3}
setB = {3, 4, 5}
# •	Print the union, intersection, and difference (setA - setB).
print(setA.union(setB))
print(setA.intersection(setB))
print(setA - setB)
# Check Unique Values
# •	Define a list vals = [1, 2, 2, 3, 3, 3, 4].
vals = [1, 2, 2, 3, 3, 3, 4]
# •	Convert it to a set.
val_set = set(vals)
# •	Print both the list and the set to show how duplicates are removed.
print("Original list:", vals)
print("Set:", val_set)
# Frozenset Creation
# •	Create a frozenset from a list [2, 4, 4, 6].
li = [2,4,4,6]
froz_set = frozenset(li)
# •	Print it and observe whether duplicates are preserved.
print(li)
print(froz_set) # duplicates are not preserved in frozenset because it is immutable and does not allow duplicate values.
# Operator Precedence
# •	Define a = 4, b = 2, c = 5.
# •	Print the result of a + b * c vs. (a + b) * c.
a = 4
b = 2
c = 5
print(a + b * c) # it means first multiply then add.
print((a + b) * c) # it means, first add then multiply.
# •	Explain in comments how the result differs.
# Modulo & Floor Division
# •	Let x = 17 and y = 4.
# •	Print x % y and x // y.
# •	Explain the difference between these two operators in comments.
x = 17
y = 4
print(x % y) # this will print remainder value after division.
print(x // y) # this will remove decimal from quotient and print onlu int value.
# Power Operator
# •	Print the result of 2 ** 3.
a = 2 ** 3
# •	Write a line to calculate 3 ** 4.
b = 3 ** 4
# •	Print the addition of both.
print(a + b)
# String Comparison
# •	Compare "apple" and "banana" with <, >, and ==.
# •	Print the results.
str1 = "apple"
str2 = "banana"
print(str1 < str2)
print(str1 > str2)
print(str1 == str2)
# Mixed Type Comparison
# •	Compare 5 and 5.0 with ==.
print(5 == 5.0) # True becoz 5 is equal to 5.0
# •	Compare 5 and 5.0 with is.
print(5 is 5.0) # false bcoz 5 is int here and 5.0 is float.
# •	Discuss the results in comment.
# Chain Comparisons
# •	Evaluate the expression 2 < 3 < 5.
# •	Print the result and explain how Python handles chained comparisons.
print("result :", 2 < 3 < 5) # python first compare 2 with 3, where 2 is less than 3 and again compare 2 with 5 which is also less than 5 too and also 3 is less than 5 so it prints true.
# Logical and
# •	Define p = True and q = False.
p = True
q = False
# •	Print p and q.
print("what comes:", p and q)
# •	Demonstrate a real-world example: (age > 18) and (has_ID == True).
age = 25
has_ID = True
print((age > 18) and (has_ID == True))
# Logical or
# •	Using the same p and q, print p or q.
print("what comes:", p or q)
# Logical not
# •	Let r = (10 > 5).
r = (10 > 5)
# •	Print r, then print not r.
print(r)
print(not r)
# Using len()
# •	Create a list with 7 elements.
# •	Use len() to get the total count.
# •	Print the result.
leng_str = [1,2,34,'five','six',7]
print(len(leng_str))
# Using type()
# •	For each of the following: 10, 10.5, "ten", True, 3+2j, print type(...).
# •	Summarize in comments the data types you observed.
var = [10, 10.5, "ten", True, 3+2j]
print(type(var[0])) # int data type
print(type(var[1])) # float data type
print(type(var[2])) # str data type
print(type(var[3])) # bool data type
print(type(var[4])) # complex data type
# Using abs()
# •	Print abs(10), abs(-10), and abs(-3.5).
# •	Explain what abs() does in comments.
print(abs(10)) # it returns as it is.
print(abs(-10)) # here, abs() removed -ve sign from int.
print(abs(-3.5)) # here, abs() removed -ve sign from float.
# Using round()
# •	Demonstrate round(3.14159, 2).
print(round(3.14159, 2)) # it rounds the number to 2 decimal places and prints 3.14
# •	Show how round(2.5) behaves in Python.
print(round(2.5)) # it rounds to the nearest even number, so it prints 2
# Using sum(), max(), min()
# •	Create a list of numeric values.
# •	Print sum(), max(), and min() of that list.
num_var = [10,99,2,76,36,69,14]
print("sum:", sum(num_var))
print("max:", max(num_var))
print("min:", min(num_var))
# Using sorted()
# •	Create a list or tuple vals = (3, 1, 4, 2).
# •	Use sorted(vals) and print the result.
# •	Show that vals itself is unchanged.
vals = (3, 1, 4, 2)
print("Original vals:", vals)
new_vals = sorted(vals)
print("Sorted vals:", new_vals) # vals itself desonot change because sorted() only returns a new sorted list.
# Using any() / all()
# •	Create a list of booleans, for example [True, False, True].
# •	Print any() on the list, then all() on the list.
# •	Show the difference in how they evaluate.
bool_lst = [True, False, True]
print(any(bool_lst)) # here, any() gives true because some of is True on list.
print(all(bool_lst)) # here, all() gives false because all element of list are not True.
# Storing Booleans from Comparisons
# •	Compare two values in separate expressions, e.g., a = (10 > 3), b = (5 == 5).
# •	Combine these booleans with and or or.
# •	Print the final result.
a = (10 > 3)
b = (5 == 5)
print(a and b) # here, both a and b are true so it prints true.
print(a or b) # here, both a or b are true so it prints true.
# Multiline String & Counting
# •	Create a multiline string describing your favorite hobby.
# •	Use the string method .count(substring) to count how many times the letter "a" appears (case-insensitive).
# •	Print the count and explain any steps taken to handle case sensitivity.
hobby = """I love playing football. Football is a great sport that requires skill, teamwork, and dedication. I enjoy the thrill of scoring goals and the camaraderie with my teammates."""
count_a = hobby.count('a')
print("Count of 'a' is:", count_a)

# Advanced String Slicing
# •	Take the string "ABCDEFGHIJ" and slice every second character, resulting in "ACEGI".
# •	Print the sliced string.
# •	Also slice in reverse step.
str1 = "ABCDEFGHIJ"
sliced_str = str1[0::2]
print("Sliced string:", sliced_str)
print("Reversed sliced string:", sliced_str[::-1])
# Casefold vs. Lower
# •	Create two strings, "Case" and "case".
# •	Compare them with the regular == operator directly.
# •	Compare them again after applying .casefold().
# •	Print results and comment on how .casefold() differs from .lower() in edge cases.
strf1 = "Case"
strf2 = "case"
print(strf1 == strf2) # this will print false because of case sensitivity.
print(strf1.casefold() == strf2.casefold()) # here, it printed true because casefold() changes all characters to lowercase.
# Formatted Printing
# •	Define name = "Ramesh", product = "Notebook", quantity = 2, and price = 12.50.
# •	Use an f-string (or str.format()) to print:
# "Ramesh purchased 2 Notebook for a total of $25.0."
name = "Ramesh"
product = "Notebook"
quantity = 2
price = 12.50
print(f"{name} purchased {quantity} {product} for a total of ${quantity * price}.")
# Type Conversion Chain
# •	Ask a user for a string that represents a number, e.g., "0".
# •	Convert it to a float, then to a bool, and print the intermediate and final results.
user_input = input("Enter a number as a string: ")
float_value = float(user_input)
bool_value = bool(float_value)
print("Float value:", float_value)
print("Boolean value:", bool_value)
# String List Sorting
# •	Given fruits = ["apple", "banana", "cherry"], sort them in descending alphabetical order.
# •	Print the sorted list, then use the .reverse() method to flip it. Compare the two results.
fruits = ["apple", "banana", "cherry"]
fruits.sort(reverse=True)
print("Descending order:", fruits)
fruits.reverse()
print("Reversed order:", fruits)
# Insert Using Slicing
# •	Start with a list [2, 5, 7, 1, 9].
# •	Insert the value 4 right after the 2 using slicing (not insert() or append()).
# •	Print the modified list.
lst2 = [2, 5, 7, 1, 9]
lst2[1:1] = [4]
print("Modified list:", lst2)
# Indexing Within a Mixed List
# •	Create a list info = ["John", 28, True, 4500.75].
# •	Print only "John" and 4500.75 using their indices.
info = ["John", 28, True, 4500.75]
print(info[0])
print(info[3])
# Tuple Concatenation & Replication
# •	Create two tuples (1, 2) and (3, 4).
# •	Concatenate them into (1, 2, 3, 4).
# •	Replicate (1, 2) 3 times to get (1, 2, 1, 2, 1, 2).
tuple1 = (1, 2)
tuple2 = (3, 4)
concatenated_tuple = tuple1 + tuple2
replicated_tuple = tuple1 * 3
print("Concatenated tuple:", concatenated_tuple)
print("Replicated tuple:", replicated_tuple)
# Single-Element Tuple
# •	Demonstrate that (42,) is a tuple whereas (42) is just an integer.
is_tuple = (42,)
not_tuple = (42)
print(type(is_tuple))
print(type(not_tuple))
# Intersection & Union
# •	Let setA = {1, 2, 3, 4} and setB = {1,2,3}.
setA = {1, 2, 3, 4}
setB = {1, 2, 3}
# •	Print their intersection using setA & setB.
print(setA.intersection(setB))
# •	Print their union using setA | setB.
print(setA.union(setB))
# Subset and Superset
# •	Check if setB is a subset of setA using setB.issubset(setA).
# •	Check if setA is a superset of setB using setA.issuperset(setB).
# Print the results.
print(setB.issubset(setA))
print(setA.issuperset(setB))