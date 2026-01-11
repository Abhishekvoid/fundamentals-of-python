
# example: 1

class division:
    def maths():
        try:
            num1 = int(input("first numebr: "))
            num2 = int(input("second number: "))
            result = num1 /  num2
            return result
        except ValueError:
            print("please enter a valid number")
            return False
        except ZeroDivisionError:
            print("cannot divide by zero!")
            return False

cal = division.maths()
print(cal)

# example 2: Tuple of Excepations

class multi:
    def maths_multi():
        try:
            num1 = int(input("first numebr: "))
            num2 = int(input("second number: "))
            result = num1 *  num2
            return result
        except (ValueError, ZeroDivisionError) as e:
            print(f"math error", e)

cal_multi = multi.maths_multi()
print(cal_multi)

# example 3:



class InsufficientBalance(Exception):

    pass
class Payment:

    def paymentfailerror(self, amount):

        balance = 900

        if amount > balance:
               raise InsufficientBalance(f"Need ${amount}, have ${balance}")
        print(f"✅ Payment ${amount} processed")
        return True

processor = Payment()
try:
    processor.paymentfailerror(1000)
except InsufficientBalance as e:
    print({e})

