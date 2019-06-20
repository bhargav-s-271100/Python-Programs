def mine():
   sname=input('enter the servername')
   dbname=input('enter the dbname')
   uname=input('enter the username')
   passw=input('enetr the password')
   s=sname+dbname+uname+passw
   return s
def main():
    p=mine()
main()    
for i in p:
      print('%s'.format(i))
