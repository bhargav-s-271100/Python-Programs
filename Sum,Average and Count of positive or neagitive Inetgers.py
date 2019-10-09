a=int(input("enter the number or enter 999 to exit : "))
pos=0
neg=0
sum=0
i=0
while(a!=999):
    if(a>0):
        pos+=1
    elif(a<0):
        neg+=1
    sum+=a
    i+=1
    a = int(input("enter the number or enter 999 to exit : "))
avg=float(sum/i)
print("sum = ",sum," average = ",avg)
