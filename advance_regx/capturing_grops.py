import re

result = re.search(r"^(\w*), (\w*)$", "Lovelace, Ada")
print(result)
# <re.Match object; span=(0, 13), match='Lovelace, Ada'>
print(result.group())
# Lovelace, Ada
print(result[0])
print(result[2])
# Ada
print("{} {}".format(result[2], result[1]))
# Ada Lovelace

def rearrange_name(name):
    result = re.search(r"^(\w*), (\w*)$", name)
    if result is None:
        return name
    return "{} {}",format(result[2], result[1])
rearrange_name("Bhattarai Kashi")
# rearrange_name("Bhattarai, Ashok")

# ^([\w \.-]*), ([\w \.-]*)$