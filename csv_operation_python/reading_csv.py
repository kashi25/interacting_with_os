import csv
f = open('csv.file.txt')
csv_f = csv.reader(f)
for row in csv_f:
    name, phone, role = row
    print("Name: {}, Phone:{}, Roll: {}". format(name, phone, role))
f.close()