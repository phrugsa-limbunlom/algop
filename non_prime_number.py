class InvalidNumberException(Exception):
    """
    Custom exception for invalid number inputs
    """
    def __init__(self, message):
        super().__init__(message)


def is_prime_number(number: int) -> bool:
    """
    Determines if a number is prime using basic divisibility test.

    Parameters:
    number (int): Number to check for primality

    Returns:
    bool: True if number is prime, False otherwise
    """
    list_of_number = [2, 3, 5, 7]

    count_prime = 2
    for i in list_of_number:
        if number != i and number % i == 0:
            count_prime += 1

    return count_prime <= 2


def find_non_prime_number(num1: str, num2: str) -> list:
    """
    Finds all non-prime numbers in given range.

    Parameters:
    num1 (str): Lower bound of range as string
    num2 (str): Upper bound of range as string

    Returns:
    list: List of non-prime numbers in range
    """
    num1, num2 = int(num1), int(num2)
    if num2 < num1:
        num1, num2 = num2, num1

    non_prime_number = [i for i in range(num1, num2 + 1) if not is_prime_number(i)]
    return non_prime_number


def format_output(non_prime_list: list) -> str:
    """
    Formats list of numbers in rows of 10.

    Parameters:
    non_prime_list (list): List of numbers to format

    Returns:
    str: Formatted string with numbers in rows of 10
    """
    output = ""
    count = 0
    for i in non_prime_list:
        if count == 9:
            output += str(i) + "\n"
            count = 0

        output += str(i) + " "
        count += 1

    return output


def validate_input_number(num1: str, num2: str) -> bool:
    """
    Validates if inputs are positive integers.

    Parameters:
    num1 (str): First number to validate
    num2 (str): Second number to validate

    Returns:
    bool: True if both inputs are valid
    
    Raises:
    InvalidNumberException: If either input is invalid
    """
    if not num1.isnumeric():
        print(f"input number 1 '{num1}' must be numeric")
        raise InvalidNumberException(f"Invalid input number! : {num1}")
    if not num2.isnumeric():
        print(f"input number 1 '{num2}' must be numeric")
        raise InvalidNumberException(f"Invalid input number! : {num2}")
    if int(num1) < 0:
        print(f"input number 1 '{num1}' must be positive")
        raise InvalidNumberException(f"Invalid input number! : {num1}")
    if int(num2) < 0:
        print(f"input number 2 '{num2}' must be positive")
        raise InvalidNumberException(f"Invalid input number! : {num2}")

    return True


if __name__ == '__main__':
    number1 = input("input number 1 : ")
    number2 = input("input number 2 : ")

    is_valid = validate_input_number(number1, number2)

    if is_valid:
        list_of_non_prime_number = format_output(find_non_prime_number(number1, number2))
        print(f"A list of all non-prime numbers is \n{list_of_non_prime_number}")
