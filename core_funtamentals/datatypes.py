
# Python data types

"""

the data types are used to define the type of a variable. It represents the type of data we are going to store in a variable and determines what operations can be done on it.

 # Numberic Data Types

    1. int
    2. flot
    3. complex

"""

var1 = 1       # int data type
var2 = True    # bool data type
var3 = 10.023  # float data type
var4 = 10+3j   # complex data type


# string Data type

"""

 is a sequence of one and more unicode characters, enclosed in single, double or triple quotations marks. python skills are immutable which means when you perform an operation on strings, you always produce a new string object of the same type, rather than mutating an existing string.

"""

str1 = 'python'
str2 = "python"
str3 = '''python'''

""" 
you can't perfrom arithemetic operations on strings, but you can use operations like silcing and concatenation

    1. Subsets of strings can be taken using the slice operator ([ ] and [:] ) with indexes starting at 0 in the beginning of the string and working their way from -1 at the end.

    2. The plus (+) sign is the string concatenation operator and the asterisk (*) is the repetition operator in Python.
"""

str = 'Hello World!'

print (str)          # Prints complete string
print (str[0])       # Prints first character of the string
print (str[2:5])     # Prints characters starting from 3rd to 5th
print (str[2:])      # Prints string starting from 3rd character
print (str * 2)      # Prints string two times
print (str + "TEST") # Prints concatenated string