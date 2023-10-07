import re

print(re.search(r"[a-zA-Z]{5}", "a ghost"))
# <re.Match object; span=(2, 7), match='ghost'>

print(re.search(r"[a-zA-Z]{5}", "Hellohi how are you"))
# <re.Match object; span=(0, 5), match='Hello'>

print(re.findall(r"[a-zA-Z]{5}", "how are you kashinath"))
# ['kashi']

print(re.findall(r"[a-zA-Z]{5}", "hello dines you kashinath"))
# ['hello', 'dines', 'kashi']



# The long_words function returns all words that are at least 7 characters. Fill in the regular expression to complete this function.

import re
def long_words(text):
  pattern = r'\b\w{7,}\b'
  result = re.findall(pattern, text)
  return result

print(long_words("I like to drink coffee in the morning.")) # ['morning']
print(long_words("I also have a taste for hot chocolate in the afternoon.")) # ['chocolate', 'afternoon']
print(long_words("I never drink tea late at night.")) # []





