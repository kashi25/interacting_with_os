import csv

with open('random.csv', newline='') as soft:
    reader = csv.DictReader(soft)
    for row in reader:
        print(("{} is the  {} age").format(row["age"], row["Name"]))


# output

# 24 is the  Lal Badhur Tamang age
# 34 is the  Hari Gadhal age
# 56 is the  Gopla Shunuwar age