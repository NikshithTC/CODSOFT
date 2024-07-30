def calculator():
    width=50
    while True:   
       print("Simple Calculator".center(width))
       print("Select an operation:")
       print("1. Addition")
       print("2. Subtraction")
       print("3. Multiplication")
       print("4. Division")
       print("5. exit")
 
    # Take input from the user
       operation = input("Enter the operation number (1/2/3/4/5): ")
 
       if operation =='5':
        print("Exiting calculator.goodbye".center(width))
        break

       if operation in ['1', '2', '3', '4']:
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))

            if operation == '1':
                result = num1 + num2
                print(f"The result of addition is: {result}")

            elif operation == '2':
                result = num1 - num2
                print(f"The result of subtraction is: {result}")

            elif operation == '3':
                result = num1 * num2
                print(f"The result of multiplication is: {result}")

            elif operation == '4':
                if num2 != 0:
                    result = num1 / num2
                    print(f"The result of division is: {result}")
                else:
                    print("Error! Division by zero is not allowed.")
        
        except ValueError:
            print("Invalid input! Please enter numeric values.")
        else:
         print("Invalid operation! Please select a valid operation number (1/2/3/4).")

if __name__ == "__main__":
    calculator()
