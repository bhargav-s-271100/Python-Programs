even=''
odd=''
upper=''
lower=''
s=str(input("Enter the string : "));
for i in range(len(s)):
    if(s[i].isdigit() and int(s[i])%2==0):
        even += s[i]
    elif(s[i].isdigit() and int(s[i])%2!=0):
        odd += s[i]
    elif(s[i]>='A' and s[i]<='Z'):
        upper += s[i]
    else:
        lower+=s[i]
res_lower = ''.join(sorted(lower))
res_upper = ''.join(sorted(upper))
res_odd = ''.join(sorted(odd))
res_even = ''.join(sorted(even))
result = res_lower+res_upper+res_odd+res_even
print(result)

