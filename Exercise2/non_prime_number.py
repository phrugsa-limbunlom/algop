from invalid_number_exception import InvalidNumberException


def is_prime_number(number):
    list_of_number = [2, 3, 5, 7]

    count_prime = 2
    for i in list_of_number:
        if number != i and number % i == 0:
            count_prime += 1

    return count_prime <= 2


def find_non_prime_number(num1, num2):
    num1, num2 = int(num1), int(num2)
    non_prime_number = []
    if num2 < num1:
        num1, num2 = num2, num1

    for i in range(num1, num2 + 1):
        if not is_prime_number(i):
            non_prime_number.append(i)

    return non_prime_number


def format_output(non_prime_list):
    output = ""
    count = 0
    for i in non_prime_list:
        if count == 9:
            output += str(i) + "\n"
            count = 0

        output += str(i) + " "
        count += 1

    return output


def validate_input_number(num1, num2):
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
