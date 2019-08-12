print("Interconvertion between List and Tuple")
a=(1,2,3,4)
b=list(a)
print(b)
a=[1,2,3,4]
b=tuple(a)
print(b)
print("Converting values of Dictionary to List")
a={1:"bat",2:"ball",3:"cricket"}
b=list(a)
print(b)
b=[a[1],a[2],a[3]]
print(b)
print("Converting values of Dictionary into Tuple")
a={1:"tennis",2:"badminton",3:"soccer"}
b=tuple(a)
print(b)
b=(a[1],a[2],a[3])
print(b)
