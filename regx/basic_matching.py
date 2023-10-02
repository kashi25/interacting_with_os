import re

result = re.search(r"aza", "plaza")
print(result)

# <re.Match object; span=(2, 5), match='aza'>

ber = re.search(r"aza", "bazar")
print(ber)
# <re.Match object; span=(1, 4), match='aza'

ark = re.search(r"aza", "ashok")
print(ark)
# None

print(re.search(r"^x", "xenon"))
# <re.Match object; span=(0, 1), match='x'>

print(re.search(r"p.ng", "clapping"))
# <re.Match object; span=(4, 8), match='ping'>


def check_aei (text):
  result = re.search(r"a.e.i", text)
  return result != None

print(check_aei("academia")) # True
print(check_aei("aerial")) # False
print(check_aei("paramedic")) # True


print(re.search(r"p.ng", "Pangaea", re.IGNORECASE))
# <re.Match object; span=(0, 4), match='Pang'>