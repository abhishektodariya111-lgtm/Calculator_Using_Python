# def show_menu():
    #print the Calculator menu


# def add(a , b):
#     # return the sum
#     return a + b

# def main():
    # call show_menu()
    # ask the user for a choice
    # if choice == 1:
    #     ask for two numbers
    #     print the result using add()
    # elif choice == 8:
    #     exit

def show_menu():
    print("===== Calculator =====")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. floor division")
    print("6. Square")
    print("7. Exit")

def add(a , b):
    return a + b
def subtract(a , b):
    return a - b
def Multiply(a , b):
    return a * b
def Divide(a , b):
    return a / b
def Floor_Division(a , b):
    return a // b
def Square(a , b):
    return a * b
    

def main():
    while True:
        show_menu()

        choice = int(input("What You Want To Calculate , Enter Your Choice: "))

        if choice == 1:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            answer = add(num1, num2)

            print("Answer =", answer)


        elif choice == 2:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            answer = subtract(num1, num2)

            print("Answer =", answer)


        elif choice == 3:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            answer = Multiply(num1, num2)

            print("Answer =", answer)

  

        elif choice == 4:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            answer = Divide(num1, num2)

            print("Answer =", answer)


        elif choice == 5:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            answer = Floor_Division(num1, num2)

            print("Answer =", answer)


        elif choice == 6:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            answer = Square(num1, num2)

            print("Answer =", answer)

    

        elif choice == 7:
            exit
    
        else :
            print("Invalid Choice")

main()