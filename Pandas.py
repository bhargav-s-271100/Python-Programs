#tuple and strings are immutable i.e they cant be altered
import pandas as pd
import numpy as np
from numpy import random

#to get same random number again we use seed function
np.random.seed(10)
print(np.random.rand())
dic={'numbers':[1,2,3,4,5],'alpha':['a','b','c','d','e'],'price':10*random.rand(5)}
print(dic)
table=pd.DataFrame(dic)
print(table)
rand_num=[random.rand() for i in range(5)]
print(rand_num)
up_to_ten=[i for i in range(10)]
random.shuffle(up_to_ten)
print(up_to_ten)
