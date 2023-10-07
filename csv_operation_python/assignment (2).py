#!/usr/bin/env python3
import csv

def read_employees(csv_file_location):
    csv.register_dialect('empDialect', skipinitialspace=True, strict=True)
    employee_list = []
    
    with open(csv_file_location, mode='r', encoding='utf-8') as file:
        employee_file = csv.DictReader(file, dialect='empDialect')
        for data in employee_file:
            employee_list.append(data)
    
    return employee_list

employee_list = read_employees('/home/student-02-a1ec66a506c1/data/employees.csv')
print(employee_list)


def process_data(employee_list):
    department_data = {}
    
    for employee_data in employee_list:
        department_name = employee_data['Department']
        if department_name in department_data:
            department_data[department_name] += 1
        else:
            department_data[department_name] = 1
    
    return department_data

dictionary = process_data(employee_list)
print(dictionary)


def write_report(dictionary, report_file):
    with open(report_file, "w+") as f:
        for k in sorted(dictionary):
            f.write(str(k) + ':' + str(dictionary[k]) + '\n')

# Provide a valid file path for the report file, e.g., '/home/student-02-a1ec66a506c1/data/report.txt'
report_file_path = '/home/student-02-a1ec66a506c1/data/report.txt'
write_report(dictionary, report_file_path)
