import numpy
m=int(input("Enter the number of rows "))
n=int(input("Enter the number of columns "))
a=numpy.arrange(m*n).reshape(m,n)
print(a)
b=numpy.array([(1,2,3),(4,5,6),(7,8,9)])
print(b)
c=numpy.dot(a,b)
print(c)