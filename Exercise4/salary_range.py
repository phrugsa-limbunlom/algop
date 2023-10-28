def find_salaries_range(employees, minimum_salary, maximum_salary):
    filtered_employees = []
    for employee in employees:
        if minimum_salary <= int(employee[2]) <= maximum_salary:
            filtered_employees.append(employee)
    # return sorted(filtered_employees, key=lambda e: e[-1], reverse=True)
    return filtered_employees


def sort_salaries(employees):
    for i in range(len(employees)):
        for j in range(i):
            if employees[i][2] >= employees[j][2]:
                employees[i], employees[j] = employees[j], employees[i]
    return employees


def format_employees_result(employees):
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
                    filtered_employee_list = find_salaries_range(employee_list, int(min_salary), int(max_salary))
                    final_employee_list = format_employees_result(sort_salaries(filtered_employee_list))
                    print(final_employee_list)
                break
        except FileNotFoundError:
            print("Incorrect file name!")
