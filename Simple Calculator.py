from termcolor import colored

def calculator():
    print(colored("=== Simple Calculator ===","yellow"))
    print(colored("Operations: +, -, *, /","green"))
    print(colored("Type 'q' to quit\n","red"))

    while True:
        op = input("Enter operation: ").strip()
        if op.lower() == 'q':
            print("Goodbye!")
            break
        if op not in '+-*/':
            print("Invalid operation! Try again.\n")
            continue

        try:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
        except ValueError:
            print("Invalid number! Please enter numeric values.\n")
            continue

        try:
            result = None
            if op == '+': result = a + b
            elif op == '-': result = a - b
            elif op == '*': result = a * b
            elif op == '/': result = a / b
            print(f"Result: {result}\n")
        except ZeroDivisionError:
            print("Error: Cannot divide by zero!\n")


if __name__ == "__main__":
    calculator()
