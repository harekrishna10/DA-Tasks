# 1. Encapsulation
# •	Create a class Person with private attributes __name and __age.
# •	Use getter and setter methods to access and modify these values.
class Person:
    def __init__(self,name,age):
        self.__name = name  
        self.__age = age  
    def get_name(self):
        return self.__name
    def get_age(self):
        return self.__age
    
    def set_name(self, name):
        self.__name = name
    def set_age(self, age):
        if age > 0:
            self.__age = age
        else:
            print("Please enter a valid age.")
    def __str__(self):
        return f"Person (Name: {self.__name}, Age: {self.__age})"
    
p = Person("Harekrishna", 24)
print(p)  
p.set_name("Krishna")
p.set_age(25)
print(f"Updated Name: {p.get_name()}")
print(f"Updated Age: {p.get_age()}")


# 2. Polymorphism
# •	Create a function show_details(obj) that works with different classes.
# •	Define the same method name (details()) in two or more classes.
# •	Call show_details() with different objects to show polymorphism.
class show_details:
    def details(self):
        print("My temporary address is Sallaghari-Bhaktapur.")

class show_p_details:
    def details(self):
        print("My permanent addresss is Lalbandi-Sarlahi.")
sd = show_details()
spd = show_p_details()
sd.details()
spd.details()


# 3. Single Inheritance
# Create a base class Vehicle with a method start().
# Create a derived class Bike that inherits from Vehicle.
# •	Bike should have its own method wheels() that prints "Two wheels".
class vehicle:
    def start(self):
        return "Vehicle starts with key."
class bike(vehicle):
    def wheels(self):
        return "Bike has two wheels."
v = vehicle()
print(v.start())
b = bike()
print(b.wheels())
print(b.start())


# 4. Multiple Inheritance
# Create class Singer with method sing() and class Dancer with method dance().
# •	Create a class Performer that inherits from both.
# •	Create a Performer object and call both methods.
class singer:
    def sing(self):
        return "Singer sings a song."
class dancer:
    def dance(self):
        return "Dancer dances on a song."
class performer(singer,dancer):
    def perform(self):
        return "Performer sing also and dance also."
s = singer()
print(s.sing())
d = dancer()
print(d.dance())
p = performer()
print(p.perform())
print("\nInheritanting from singer and dancer\n")
print(p.sing())
print(p.dance())


# 5. Hierarchical Inheritance
# Create a base class Appliance.
# •	Create two child classes: WashingMachine and Microwave.
# •	WashingMachine should have a method wash(), and Microwave should have a method heat().
# •	Create objects of both and call their respective methods.
class Appliance:
    def homeuses(self):
        return "Appliances are used for household purposes."
    
class Washingmachine(Appliance):
    def wash(self):
        return "Washing machine washes clothes."
        
class Microwaave(Appliance):
    def heat(self):
        return "Microwave produces heat."
a = Appliance()
print(a.homeuses())

print("\n***Inheritating from Applicances by multiple chile classes Washing machine and microwav.*** \n")

w = Washingmachine()
print(w.wash())
print(w.homeuses())
m = Microwaave()
print(m.heat())
print(m.homeuses())

# 6. Polymorphism Using a Loop
# Create classes Pen and Pencil, both with a method write().
# •	Loop through a list of objects (Pen and Pencil) and call write() on each object.
class pencil:
    def write(self):
        print("We can write with pencil and erase with eraser.")
class pen:
    def write(self):
        print("We can write with pen but we cannot erase with eraser.")

my_pencil = pencil()
my_pen = pen()

write_with = [my_pencil,my_pen]

for i in write_with:
    i.write()


# 7. Use Encapsulation to Protect Age
# Create a class Person with private attribute __age.
# •	Use set_age() to set the age.
# •	If age is less than 0, print "Invalid age".
# •	Use get_age() to return the age.
class Person:
    def __init__(self, age):
        self.__age = 0 
        self.set_age(age)
    def get_age(self):
        return self.__age
    def set_age(self, age):
        if age < 0:
            print("Invalid age")
        else:
            self.__age = age
p = Person(25)
print(f"Initial age: {p.get_age()}")
p.set_age(-8)
print(f"Age after attempt: {p.get_age()}")


# 8. Company Structure
# Create class Company with method company_name().
# •	Create class Department that inherits Company and adds department_name().
# •	Create class Employee that inherits Department and adds employee_name().
# •	Create an Employee object and call all the methods.
# Base Class (Grandparent)
class Company:
    def company_name(self):
        print("Company Name: Mindrisers Institute of Technology")
class Department(Company):
    def department_name(self):
        print("Department Name: Python with DATA SCIENCE")
class Employee(Department):
    def employee_name(self):
        print("Employee Name: Sir Nabin Katwal")
emp = Employee()
emp.company_name()
emp.department_name()
emp.employee_name()

# 9. Lambda to check if a Number is Positive
# Write a lambda function that takes a number and returns True if it is positive, otherwise False.
# •	Test it with different values like 5, -3, and 0
# num = int(input("Enter the number:"))
check = lambda num : num if num > 0 else "Enter the positive number."
print(check(8))
print(check(0))
print(check(-9))

# 10. Lambda to Get First Character of a String
# Create a lambda function that takes a string and returns its first character.
# •	Example: "apple" → 'a'
# Lambda function that takes a string 's' and returns the character at index 0

char = lambda s: s[0] if len(s) > 0 else ""
print(char("apple"))
print(char("Python"))
print(char("DataScience"))


# 11. Add 10 to All List Elements
# Given a list [1, 2, 3, 4, 5],
# •	Use map() and lambda to return a new list where 10 is added to each number.
l = [1,2,3,4,5]
total = list(map(lambda l: l + 10,l))
print(total)

# 12. Get Length of Each Word
# Given a list ["apple", "banana", "kiwi"],
# •	Use map() and lambda to return a list of lengths of each word.
# → Output: [5, 6, 4]
l2 = ["apple","banana","kiwi"]
length = list(map(lambda l2: len(l2),l2))
print(length)


# 13. Filter Numbers Greater Than 50
# Given a list [10, 55, 60, 23, 90],
# •	Use filter() and lambda to return only the numbers greater than 50.
l3 = [10,55,60,23,90]
greater = list(filter(lambda l3: l3 > 50,l3))
print(greater)

# 14.Create a Word by Joining Letters
# Given a list of letters ['P', 'Y', 'T', 'H', 'O', 'N'],
# •	Use reduce() and lambda to join them into a single word: "PYTHON".
import functools
l4 = ['P','Y','T','H','O','N']
combine = functools.reduce(lambda x,y: x + y,l4)
print("Combined output is:",combine)