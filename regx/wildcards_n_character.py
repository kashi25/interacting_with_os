import re

print(re.search(r"[Pp]ython", "Python "))
# <re.Match object; span=(0, 6), match='Python'>

print(re.search(r"[a-z]way", "The end of the highway"))
# <re.Match object; span=(18, 22), match='hway'>

print(re.search("cloud[a-zA-Z0-9]", "cloudy"))
# <re.Match object; span=(0, 6), match='cloudy'>


# check if the text passed contains punctuation symbols: commas, periods, colons, semicolons, question marks, and exclamation points.


import re
def check_punctuation (text):
  result = re.search(r"[.?!]$", text)
  return result != None

print(check_punctuation("This is a sentence that ends with a period.")) # True
print(check_punctuation("This is a sentence fragment without a period")) # False
print(check_punctuation("Aren't regular expressions awesome?")) # True
print(check_punctuation("Wow! We're really picking up some steam now!")) # True
print(check_punctuation("End of the line")) # False




# next
print(re.search(r"[^a-zA-Z]", "This is a sentence with space"))
# <re.Match object; span=(4, 5), match=' '>search any character that is  not a letter


print(re.search(r"[^a-zA-Z ]", "This is a sentence with space."))
# <re.Match object; span=(29, 30), match='.'>

print(re.search(r"cat|dag", "i like cats."))
# <re.Match object; span=(7, 10), match='cat'>

print(re.search(r"cat|dag", "i like cats and dog."))
# <re.Match object; span=(7, 10), match='cat'>

print(re.findall(r"cat|dog", "i like cat and dog"))
# <re.Match object; span=(7, 10), match='cat'>
# ['cat', 'dog']