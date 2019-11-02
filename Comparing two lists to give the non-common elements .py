a=input("Enter the first list : ").split(',')
b=input("Enter the final List : ").split(',')
c=[]
d=0
for i in a:
    d+=1
    if i not in b:
        print("Removed Element ",i," found at location",d)