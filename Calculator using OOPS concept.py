class calculator:
    def __init__(self,a,b):
        self.c=a
        self.d=b
    def add(self):
        return self.c+self.d
    def subtract(self):
        if self.c>self.d:
            self.c-self.d
        else:
            return self.c-self.d
    def multiply(self):
        return self.c*self.d
    def int_divide(self):
        return self.c//self.d
    def float_divide(self):
        return self.c/self.d
    def power(self):
        return self.c**self.d
print("Enter $ to exit from the calculator:")
a = input("enter the operation to be performed : ")
while a!='$':
    b = a.split(sep=" ")
    d=b[0]
    c = b[1]
    o = calculator(int(d),int(b[2]))
    if c=='+':
        print (o.add())
    elif c=='-':
        print(o.subtract())
    elif c=='*':
        print(o.multiply())
    elif c=='/':
        print(o.float_divide())
    elif c=='//':
        print(o.int_divide())
    elif c=='**':
        print(o.power())
    print("Enter $ to exit from the calculator:")
    a = input("enter the operation to be performed : ")
