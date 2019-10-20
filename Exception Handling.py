#to add an exception to certain exceptions
try:
    a=10
    b=int(input("Enter the value : "))
    c=a/b
    print(c)
except ZeroDivisionError:
    print("division by zero is not possible")
#this concept can be used to chcek the presence of modules