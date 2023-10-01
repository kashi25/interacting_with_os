import csv

def read_employees(csv_file_location):
    csv.register_dialect('empDialect', skipinitialspace=True, strict=True)
    employee_file = csv.DictReader(open(csv_file_location), dialect='empDialect')
    employee_list = []
    for data in employee_file:
        employee_list.append(data)
    return employee_list

employee_list = read_employees('/home/student-02-a1ec66a506c1/data/employees.csv')
print(employee_list)


def process_data(employee_list):
    department_data = {}
    
    for employee_data in employee_list:
        department = employee_data['Department']
        if department in department_data:
            department_data[department] += 1
        else:
            department_data[department] = 1
            
    return department_data

dictionary = process_data(employee_list)
print(dictionary)


def write_report(dictionary, report_file):
    with open(report_file, "w+") as f:
        for k in sorted(dictionary):
            f.write(str(k) + ':' + str(dictionary[k]) + '\n')

# Replace '<report_file>' with the actual file path where you want to save the report.
write_report(dictionary, 'report.txt')
