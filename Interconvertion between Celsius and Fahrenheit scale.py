t=input("enter the temperature")
def convert(temp):
    b=temp[0:4]
    a=int(b)
    print(a)
    if  temp[-1]=='F':
        a=(a-32)*0.556
    elif  temp[-1]=='C':
        a=(a+32)*1.8
    else:
        print("invalid input")
    return a
a=convert(t)
print("temperature is :")
print(a)
        
