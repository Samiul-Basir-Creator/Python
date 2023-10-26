# Addition
def add(x, y):
    return x + y

# Subtraction
def subtract(x, y):
    return x - y

# Multiplication
def multiply(x, y):
    return x * y

# Division
def divide(x, y):
    if y == 0:
        return "Cannot divide by zero"
    return x / y

# Main function
def main():
    count =0
    while(count==0):
        
        print("Calculator:")
        print("1. Addition")
        print("2. Substraction")
        print("3. Multiplication")
        print("4. Division")
       
        choice = input("What would you like to do? \n(1/2/3/4) or Exit: ")
        if choice == "Exit" or choice=="exit":
            count = 1
        else:

            x = float(input("Enter the first number: "))
            y = float(input("Enter the second number: "))
            if choice == '1':
                print("Addition:", add(x, y))
            elif choice == '2':
                print("Subtraction:", subtract(x, y))
            elif choice == '3':
                print("Multiplication:", multiply(x, y))
            elif choice == '4':
                print("Division:", divide(x, y))
            else:
               print("Invalid input")

main()
