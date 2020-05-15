import re
mystr = "You can learn programming language, whether it is Python2, Python3, Java, javascript or PHP."
a = re.match("You",mystr)
print(a)
b = re.match("you", mystr,re.I)
print(b.group())

# Search for patteren in entire string - search method
c = re.search("learn",mystr,re.I)
print(c.group())
