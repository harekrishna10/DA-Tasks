# Iterate Through a Tuple and Print Types
# •	Task: Create a tuple with at least 5 different types of elements (int, float, string, bool, and complex).
# •	Use a for loop to iterate over the tuple and print each element along with its data type.
t = (1,2.2,"Three",True,3 + 4j)
for i in t:
    print(f"Element: {i}, Data type: {type(i)}")


# Print All Items from a List with a Custom Message
# •	Task: Create a list of 4 different city names.
# •	Use a for loop to print each city name followed by the phrase "is a great place".
l1 = ["Kathmandu","Pokhara","Chitwan","Manakamana"]
for i in l1:
    print(f"{i} is a great place.")


# Print Each Character of a String with Its Index
# •	Task: Ask the user to enter a word.
# •	Use a for loop and enumerate() to print each character of the string along with its index.
word = str(input("Enter the word:"))
for i, words in enumerate(word): # enumerate function give each character along with its index no
    print(f"Index{i} : {words}")

# Sum of Elements in a List
# •	Task: Create a list of integers.
# •	Use a for loop to calculate the sum of all the elements and print the total.
l2 = [1,2,3,4,5]
sum = 0
for i in l2:
    sum = sum + i
    i += 1
print("sum of list is:",sum)
    
# Count Booleans in a Tuple
# •	Task: Create a tuple containing different data types, including multiple True and False values.
# •	Use a for loop to count how many True values are present and print the count.
t2 = (6,2,"Three",True,"Four",False,True,False,79,1)
count = 0
for i in t2:
    if isinstance(i,bool) and i == True: # isinstance function is used to chek if assign element in i is of bool data type or not.
        count = count + 1
print("Number of True in t2 is:", count)


# Check and Print Data Types from a List
# •	Task: Create a list with at least 6 elements of different types (int, float, str, bool, etc.).
# •	Use a for loop to iterate through the list and print the data type of each element.
l3 = [1,2.3,"Three",True,4 + 6j]
for i in l3:
    print(f" Element {i}, has data type : {type(i)}")


# Check for Vowels in a String
# •	Task: Ask the user for a word.
# •	Use a for loop to check each character and print a message if it’s a vowel (a, e, i, o, u).
u_word = str(input("Enter the word:"))
for i in u_word.lower():
    if i in 'aeiou':
        print(i)


# Print Square of Numbers from a Tuple
# •	Task: Create a tuple of numbers from 1 to 5.
# •	Use a for loop to iterate through the tuple and print the square of each number.
t3 = (1,2,3,4,5)
for i in t3:
    print(i**2)


# Print Elements of a List in Uppercase
# •	Task: Create a list of 5 small letter containing words.
# •	Use a for loop to iterate over the list and print each word in lowercase.
l4 = ["cow","goat","horse","buffalo"]
for i in l4:
    print(i.lower())

# Count Numbers Greater Than 10 in a List
# •	Task: Create a list of integers.
# •	Use a for loop to count how many numbers in the list are greater than 10.
# •	Print the final count.
l5 = [1,200,40,7,75,69,36,3,6996,1415]
count = 0
for i in l5:
    if i > 10:
        count = count + 1
print("Final count is:",count)

