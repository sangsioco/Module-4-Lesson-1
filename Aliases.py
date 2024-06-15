# main.py

import text_utils as tu

def main():
    # Test reverse_string function
    s = "hello"
    reversed_s = tu.reverse_string(s)
    print(f"Reversed '{s}': {reversed_s}")

    # Test capitalize_string function
    s = "hello world"
    capitalized_s = tu.capitalize_string(s)
    print(f"Capitalized '{s}': {capitalized_s}")

if __name__ == "__main__":
    main()
