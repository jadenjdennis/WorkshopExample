"""
ui.py
Menu text, user input handling, and dispatching a menu choice to the
correct function in operations.py.
"""

import operations

MENU = """
==== Scientific Calculator ====
 1. Add                (x + y)
 2. Subtract            (x - y)
 3. Multiply            (x * y)
 4. Divide              (x / y)
 5. Power               (x ^ y)
 6. Square Root         (sqrt x)
 7. Sine                (sin x, degrees)
 8. Cosine              (cos x, degrees)
 9. Tangent             (tan x, degrees)
10. Natural Log         (ln x)
11. Log Base 10         (log10 x)
12. Factorial           (x!)
13. Inverse Sine        (invsin x, degrees)
14. Inverse Cosine      (invcos x, degrees)
15. Inverse Tangent     (invtan x, degrees)
 0. Exit
================================
"""

# Operations that only need one number instead of two
SINGLE_INPUT_OPS = {6, 7, 8, 9, 10, 11, 12}


def get_number(prompt):
    """Keep asking until the user enters a valid number."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")


def run_operation(choice, x, y=None):
    if choice == 1:
        return operations.add(x, y)
    elif choice == 2:
        return operations.subtract(x, y)
    elif choice == 3:
        return operations.multiply(x, y)
    elif choice == 4:
        return operations.divide(x, y)
    elif choice == 5:
        return operations.power(x, y)
    elif choice == 6:
        return operations.square_root(x)
    elif choice == 7:
        return operations.sine(x)
    elif choice == 8:
        return operations.cosine(x)
    elif choice == 9:
        return operations.tangent(x)
    elif choice == 10:
        return operations.natural_log(x)
    elif choice == 11:
        return operations.log_base_10(x)
    elif choice == 12:
        return operations.factorial(x)
    elif choice == 13:
        return operations.invsin(x)
    elif choice == 14:
        return operations.invcos(x)
    elif choice == 15:
        return operations.invtan(x)
    else:
        raise ValueError("Invalid menu choice.")
