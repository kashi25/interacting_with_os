import re

ba= re.split(r"[.?!]", "One sentence. Another one? And Last one!")
print(ba)

['One sentence', ' Another one', ' And Last one', '']

aa= re.split(r"([.?!])", "One sentence. Another one? And Last one!")
print(aa)
# ['One sentence', '.', ' Another one', '?', ' And Last one', '!', '']


kr=re.sub(r"[\w.%+-]+@[\w.-]+", "[REDACTED]", "Redeived an email from  xya@gmail.com")
print(kr)
# Redeived an email from  [REDACTED]



kr = re.sub(r"^([\w .-]*), ([\w .-]*)$", r"\2 \1", "Lovelace, Ada")
print(kr)
# Ada Lovelace