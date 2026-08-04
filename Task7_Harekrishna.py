# Function with Default Argument
# Question:
# Create a function greet(name, message="Welcome!") that prints:
# "Hello, <name>! <message>"
# •	Call the function with and without the message argument.
def greet(name,message="Welcome !"):
    print(f"Hello, {name} {message}")
greet("Harekrishna")
greet("Harekrishna","Welcome to Nepal.")


# Function with args (Variable Number of Arguments)
# Question:
# Create a function total(*numbers) that takes any number of numeric arguments and returns their sum.
# •	Example call: total(5, 10, 15) should return 30.
def total(*number):
    add = 0
    for i in number:
        add += i
    return add
print(f"Sum of number: {total(5,10,15)}")


# Function with kwargs (Keyword Arguments)
# Question:
# Create a function display_info(**details) that prints key-value pairs like:
# name: Rajesh 
# age: 25  
# city: Kathmandu  
def display_info(**details): # using **parameter inside the function prints the object in dictionary type.
    print(details)

display_info(name = "Rajesh", age = "25", city = "kathmandu")


# Function Using Both args and a Default Argument
# Question:
# Create a function repeat_words(*words, times=2) that repeats each word the given number of times.
# •	Example: repeat_words("Hi", "Bye", times=3)
# Output:
def repeat_words(*words,times = 2):
    for word in words:
        print(word * times)

repeat_words("Hi", "Bye", times = 3)


# Function Using All Types of Parameters Together
# Question:
# Create a function user_profile(name, age=18, *hobbies, **extra_info) that:
# •	Prints the name and age.
# •	Prints all hobbies (if any).
# •	Prints any additional info passed via **kwargs.
def user_profile(name, age=18, *hobbies, **extra_info):
    print(f"Name: {name}, Age: {age}")
    if hobbies:
        for hobby in hobbies:
            print(hobby)
    if extra_info:
        for key, value in extra_info.items(): 
            print(f"{key}: {value}")
user_profile("Krishna", 18, "PUBG PC", contact=9812138040)
