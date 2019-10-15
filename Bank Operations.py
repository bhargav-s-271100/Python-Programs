class Bank :
    def __init__(self,bal):
        self.bal=bal
    def withdrawl(self):
        a=int(input("enter the amount to be withdrawn "))
        self.bal-=a
        if self.bal>=1000 :
            print("Account Balance = ",self.bal)
        else :
            print("Insufficient balance ")
    def deposit(self):
        a=int(input("enter the amount to be deposited "))
        self.bal+=a
        print("Account Balance = ", self.bal)
ob=Bank(1000)
while (1):
    c=input("Enter 1 for withdrawl and 2 for deposit or * to exit ")
    if c=='1':
        ob.withdrawl()
    elif c=='2':
        ob.deposit()
    elif c=='*':
        exit(0)