#Lists are scalar datatypes and cannot be added
import numpy as np
vector_row=np.arange(10)
print(vector_row)
#matrices can be made as below
matrix=np.arange(1,10).reshape(3,3)
print(matrix)

matrix=np.arange(1,5).reshape(4,1)
print(matrix[:2])
print('\n')
print(matrix[::-1])
print('\n')
print(matrix.shape)
print('\n')
print(matrix.size)
print('\n')
print(matrix.diagonal)
print('\n')
print(matrix.trace())
print('\n')
print(np.max(matrix,axis=0))
print('\n')
print(np.min(matrix,axis=1))
print('\n')

#Fancy Indexing
M=np.arange(24).reshape(6,4)
print(M[4,[1,2]])
print(M[:3,[0,1,2]])

#repeating a tile
A=[1,2,3,4]
print(np.tile(A,3))
print(np.repeat(A,2))

#Stacking
A1=np.arange(1,10).reshape(3,3)
A2=np.arange(10,19).reshape(3,3)
print(np.hstack((A1,A2)))
print(np.vstack((A1,A2)))

print(np.zeros(3,3))
print(np.ones(3,3))
print(np.eye(3))