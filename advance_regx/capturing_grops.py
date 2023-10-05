import re

result = re.search(r"^(\w*), (\w*)$", "Lovelace, Ada")
print(result)
# <re.Match object; span=(0, 13), match='Lovelace, Ada'>
print(result.group())
# Lovelace, Ada