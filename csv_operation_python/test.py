import csv

content = [[24, 'Lal Badhur Tamang', "kyampa", 30000],[34, 'Hari Gadhal', "Kyampa",  27000], [56, 'Gopla Shunuwar', "dadaline", 34000]]
with open('random.csv', 'w', newline='') as rand_csv:  # Open the file in write mode and specify newline=''
    jhot = csv.writer(rand_csv)
    header = ["age", "Name", "address", "salary"]
    
    # Write the header row
    jhot.writerow(header)
    
    # Write the data rows
    jhot.writerows(content)

