def filter_employees_by_salaries(employees: list, minimum_salary: int, maximum_salary: int) -> list:
    """
    Filters employees whose salaries fall within given range.

    Parameters:
    employees (list): List of employee tuples (name, position, salary)
    minimum_salary (int): Lower bound of salary range
    maximum_salary (int): Upper bound of salary range

    Returns:
    list: Filtered list of employees within salary range
    """
    filtered_employees = []
    for employee in employees:
        if minimum_salary <= int(employee[2]) <= maximum_salary:
            filtered_employees.append(employee)
    return filtered_employees


def sort_employees_by_salaries(employees: list) -> list:
    """
    Sorts employees by salary in descending order using bubble sort.

    Parameters:
    employees (list): List of employee tuples to sort

    Returns:
    list: Sorted list of employees by salary
    """
    for i in range(len(employees)):
        for j in range(i):
            if employees[i][2] >= employees[j][2]:
                employees[i], employees[j] = employees[j], employees[i]
    return employees


def format_employees_result(employees: list) -> str:
    """
    Formats employee list as a string with each employee on new line.

    Parameters:
    employees (list): List of employee tuples to format

    Returns:
    str: Formatted string with each employee on new line
    """
    final_filtered_employees = ""
    for employee in employees:
        final_filtered_employees += str(employee) + "\n"
    return final_filtered_employees


if __name__ == "__main__":

    while True:
        try:
            file_name = input("Input file name (include extension) : ")
            with open(file_name, 'r') as file:
                print(f"{file_name} opened successfully")
                employee_list = [tuple(line.strip().split(",")) for line in file]
                print(f"All employees information : {employee_list}")
                while True:
                    salary_range = input(
                        "Input salary range (e,g, 1000000-10000000) or type 'exit' if want to quit the program: ")
                    if salary_range == "exit":
                        break
                    min_salary, max_salary = salary_range.split("-")
                    filtered_employee_list = filter_employees_by_salaries(employee_list, int(min_salary), int(max_salary))
                    sorted_filtered_employee_list = sort_employees_by_salaries(filtered_employee_list)
                    final_employee_list = format_employees_result(sorted_filtered_employee_list)
                    print(f"List of employees whose salaries are in the range\n{final_employee_list}")
                break
        except FileNotFoundError:
            print("Incorrect file name!")