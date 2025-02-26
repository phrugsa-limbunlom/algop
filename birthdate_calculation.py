from datetime import datetime


class InvalidBirthDateException(Exception):
    """
    Custom exception for invalid birth date inputs
    """
    def __init__(self, message):
        super().__init__(message)


class BirthDate:
    """
    Handles birth date operations including format conversion and age calculation
    """
    def __init__(self, date: str):
        """
        Initialize BirthDate object.

        Parameters:
        date (str): Date string in MM/DD/YYYY format
        """
        self.date = date

    def change_to_european_format(self) -> str:
        """
        Converts US date format to European format.

        Returns:
        str: Date string in DD/MM/YYYY format
        """
        input_date = datetime.strptime(self.date, '%m/%d/%Y').date()
        return input_date.strftime("%d/%m/%Y")

    def calculate_age(self) -> int:
        """
        Calculates current age based on birth date.

        Returns:
        int: Age in years
        """
        birth_date = datetime.strptime(self.date, '%m/%d/%Y').date()
        current_date = datetime.now().date()
        year_difference = current_date.year - birth_date.year

        if current_date.month < birth_date.month or (
                current_date.month == birth_date.month and current_date.day < birth_date.day):
            return year_difference - 1

        return year_difference


def is_valid_date(input_date: str) -> bool:
    """
    Validates date format and values.

    Parameters:
    input_date (str): Date string in MM/DD/YYYY format

    Returns:
    bool: True if date is valid, False otherwise
    """
    month, day, year = map(int, input_date.split('/'))

    if month < 1 or month > 12:
        print("Month must be between 1 and 12")
        return False

    if day < 1 or day > 31:
        print("Date must be between 1 and 31")
        return False

    if month in (4, 6, 9, 11) and day > 30:
        print("Date must be between 1 and 30")
        return False

    if month == 2 and day > 29:
        print("Date must be between 1 and 29")
        return False

    if year > datetime.now().year:
        print(f"Year must not be longer than {datetime.now().year}")
        return False

    return True


if __name__ == '__main__':
    date = input("Please input your date of birth (mm/dd/yyyy) : ")
    birthDate = BirthDate(date)
    valid_date = is_valid_date(birthDate.date)
    if valid_date:
        age = birthDate.calculate_age()
        output_date = birthDate.change_to_european_format()
        print(f"Your input date of birth is : {output_date} (dd/mm/yyyy)")
        print(f"Your age is : {age}")
    else:
        raise InvalidBirthDateException(f"Invalid input date of birth! : {birthDate.date}")
