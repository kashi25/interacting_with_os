import sys

logfile = sys.argv[1]
with open(logfile) as f:
    for line in f:
        if "CORNS" not in line:
            continue
        print(line.strip())
        

# in python cell
# import re
# pattern = r"USER\((\w+)\)$"
# line = "kashi 12444-7865 computer name CORNS found"
# result = re.search(pattern, line)
# print(result[1])