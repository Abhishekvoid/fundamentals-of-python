
"""
Loops in Python are used to repeat actions efficiently. The main types are For loops (counting through items) and While loops (based on conditions).
"""

# 1. For loop

"""
For loop is used iterate over a sequence such as list, tuple, string and range. it allow to excute a block of code repeatedly, once for each item in the sequence.
"""

n= 4
for i  in range (n):
    print(i)


"""
 This code prints the numbers from 0 to 3 (inclusive) using a for loop that iterates over a range from 0 to n-1 (where n = 4).
"""

# Iterating Over List, Tuple, String and Dictionary Using for Loops in Python

li = ["geeks", "for", "geeks"]
for x in li:
    print(x)
    
tup = ("geeks", "for", "geeks")
for x in tup:
    print(x)
    
s = "abc"
for x in s:
    print(x)
    
d = dict({'x':123, 'y':354})
for x in d:
    print("%s  %d" % (x, d[x]))
    
set1 = {10, 30, 20}
for x in set1:
    print(x),

# Iterating by Index of Sequences

li = ["geeks", "for", "geeks"]
for index in range(len(li)):
    print(li[index])


# 2. While loop

"""

a while is used to execute a block of statements repeatedly until a given condition is statisfied.When the condition becomes false, the line immediately after the loop in the program is executed.
"""

count = 0

while (count < 3):
    count = count+ 1
    print("hii!")


# infinite While loop

# while (True):
#     print("Hello Geek")

# """
#     'while' loop with the condition "True", which means that the loop will run infinitely 
# """

for i in range(1, 5):
    for j in range(i):
        print(i, end=" ")
    print()