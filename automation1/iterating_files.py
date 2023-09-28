# with open('E:/google_python_os/automation1/spider.txt') as file:
#     for line in file:
#         print(line.upper())


# output
# THIS IS NORMAL SPDER.TXT FILE

# THIS IS TESTING FILE 


with open('E:/google_python_os/automation1/spider.txt')as file:
    for line in file:
        print(line.strip().upper())
        
        
# the output of the code is 
# THIS IS NORMAL SPDER.TXT FILE
# THIS IS TESTING FILE