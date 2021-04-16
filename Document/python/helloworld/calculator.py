#  calculator project 16 /04 / 21

def add(x,y):
    return x + y

def subtract(x,y):
    return x - y

def multiply(x,y):
    return x * y 

def devide(x,y):
    return x / y 

print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Devide")

while True:

    choice = input("Enter your choice(1/2/3/4): ")
    if choice in ('1', '2', '3', '4'):
        number1 = float(input("Enter first number:" ))  # num1 and num2 i have changed the float number to a integer 
        number2 = float(input("Enter second number: "))    # you can either user int for base 10 num or float for decimals
        if choice == '1':
            print(number1, "+", number2, "=", add(number1, number2))
        elif choice == '2':
            print(number1, "-", number2, "=", subtract(number1, number2))
        elif choice == '3':
            print(number1, "*", number2, "=", multiply(number1, number2))
        elif choice == '4':
            print(number1, "/", number2, "=", devide(number1, number2))
        break
    else:
        print("Entered input is invalid")

