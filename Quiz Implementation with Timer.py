from random import *
from datetime import *
a=['C','C++',"Python"]
b=['int','char','string']
c=['list','set','tuple']
print("Q1) Which of the languages is an interpreted one ?       time=1min")
shuffle(a)
print("The options are : ")
for i in range(0,3):
    print(i+1,") ",a[i])
initial=datetime.today()
final=initial+timedelta(minutes=1)
A1=input("Enter ur answer : ")
if(final>datetime.today()):
   if A1=='Python':
         print("Correct Answer")
   else :
        print("Wrong Answer")
else:
    print("Time Up")
print("Q2) Which datatype is not available in python ?       time=1min")
shuffle(b)
print("The options are : ")
for i in range(0,3):
    print(i+1,") ",b[i])
initial=datetime.today()
final=initial+timedelta(minutes=1)
A2=input("Enter ur answer : ")
if(final>datetime.today()):
   if A2=='char':
         print("Correct Answer")
   else :
        print("Wrong Answer")
else:
    print("Time Up")
print("Q3) Which of these is an immutable datatype ?       time=1min")
shuffle(c)
print("The options are : ")
for i in range(0,3):
    print(i+1,") ",c[i])
initial=datetime.today()
final=initial+timedelta(hours=0.0167)
A3=input("Enter ur answer : ")
if(final>datetime.today()):
   if A3=='tuple':
         print("Correct Answer")
   else :
        print("Wrong Answer")
else:
    print("Time Up")

