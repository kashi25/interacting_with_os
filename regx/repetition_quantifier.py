import re
print(re.search(r"Py.*n", "Pygmalion"))
# <re.Match object; span=(0, 9), match='Pygmalion'>

print(re.search(r"Py[a-z]*n", "Python Programming"))
# <re.Match object; span=(0, 6), match='Python'>

print(re.search(r"o+l+", "goldfish"))
# <re.Match object; span=(1, 3), match='ol'>

print(re.search(r"o+l+", "booley"))
# <re.Match object; span=(1, 4), match='ool'>

print(re.search(r"p?each", "To each there own"))
# match each

print(re.search(r"p?each", "i like peach"))
# match peach

import re
def repeating_letter_a(text):
  result = re.search(r'a.*a', text, re.IGNORECASE)
  return result != None

print(repeating_letter_a("banana")) # True
print(repeating_letter_a("pineapple")) # False
print(repeating_letter_a("Animal Kingdom")) # True
print(repeating_letter_a("A is for apple")) # True