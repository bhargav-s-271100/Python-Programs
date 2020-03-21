#A valid Password must follow the rules below:

# 1) It must contain at least 2 uppercase English alphabet characters.
# 2) It must contain at least 3 digits (0-9).
# 3) It should only contain alphanumeric characters (a-z , A-Z  & 0-9).
# 4) No character should repeat.
# 5) There must be exactly 10 characters in a valid UID.
n=input("Enter the number of passwords : ")
data=input("Enter the passwords : ")
UID=data.split(sep=' ',maxsplit=int(n))
def check_UID(str):
    digit,upper,neg,rep =0,0,0,0
    s=str
    for i in range(0,len(s)):
        if(s[i].isdigit()):
            digit+=1
        elif(s[i].isalpha() and s[i].isupper()):
            upper+=1
        else:
            neg+=1
    for i in s:
        s=s[1:]
        if i in s:
            rep+=1
    if(len(str)==10 and digit>=3 and upper>=2 and neg==0 and rep==0):
        print("Valid")
    else:
        print("Invalid")
for i in UID:
    check_UID(i)