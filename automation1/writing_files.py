# with open("first.txt", "w") as file:
#     file.write("it was a dark and stromy night")
    
# """What happens to the previous contents of a file when we open it using "w" ("write" mode)?"""
# The old contents get deleted as soon as we open the file.

# for more details https://docs.python.org/3/library/functions.html#open

guest = open("guest.txt","w")
initial_guest = ['kashi', 'ashok', 'bhairab', 'shiva']
for i in initial_guest:
    guest.write(i + "\n")
guest.close()


# to display the content of guest.txt
with open("guest.txt") as guest:
    for line in guest:
        print(line)


# kashi

# ashok

# bhairab

# shiva