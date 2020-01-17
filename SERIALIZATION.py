#converting data into binary format using PICKLE
import pickle as p
import os
data={'id':10,'name':'steve','place':'bangalore'}
fp=open("C://data//ser",'wb')
p.dump(data,fp)
a=os.getcwd()
print(a)
fp.close()
fp=open("C://data//ser",'rb')
print(p.load(fp))
