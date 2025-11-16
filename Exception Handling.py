print("Welcome To Except Handler")

def demonstrate_exceptions():
    print("\n--- 1. ArithmeticException (ZeroDivisionError) ---")
    try:
        numerator = 100
        denominator = 0
        result = numerator / denominator
    except ZeroDivisionError as e:
        print(f"Caught Arithmetic error: {e}")
    except ArithmeticError as e:
        print(f"Caught broader ArithmeticError: {e}")

    print("\n--- 2. NullPointerException (AttributeError / TypeError) ---")
    obj = None
    try:
        obj.upper()
    except AttributeError as e:
        print(f"Caught Null-pointer-like error (AttributeError): {e}")

    try:
        _ = obj[0]
    except TypeError as e:
        print(f"Caught Null-pointer-like error (TypeError): {e}")

    print("\n--- 3. NumberFormatException (ValueError) ---")
    user_input = "12ab"
    try:
        number = int(user_input)
        print(f"Converted number: {number}")
    except ValueError as e:
        print(f"Caught NumberFormat error: {e}")

    print("\n--- 4. ArrayIndexOutOfBoundsException (IndexError) ---")
    my_list = [10, 20, 30]
    try:
        value = my_list[5]
        print(f"Value at index 5: {value}")
    except IndexError as e:
        print(f"Caught Index out-of-bounds error: {e}")

    finally:
        print("All exception demos finished.\n")

if __name__ == "__main__":
    demonstrate_exceptions()