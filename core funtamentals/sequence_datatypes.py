

# 1. Python Sequence Data Types

"""
sequence is a collection of the data types. it is an order collection of items, having index starting with 0.

    1. List Data Type
    2. Tuple Data Type
    3. Range Data Type

Python sequences are bounded and iterable
"""

"""
(a) Python List data types

are the most versatile compound data types. items are separated by commas and enclosed within square( [] ). similar to arrays in C or C++  list can be of different data type where as C array can store elements related to a particular data type.
"""

list = [ 'abcd', 786 , 2.23, 'john', 70.2 ]
tinylist = [123, 'john']

print (list)            # Prints complete list
print (list[0])         # Prints first element of the list
print (list[1:3])       # Prints elements starting from 2nd till 3rd 
print (list[2:])        # Prints elements starting from 3rd element
print (tinylist * 2)    # Prints list two times
print (list + tinylist) # Prints concatenated lists


"""
(b) Tuple Data Types

is another sequence data type that is similar to a list. A Python tuple consists of a number of values separated by commas. Unlike lists, however, tuples are enclosed within parentheses (...).

A tuple is also a sequence, hence each item in the tuple has an index referring to its position in the collection. The index starts from 0.

            1. Tuples can be thought of as read-only lists.
            2. tuples are enclosed in parentheses ( ( ) ) and cannot be updated (immutable). 
"""

tuple = ( 'abcd', 786 , 2.23, 'john', 70.2  )
tinytuple = (123, 'john')

print (tuple)               # Prints the complete tuple
print (tuple[0])            # Prints first element of the tuple
print (tuple[1:3])          # Prints elements of the tuple starting from 2nd till 3rd 
print (tuple[2:])           # Prints elements of the tuple starting from 3rd element
print (tinytuple * 2)       # Prints the contents of the tuple twice
print (tuple + tinytuple)   # Prints concatenated tuples

""" 
(c) Range Data Types

A Python range is an immutable sequence of numbers which is typically used to iterate through a specific number of items.

It is represented by the Range class. The constructor of this class accepts a sequence of numbers starting from 0 and increments to 1 until it reaches a specified number. Following is the syntax of the function −

            'range(start, stop, step)'

            1. start: Integer number, starting position, its optional default is 0
            2. stop:  Integer number, ending position, its mandatory
            3. step:  Integer number to specify increment, (Its optional, Default: 1)
"""

for i in range(5):  # with just stop 
  print(i)     


for i in range(2, 5): # with start and stop
  print(i)

for i in range(1, 5, 2): # with start stop and step
  print(i)


