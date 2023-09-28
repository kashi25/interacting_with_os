with open("first.txt", "w") as file:
    file.write("it was a dark and stromy night")
    
# """What happens to the previous contents of a file when we open it using "w" ("write" mode)?"""
# The old contents get deleted as soon as we open the file.

# for more details https://docs.python.org/3/library/functions.html#open