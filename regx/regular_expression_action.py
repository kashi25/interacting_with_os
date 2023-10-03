import re

print(re.search(r"^A.*a$", "Australia"))
# <re.Match object; span=(0, 9), match='Australia'>

pattern = r"^[a-zA-Z_][a-zA-Z0-9_]*$"
print(re.search(pattern, "_this_is_valid_variable_name"))
# <re.Match object; span=(0, 28), match='_this_is_valid_variable_name'>


print(re.search(pattern, "this is not valid"))
# None


# check if the text passed looks like a standard sentence, meaning that it starts with an uppercase letter, followed by at least some lowercase letters or a space, and ends with a period, question mark, or exclamation point. 


import re
def check_sentence(text):
  result = re.search(r"^[A-Z][^.!?]*[.!?]$", text)
  return result != None

print(check_sentence("Is this is a sentence?")) # True
print(check_sentence("is this is a sentence?")) # False
print(check_sentence("Hello")) # False
print(check_sentence("1-2-3-GO!")) # False
print(check_sentence("A star is born.")) # True