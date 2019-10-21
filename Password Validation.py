print("Password must contain 1) one upper case or lower case alphanbet 2) one digit 3) #,$,@ or _ 4) min length of 6 and max length of 12")
p=input("Enter the password :")
if (any(c.isalpha() for c in p) and (c.isdigit() for c in p) and (('#'in p) or ('@' in p) or ('$' in p) or ('_'in p)) and len(p)>=6 and len(p)<=12):
    print("Valid Password")
else:
    print("Password strength LOW")