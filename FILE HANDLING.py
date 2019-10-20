# To create and write in a text
file=open("new.txt","w")
file.write("My First Text \n")
file.write("My Second Text ")
#to write multiple texts we use concatenation
file.write("Username : "+"Bhargav")
file.close()
# here file is owerwritten again and again
# so we append to add the code
file=open("appended.txt","a")
file.write("My First Text \n")
file.write("My Second Text ")
file.close()
# to read a file
file=open("new.txt","r")
print(file.read())
# to write user input data to a file
file=open("appended.txt","a")
a=input("Enter the data ")
file.write("Entered data = %s" %a)
file.close()
#to read a file
file=open("appended.txt","r")
print(file.read())
file.close()
