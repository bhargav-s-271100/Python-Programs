#to search for a string in a variable or file
import re
a="Bhargav is a good boy"
print(re.findall("ar",a))
#to find the number of times a string is present
b=len(re.findall("ar",a))
print(b)
# or we can use count
print(a.count("a"))
#to slice out a string before and after a given charatcter
b="mail id : bhargavs@gmail.com"
#prints different characters
print(re.findall("[\S]",b))
#prints words differently
print(re.findall("[\S]+[\S]",b))
#prints words before and after @
print(re.findall("[\S]+@+[\S]+[\S]",b))
