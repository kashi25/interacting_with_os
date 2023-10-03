import re
print(re.search(r".com", "welcome"))
# <re.Match object; span=(2, 6), match='lcom'>

print(re.search(r"\.com", "welcome"))
# None

print(re.search(r"\.com", "mydomain.com"))
# <re.Match object; span=(8, 12), match='.com'>

# when we see a pattern that includes a backslash, it could be
# escaping a special regex character or a special string character
# \w represent any alpha numerica character
# \b for board boundary
# \d for digit
# \s for white space
print(re.search(r"\w*", "this_is an example"))
# <re.Match object; span=(0, 7), match='this_is'>


import re
def check_character_groups(text):
  result = re.search(r"\d", text)
  return result != None

print(check_character_groups("One")) # False
print(check_character_groups("123  Ready Set GO")) # True
print(check_character_groups("username user_01")) # True
print(check_character_groups("shopping_list: milk, bread, eggs.")) # False

