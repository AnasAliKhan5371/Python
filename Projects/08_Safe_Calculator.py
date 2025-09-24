# Exception Handling
#simple command-line calculator that handles common errors using try-except blocks.
def calc():
    while True:
        try:
            num_1=input("Enter first number: ")
            if num_1.lower()=='exit':
                break
            num_1=float(num_1)

            op=input("Enter operator (+, -, *, /) : ")
            if op.lower()=='exit':
                break
            if op not in ['+','-','*','/']:
                print("ERROR: Invalid operation. Use +, _, * or / .")
                continue

            num_2 = input("Enter second number: ")
            if num_2.lower() == 'exit':
                break
            num_2 = float(num_2)

            if op == '+':
                result = num_1 + num_2
            elif op == '-':
                result = num_1 - num_2
            elif op == '*':
                result = num_1 * num_2
            elif op == '/':
                result = num_1 / num_2

            print(f"☑️ Result : {result}\n")

        except ValueError:
            print("❌ ERROR: Invalid input. Please enter a valid number.\n")
        except ZeroDivisionError:
            print("❌ ERROR: Cannot divide by zero. Please try again.\n")
        except Exception as e:
            print(f"An unexpected error occurred: {e}\n")
    print("\nCalculator closed. Goodbye!")

if __name__=="__main__":
    calc()