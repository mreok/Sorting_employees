# One of the ways of sorting employees

def sort_employees(employees, sort_by):
    sort_indices = ['name','age', 'salary']
    sort_index = sort_indices.index(sort_by)

    sorted_employees = []

    employees_copy = employees[:]

    while len(employees_copy) > 0:
        smallest_employee_index = 0

        for i,employee in enumerate(employees_copy):
            current_smallest_value = employees_copy[smallest_employee_index]
            if employee[sort_index] < current_smallest_value:
                smallest_employee_index = i

        next_sorted_employees = employees_copy[smallest_employee_index]
        sorted_employees.append(next_sorted_employees)
        employees_copy.pop(smallest_employee_index)

    return sort_employees

# Sorting employees can also be done in a simplest form

def sort_laborers(laborers, sort_by):
    sort_indices = ['name', 'age', 'salary']
    sort_index = sort_indices.index(sort_by)

    sorted_laborers = sorted(laborers, lambda x: x[sort_by])

    return sorted_laborers

