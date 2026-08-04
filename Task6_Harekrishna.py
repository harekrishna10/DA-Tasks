# Print Numbers from 10 to 30
# •	Use a while loop to print numbers from 10 to 30.
i = 10
while i <= 30:
    print(i)
    i += 1


# Print Odd Numbers from 1 to 20
# •	Use a while loop to print all odd numbers from 1 to 20.
i = 1
while i <= 20:
    if i%2 != 0:
        print(i)
    i += 1


# Print a Word 5 Times
# •	Use a while loop to print the word "Hello" five times.
word = 'Hello'
i = 0
while i < 5:
    print(word)
    i += 1


# Countdown from 5
# •	Use a while loop to print numbers from 5 to 1.
i = 5
while i > 0:
    print(i)
    i -= 1


# Print All Multiples of 3 up to 30
# •	Use a while loop to print 3, 6, 9, ..., up to 30.
i = 3
while i <= 30:
    print(i)
    i += 3


# Keep Asking for a Number Until It's Positive
# •	Keep asking the user to enter a number until they enter a positive number.
number = int(input("Enter the positive number:"))
while number <= 0:
    print("you entered the negative number. Try again !")

    number = int(input("Enter the positive number:"))

print("Congratulation ! You entered the positive number.",number)


# Print Even Numbers Between 10 and 20
# •	Use a while loop to print even numbers from 10 to 20.
i = 10
while i <= 20:
    if i%2 == 0:
        print(i)
    i += 1


# Guess the Secret Number using while loop
# •	Secret number = 7.
# •	Ask the user to guess the number until it's correct.

secret_number = 7
guess = int(input("Guess the secret number:"))
if guess != secret_number:
    print("Your guessed number is wrong. Try again !")

    guess = int(input("Guess the secret number:"))

print("Congratulation you guessed a secret number.")

# Function to Add Two Numbers
# •	Create a function add(a, b) that returns the sum.
def add(a,b):
    return a + b
print(add(7,8))


# Function to Multiply Two Numbers
# •	Create a function multiply(x, y) that returns the product.
def multiply(x,y):
    return x * y
print(multiply(7,8))


# Function to Check Even or Odd
# •	Create a function check_even(num) that prints "Even" or "Odd".
def number_cheker(num):
    if num%2 == 0:
        print("Even number:", num)
    else:
        print("Odd number:", num)
number_cheker(8)
