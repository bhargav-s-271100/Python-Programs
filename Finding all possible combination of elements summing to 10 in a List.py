a=list(input("Enter the list : "))
for i in a:
    for j in a:
        if int(i)+int(j)==10 and i!=j:
            print(int(i)," + ",int(j)," = 10")


