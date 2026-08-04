# Even or Odd Checker
# •	Task: Write a program that prompts the user for an integer.
# o	Use if/else to check whether the number is even or odd.
# o	Print "Even" or "Odd" accordingly.
val1 = int(input("Enter a number:"))
if val1 % 2 == 0:
    print(val1," is even number.")
else:
    print(val1, "is odd number.")
# Positive, Negative, or Zero
# •	Task: Write a program that prompts the user for a number.
# o	Use if/elif/else to determine if the number is positive, negative, or zero.
# o	Print a message such as "The number is positive.".
val2 = int(input("Enter a number:"))
if val2 > 0:
    print(val2, " is positive number.")
elif val2 < 0:
    print(val2, " is negative number.")
elif val2 == 0:
    print(val2, " is zero.")
else:
    print("Enter only a number.")
# Grade Categorizer
# •	Task: Prompt the user for a number between 0 and 100 (the score).
# o	Use if/elif/else to categorize the score:
# 	90–100: "Grade A"
# 	80–89: "Grade B"
# 	70–79: "Grade C"
# 	< 70: "Fail"
marks = int(input("Enter your obtained marks:"))
if marks >= 90 and marks <= 100:
    print("Grade A")
elif marks >= 80 and marks <= 89:
    print("Grade B")
elif marks >= 70 and marks <= 79:
    print("Grade C")
elif marks < 70:
    print("Fail")
# Multiples of 3 and 5
# •	Task: Prompt the user for a single integer n.
# o	Use a for loop to iterate from 1 up to n (inclusive).
# o	For each value i, print:
# 	"Multiple of both" if i is divisible by 3 and 5.
# 	"Multiple of 3" if i is divisible by 3 but not 5.
# 	"Multiple of 5" if i is divisible by 5 but not 3.
# 	The number i itself otherwise.
n = int(input("Enter the value of n:"))
for i in range(1, n+1):
    if i % 3 == 0 and i % 5 == 0:
        print(i, "is a multiple of both 3 and 5.")
    elif i % 3 == 0 and i % 5 != 0:
        print(i, "is a multiple of 3.")
    elif i % 5 == 0 and i % 3 != 0:
        print(i, "is a multiple of 5.")
    else:
        print(i)
# Simple Password Check
# •	Task: Prompt the user for a password (e.g., "secret").
# o	Use if to check if the user’s input matches the correct password.
# o	If correct, print "Access granted", otherwise print "Access denied".
correct_pass = "secret"
user_pass = str(input("Enter the password:"))
if user_pass == correct_pass:
    print("Access granted.")
else:
    print("Access denied.")
# Count Vowels in a String
# •	Task: Ask the user for a string.
# o	Use a for loop to iterate over each character.
# o	Use if conditions to check if it’s a vowel ("a", "e", "i", "o", "u").
# o	Count the total number of vowels and print the result.
user_string = str(input("Enter a word:"))
count = 0
for char in user_string:
    if char in "aeiouAEIOU":
        count = count + 1
if count > 0:
    print("Total number of vowel letter are:", count)
else:
    print("There is no vowel letter.")
# Smallest of Three Numbers
# •	Task: Prompt the user for three different numbers.
# o	Use if/elif/else to find and print which one is smallest.
num1 = int(input("Enter the first number:"))
num2 = int(input("Enter the second number:"))
num3 = int(input("Enter the third number:"))
if num1 < num2 and num1 < num3:
    print(num1, " is smallest.")
elif num2 < num1 and num2 < num3:
    print(num2, " is smallest.")
else:
    print(num3, " is smallest.")
# Simple Menu Selection
# •	Task: Prompt the user to choose an option (e.g., 1 for "Start", 2 for "Settings", 3 for "Exit").
# o	Use if/elif/else to print a response based on which option is chosen.
# o	Example:
# 	If user enters 1: print "Game starting..."
# 	If user enters 2: print "Opening settings..."
# 	If user enters 3 or any other: print "Exiting..."
user_option = int(input("Select an option: \n1. Start \n2. Settings \n3. Exit \n Enter your Choice:"))
if user_option == 1:
    print("Game Starting...")
elif user_option == 2:
    print("Opening Settings...")
else:
    print("Existing....")
