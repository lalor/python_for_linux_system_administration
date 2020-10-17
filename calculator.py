# Made by Subhamay Ganguly
def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    return x / y
def power(x, y):
    return x ** y
def dx(num1, num2):
    if num1 == 1:
        return 0
    else:
        return (num2 * num1) ** (num2 - 1)
def inte(num1, num2):
    if num1 == 1:
        return 1
    else:
        return (num1 ** (num2+1))/(num2+1)
def fac(num1):
    if num1==1:
        return 1
    else:
        return num1* fac(num1-1)

def fibo(num1):
    if num1==1:
        return 0
    elif num1==2:
        return 1
    else:
        return fibo(num1-1)+fibo(num1-2)
def split(num1, num2):
    return ((num1*num1)+(2*(num1*num2))+(num2*num2))

def splitt(num1, num2):
    return ((num1*num1)-(2*(num1*num2))+(num2*num2))

def qube(num1, num2):
    return ((num1*num1*num1) - (3*(num1*num1)*num2)+ (3*num1*(num2*num2)) - (num2*num2*num2))

def qub(num1, num2):
    return ((num1*num1*num1) + (3*(num1*num1)*num2) + (3*num1*(num2*num2)) + (num2*num2*num2))

def root(x, y):
    return x ** y

def sq(x):
    return x**2

def qu(x):
    return x**3

def byx(x):
    return 1/x

def percen(num1,num2):
    return ((num1/num2)*100)

while True:
    print("                                             Calculator  By   STREIN")
    print("  ")
    print("1. Normal Calculator", end="    ")
    print("2. Scientific Calculator\n")
    print("C -- Cancel")
    choice = input("Enter Your choice [1/2]: ")
    if choice in ('1', '2', 'c'):
        if choice == '1':
            while True:
                print("  ")
                print("Select operation :")
                print("1.Addition", end="   ")
                print("2.Subtract", end="   ")
                print("3.Multiply", end="   ")
                print("4.Divide", end="   ")
                print("5.Power", end="   ")
                print("6.Square", end="   ")
                print("7.Qube", end="   ")
                print("8.%\n")
                print("Exit --  x")
                choice = input("Enter Your choice [1/2/3/4/5/6/7/8]: ")
                if choice in ('1', '2', '3', '4', '5', 'x', '6', '7', '8'):
                    if choice == '1':
                        num1 = float(input("Enter First Number :"))
                        num2 = float(input("Enter Second Number :"))
                        print(" ")
                        print(num1, "+", num2, "=", add(num1, num2))
                    elif choice == '2':
                        num1 = float(input("Enter First Number :"))
                        num2 = float(input("Enter Second Number :"))
                        print(" ")
                        print(num1, "-", num2, "=", subtract(num1, num2))
                    elif choice == '3':
                        num1 = float(input("Enter First Number :"))
                        num2 = float(input("Enter Second Number :"))
                        print(" ")
                        print(num1, "*", num2, "=", multiply(num1, num2))
                    elif choice == '4':
                        num1 = float(input("Enter First Number :"))
                        num2 = float(input("Enter Second Number :"))
                        print(" ")
                        print(num1, "/", num2, "=", divide(num1, num2))
                    elif choice == '5':
                        num1 = float(input("Enter First Number :"))
                        num2 = float(input("Enter Second Number :"))
                        print(" ")
                        print(num1, "^", num2, "=", power(num1, num2))
                    elif choice == '6':
                        num1 = float(input("Enter Your Number :"))
                        print(" ")
                        print("Your Answer is --",sq(num1))
                    elif choice == '7':
                        num1 = float(input("Enter Your Number :"))
                        print(" ")
                        print("Your Answer is --",qu(num1))
                    elif choice == '8':
                        num1 = int(input("Enter Number That you Get :"))
                        num2 = int(input("Out Of :"))
                        print(" ")
                        print("Your Answer is :", percen(num1, num2))
                    elif choice == 'x':
                        import cal3
                        break
                    else:
                        print("Invalid Input")
        elif choice == '2':
            while True:
                print(" ")
                print("1.Derivative", end="   ")
                print("2.Integration", end="   ")
                print("3.Factorial", end="   ")
                print("4.Fibonacci", end="   ")
                print("(A+B)^2 -- '5'", end="   ")
                print("(A-B)^2 -- '6'", end="   ")
                print("(A-B)^3 -- '7'", end="   ")
                print("(A+B)^3 -- '8'")
                print("'9' -- Root", end="   ")
                print("'b' -- 1/x\n")
                print("Exit -- 'x'")
                choice = input("Enter Your choice [1/2/3/4/5/6/7/8/9]: ")
                if choice in ('1', '2', '3', '4', '5', '6', '7', '8', '9', 'x', 'b'):
                    if choice == '1':
                        num1 = float(input("Enter First Number :"))
                        num2 = float(input("Enter Second Number :"))
                        print(" ")
                        print("Your Answer is --",dx(num1, num2))
                    elif choice == '2':
                        num1 = float(input("Enter First Number :"))
                        num2 = float(input("Enter Second Number :"))
                        print(" ")
                        print("Your Answer is --",inte(num1, num2))
                    elif choice == '3':
                        num1 = float(input("Enter First Number :"))
                        print(" ")
                        print("Factorial Is :", fac(num1))
                    elif choice == '4':
                        num1 = float(input("Enter First Number :"))
                        print(" ")
                        print("Your Answer is --",fibo(num1))
                    elif choice == '5':
                        num1 = float(input("Enter First Number :"))
                        num2 = float(input("Enter Second Number :"))
                        print(" ")
                        print("Your Answer is --",split(num1, num2))
                    elif choice == '6':
                        num1 = float(input("Enter First Number :"))
                        num2 = float(input("Enter Second Number :"))
                        print(" ")
                        print("Your Answer is --",splitt(num1, num2))
                    elif choice == '7':
                        num1 = float(input("Enter First Number :"))
                        num2 = float(input("Enter Second Number :"))
                        print(" ")
                        print("Your Answer is --",qube(num1, num2))
                    elif choice == '8':
                        num1 = float(input("Enter First Number :"))
                        num2 = float(input("Enter Second Number :"))
                        print(" ")
                        print("Your Answer is --",qub(num1, num2))
                    elif choice == '9':
                        num1 = float(input("Enter Your Number :"))
                        print(" ")
                        print("Your Answer is --",root(num1, (1 / 2)))
                    elif choice == 'b':
                        num1 = float(input("Enter Your Number :"))
                        print(" ")
                        print("Your Answer is --", byx(num1))
                    elif choice == 'x':
                        import cal3
                        break
                    else:
                        print("Invalid Input")
        elif choice == 'c':
            import strein
        else:
            print("Invalid Input")
