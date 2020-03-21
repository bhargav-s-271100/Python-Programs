s=input("Enter the string : ")
rep=0
for i in s:
        s=s[1:]
        if i in s:
            rep+=1
if rep==0:
    print("String is non-repeating")
else:
    print("string is repeating")