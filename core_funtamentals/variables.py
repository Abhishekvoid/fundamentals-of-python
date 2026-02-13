
# Python Variables

"""
    Variables are used to reserved memory locations used to store values, When you create a variable it will reserve space in the memory

    Based on the datatypes of the variables, memory space is allocate to it, python have different type of data types to store intergerts. decimals or characters in variables

    Each variable assigned some memory loacation and this location is the memory address of the variable.which is reprensted in binary form, data also stored in the binary. it stores the object in a randomly chosen memory location. you can access this address and location using "Id()" function which returns the address of the object
"""

month = "may"
age = 18

print("id of month", id(month), "id of age", id(age))


# Creating Python Variables

# creates different types (an integer, a float, and a string) of variables.

counter = 100          # Creates an integer variable
miles   = 1000.0       # Creates a floating point variable
name    = "Zara Ali"   # Creates a string variable

# print those variables

print(counter)
print(miles)
print(name)

# delete this variables

del counter
print("now deleted",) # gives error NameError: name 'counter' is not defined

# Getting Type of a Variable

print(type(month))
print(type(miles))
print(type(age))

# Casting Python Variables

"""You can specify the data type of a variable"""

x = str(10)     # x = '10'  string
y = int(10)     # y = 10    integers
z = float(10)   # z = 10.0 decimals


# Case-Sensitivity of Python Variables

rate = 10
Rate = 30

'this both with be different variables, those case sensitive'

# multiple assignment'

a=10
b=10
c=10

# instead you can 

a = b = c = 10

# or

a,b,c = 10,20,30


# Python naming convention

"""
    Every Python variable should have a unique name like a, b, c. A variable name can be meaningful like color, age, name etc

    1. name must start with a letter or underscore character
    2. name cannot start with a number or special character like $, (, *, % etc.
    3. name can only contain alpha-numeric characters and underscores
    4. Python variable names are case-sensitive 

    #. Camel case - First letter is a lowercase, but first letter of each subsequent word is in uppercase. For example: kmPerHour, pricePerLitre

    #. Pascal case - First letter of each word is in uppercase. For example: KmPerHour, PricePerLitre

    #. Snake case - Use single underscore (_) character to separate words. For example: km_per_hour, price_per_litre
"""

counter = 100
_count  = 100
name1 = "Zara"
name2 = "Nuha"
Age  = 20
zara_salary = 100000