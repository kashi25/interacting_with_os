# log = "July 31 07:52:48 mycomputer bad_process[12345896]:error performance package upgrade"
# index = log.index("[")
# print(log[index+1:index+7])
# # output will be 123458

# we can perform same operation by using re module
import re
log = "July 31 07:52:48 mycomputer bad_process[12345896]:error performance package upgrade"
regex = r"\[(\d+)\]"
result = re.search(regex, log)
print(result[1])
# the output 12345896