# Simple Calculator in Python
# Performs basic arithmetic: addition, subtraction, multiplication, division


# --- Arithmetic Functions ---
# Each function takes two numbers and returns the result of the operation.

def add(a, b):
    # Returns the sum of a and b
    return a + b


def subtract(a, b):
    # Returns the difference of a and b
    return a - b


def multiply(a, b):
    # Returns the product of a and b
    return a * b


def divide(a, b):
    # Returns the quotient of a and b
    # If b is zero, returns an error message instead of crashing
    if b == 0:
        return "Cannot divide by zero"
    return a / b


# --- Input Functions ---
# These handle user input and make sure it's valid before moving on.

def get_number(prompt):
    # Keeps asking until the user types a valid number.
    # For example, typing "abc" would normally crash the program,
    # but the try/except block catches that and asks again.
    while True:
        try:
            user_input = input(prompt)
            number = float(user_input)  # Convert text to a number
            return number
        except ValueError:
            # This runs if the input can't be converted to a number
            print("Invalid input. Please enter a number.")


def get_operation():
    # Keeps asking until the user picks a valid operator: +, -, *, or /
    valid_operations = {"+", "-", "*", "/"}
    while True:
        op = input("Operation (+, -, *, /): ").strip()
        if op in valid_operations:
            return op
        print("Invalid operation. Choose +, -, *, or /.")


# --- Calculation Function ---

def calculate(a, op, b):
    # Uses a dictionary to map each operator symbol to its function.
    #
    # Instead of writing:
    #   if op == "+": return add(a, b)
    #   elif op == "-": return subtract(a, b)
    #   ...
    #
    # We store the functions in a dictionary and look them up by symbol.
    # This is cleaner and easier to extend with new operations.
    operations = {
        "+": add,
        "-": subtract,
        "*": multiply,
        "/": divide
    }

    # Look up the function by operator, then call it with a and b
    function = operations[op]
    result = function(a, b)
    return result


# --- Main Function ---

def main():
    # This is the entry point — it runs the calculator in a loop.

    print("Simple Calculator")
    print("-" * 20)

    while True:
        # Step 1: Get the first number from the user
        a = get_number("First number: ")

        # Step 2: Get the operation (+, -, *, /)
        op = get_operation()

        # Step 3: Get the second number from the user
        b = get_number("Second number: ")

        # Step 4: Perform the calculation and display the result
        result = calculate(a, op, b)
        print(f"\n{a} {op} {b} = {result}\n")

        # Step 5: Ask if the user wants to do another calculation
        again = input("Continue? (y/n): ").strip().lower()
        if again != "y":
            print("Done.")
            break  # Exit the loop and end the program


# This ensures main() only runs when the file is executed directly,
# not when it's imported as a module by another Python file.
if __name__ == "__main__":
    main()