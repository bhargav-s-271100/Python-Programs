sen=input("Enter the sentence : ")
def reverse(a):
    b=a.split(sep=" ")
    c=b[::-1]
    for i in c:
        d=""
        d+=i
        print(d,end=" ")
reverse(sen)