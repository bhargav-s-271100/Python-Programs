print("Printing alphabet A ")
for i in range(5):
    print("\n")
    for j in range(7):
        if (i==0)or(i==1 and (j==0 or j==6))or(i==2)or(i==3 and (j==0 or j==6))or(i==4 and (j==0 or j==6)):
            print("*",end="")
        else:
            print(" ",end="")