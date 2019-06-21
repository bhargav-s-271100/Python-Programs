r=input("input the string")
s=r.split(sep=";")
t=s[0].split(sep="=")
tel={}
tel[t[0]]=t[1]
u=s[1].split(sep="=")
tel[u[0]]=u[1]
print(tel)

          
