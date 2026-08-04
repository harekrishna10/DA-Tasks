# 1) Baic Arithmetic and Type identification
# i. Create three variables: one integer, one float and one complex number.
var_int = 10
var_float = 3.7
var_complex = 2 + 3j
# ii. Print each varibale and use the type() function to confirm their data types.
print(var_int)
print(var_float)
print(var_complex)
print(var_int,type(var_int))
print(var_float,type(var_float))
print(var_complex,type(var_complex))

# 2) Arithmetic with mixed types
# i. create one int variable (a) and one float variable (b).
a = 17
b = 36.69
# ii. Print the sum, difference, product and quotient of a and b.
sum = a + b
difference = a - b
product = a * b
quotient = a / b
print("Sum:", sum)
print("Difference:", difference)
print("Product:", product)
print("Quotient:", quotient)

# iii. print the type() of each result (notice how types may changes)
print(type(sum))
print(type(difference))
print(type(product))
print(type(quotient))

# 3) Comparison Operators
# i. let x = 10 and y = 7
x = 10
y = 7
# ii. print the result of x>y, x<y, x==y, and x!=y
print(x > y) # this will print True since 10 is greater than 7.
print(x < y) # this will print False since 10 is not less than 7.
print(x == y) # this will print False since 10 is not equal to 7.
print(x != y) # this will print True since 10 is not equal to 7.
# iii. After observing the output, explain why each result is True or False in comments.

# 4) Boolean Variables
# •	Define a variable status = True.
# •	Print the value of status and confirm it is a boolean using type(status).
# •	Reassign status to False and confirm its type again.

status = True
print(status)
print(type(status))
status = False
print(type(status))

# 5) String Creation and length
# •	Create a string variable, for example text = "Hello World".
# •	Use len(text) to print its length.
# •	Use type(text) to verify it is a string.
text = "Hello World"
print(len(text))
print(type(text))

# 6) String Indexing
# •	With the string s = "Python", print each character. Then print just the first and last characters using negative indexing.
s = 'python'
print(s)
print(s[0])
print(s[-1])

# 7) String Slicing
# •	Let lang = "Programming".
# •	Print the substring from index 0 to index 4.
# •	Print the substring from index 3 to the end.
# •	Print the substring that omits the first 2 and last 2 characters.
lang = "Programming"
print(lang[0:4])
print(lang[3:])
print(lang[2:-2])

# 8) Exploring len() on Slices
# •	Continue using lang = "Programming".
# •	Slice lang to get "Program" and store it in a variable part1.
# •	Print len(part1) and comment how it differs from len(lang).
print(len(lang))
part1 = lang[0:7]
print(len(part1)) # it is different from the len(lang) since it is (substring)part of lang.

# 9) String Methods - case conversion
# •	Let phrase = "Hello, Python!".
# •	Print phrase.upper() and phrase.lower().
# •	Print the original phrase to show it remains unchanged (strings are immutable).
phrase = "Hello, Python!"
print(phrase.upper())
print(phrase.lower())
print(phrase)

# 10) Combining Strings
# •	Create two strings, str1 = "Data" and str2 = "Science".
# •	Combine them into a single string with a space in between and print it.
# •	Print the length of the combined string.
str1 = "Data"
str2 = "Science"
str3 = str1 + " " + str2
print(str3)
print(len(str3))

# 11) In-Place vs. Reassignment with String Methods
# •	Let word = "example".
# •	Call word.upper() but do not store it, then print word.
# •	Now set word = word.upper(), then print word.
# •	Comment on why the second print is different from the first.
word = "example"
word.upper()
print(word)
word = word.upper()
print(word) # second print is different from first because in first print we just use upper() where in second print we store the word.upper() value in word which executed properly.

# 12) Arithmetic Operator Precedence
# •	Define a = 5, b = 3, c = 2.
# •	Print the result of the expression a + b * c.
# •	Print the result of (a + b) * c.
# •	In comments, explain how operator precedence affects the outcome.
a = 5
b = 3
c = 2
result1 = a + b * c
print(result1) # here, first b is multiplied with c and then added result to a.
result2 = (a + b) * c 
print(result2) # here, first a is added to b, then result is multiplied to c.

# 13) String Index Out of Range
# •	Let text = "Hello".
# •	Attempt to access an index that doesn’t exist, like text[10].
# •	Observe the error message (IndexError) and explain why it happens in comments.
text = "Hello"
# print(text[10]) # error occurs because text has it index range from 0 to 4 only.

# 14) Equality vs. Identity Check (Conceptual Explanation)
# •	Create two variables with the same string value, s1 = "test" and s2 = "test".
# •	Use the == operator to compare them, then use the is operator.
# •	Explain in comments what each comparison checks.
s1 = "test"
s2 = "test"
print(s1 == s2) # this cheks if all the elements of s1 is same as s2 or not.
print(s1 is s2) # this checks if s1 is itself s2 or not.

# 15) Creating and Checking a Complex Number
# •	Define z = 3 + 4j.
# •	Print the real part (z.real) and the imaginary part (z.imag).
# •	Confirm that its type is complex using type(z).
z = 3 + 4j
print("this is real part:", z.real)
print("this is imageinary part:", z.imag)
print(type(z))

# 16) Comparisons with Floats
# •	Let f1 = 0.1 + 0.2 and f2 = 0.3.
# •	Print f1 == f2.
# •	Print the actual values of f1 and f2 to explain any difference in the comparison outcome (floating-point precision).
f1 = 0.1 + 0.2
f2 = 0.3
print(f1 == f2) # the result is false because of the representation of decimal number
print(f1)
print(f2)
