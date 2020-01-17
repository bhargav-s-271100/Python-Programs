def calc(a,b):
    return (a+b),(a-b)
a,b=calc(10,20)
print(a,b)
#lambda parameters
add=lambda a,b:(a+b)
print(add(10,20))
#anonymous functions
def fn(a):
    return lambda n:a*n
fn1=fn(2)
print(fn1(3))
#MAP function
l=[1,2,3,4,5,6]
#to manipulate each element of list
num=map(lambda n:n*2,l)
print(list(num))
#FILTER Function
l=[1,2,3,4,5,6]
#to filter a list depending on a condition
l1=list(map(lambda n:n*10,l))
vote=filter(lambda n:n>18,l1)
print(list(vote))
#REDUCE Function
l=[10,20,30,40,50]
import functools as red
print(red.reduce(lambda a,b:a+b,l))
#to find smallest element of the list
print(red.reduce(lambda a,b:a if a<b else b,l))
