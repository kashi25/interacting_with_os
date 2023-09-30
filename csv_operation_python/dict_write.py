import csv
users = [{"name":"diraj karki", "username":"diraj","department":"IT"},
         {"name":"milan bhandari", "username":"milan", "department":"management"},
         {"name":"anil oli", "username":"anil","department":"cnstruction"}]


keys = ["name", "username", "department"]
with open('by_department.csv', 'w') as by_department:
    writter = csv.DictWriter(by_department, fieldnames= keys)
    writter.writeheader()
    writter.writerows(users)
    
    
    # output name,username,department

# diraj karki,diraj,IT

# milan bhandari,milan,management

# anil oli,anil,cnstruction