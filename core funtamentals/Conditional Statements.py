
# Conditional Statements

"""
Conditional statements in python are used to execute certain blocks of code based on specific conditions. These statements help control the flow of a program, making it behave differently in different situations.

(a). if Conditional Statements is simplest form of a conditional statements it executes a block if the given condition is true.

if(condition):
True             # This block will execute

"""

age = 20
if age >= 18:
    print("Eligible to vote.")  


"""
(b). if else Conditional Statement allow us to specify a block of code that will execute if the conditions associated with an if or elif statement evaluates to false. else block provides a way to handle all other cases that don't meet the specified conditions.


"""

rate = 10
if age <= 12:
    print("Travel for free.")
else:
    print("Pay for ticket.")


# short handed if-else

# The short-hand if-else statement allows us to write a single-line if-else statement.

marks = 45

res = "Pass" if marks >= 40 else "fail"
print(f"Result: {res}")

"""
Note: This method is also known as ternary operator. Ternary Operator essentially a shorthand for the if-else statement that allows us to write more compact and readable code, especially for simple conditions.
"""

"""
(c). elif statement in python stands for "else if". it allows us to check multiple conditions, providing a way to execute different blocks of code based on which condition is true.Using elif statements makes our code more readable and efficient by eliminating the need for multiple nested if statements.

"""

age = 25

if age <= 12:
    print("Child.")
elif age <= 19:
    print("Teenager.")
elif age <= 35:
    print("Young adult.")
else:
    print("Adult.")

"""

The code checks the value of age using if-elif-else. Since age is 25, it skips the first two conditions (age <= 12 and age <= 19), and the third condition (age <= 35) is True, so it prints "Young adult.".
"""

"""
(d). Nested if..else Conditional Statement means an if else statement inside another if statement. We can use nested if statements to check conditions within conditions


"""

age = 70
is_member = True

if age >= 60:
    if is_member:
        print("30% senior discount!")
    else:
        print("20% senior discount.")
else:
    print("Not eligible for a senior discount.")