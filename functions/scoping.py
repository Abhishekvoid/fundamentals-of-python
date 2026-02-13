
def customer():

    customer_name  = "fish" # enclosing varaible

    def customer_1():

        customer_name = "cat"  # local varaible only can be used inside this function and it can't inhert like class

        print(f"inside innner function {customer_name}")  # will not change the value of enclosing customer_name output: inside innner function cat

    customer_1()

    print(f"this outer main function {customer_name}") # output: this outer main function dog


customer_name = "dog" # global

customer()


# using nonlocal variable

def robot_function():

    current_function = "follow me"

    # using global will allow ot access and change this varaible anywhere in the program 
    global follow_me
    follow_me = "depth camera"

    print(f"inside the robot function and varaible is global: {follow_me}")

    print(f"enclosing before nonlocal: {current_function}")

    def robot_function_2():
        
        # nonlocal means use the variable from the nearest outer function
        nonlocal current_function  

        # now this will change the value of current_function to "slam mapping"
        current_function = "slam mapping"

        print(f"using nonlocal variable: {current_function}")
    
    robot_function_2()

    print(f"enclosing variable after nonlocal: {current_function}") # wil print changed value "slam mapping"


robot_function()


# changing the follow_me variable from robot_function outside if its scope
follow_me = "UWB module"
print(f"access and changing the gobal variable out side the function scope: {follow_me}")