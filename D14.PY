def main():
    try:
        # NameError example
        print(undefined_variable)
    except NameError:
        print("NameError: The variable is not defined.")

    try:
        # TypeError example
        x = "five"
        y = 2
        result = x + y
    except TypeError:
        print("TypeError: Unsupported operation between different data types.")

if _name_ == "_main_":
    main()

In this program, we have two separate try-except blocks. The first block attempts to print an undefined variable undefined_variable, which raises a NameError. The exception is caught, and a custom message is printed indicating that the variable is not defined.

The second block attempts to add a string and an integer (x + y), which would result in a TypeError. The exception is caught, and a custom message is printed indicating that the operation between different data types is unsupported.

When you run the program, it will output:
NameError: The variable is not defined.
TypeError: Unsupported operation between different data types.