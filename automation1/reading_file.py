
# file = open("E:/google_python_os/automation1/spider.txt")
# print(file.readline()) # it reads the single line of the file
# file.close()

with open("E:/google_python_os/automation1/spider.txt") as file:
    print(file.read())
    
    # the output
#     this is normal spder.txt file
#     this is testing file
# with open keywords python will automatically close the file, we don't have to close it

# The readline() method reads a single line from the current position, the read() method reads from the current position until the end of the file.