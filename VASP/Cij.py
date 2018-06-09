import re
import numpy as np

filename = input("Please input your matrix file name: ")
f = open(filename)

# the below part was learnt from https://blog.csdn.net/u014453898/article/details/73378463
Cij = np.zeros((6,6),dtype = float)
lines = f.readlines()
Cij_row = 0
for line in lines:
		list = line.strip('\n').split()
		' '.join(list)
		Cij[Cij_row:] = list[0:6]
		Cij_row += 1
print('Here is the Cij!')
print(Cij)

# >print(type(Cij))
# >class 'numpy.ndarray'

Sij = np.linalg.inv(Cij)
print('Here is the inverse of Cij!')
print(Sij)

# multiply of matrix (https://migege.com/post/matrix-multiplication-in-numpy)
I =  Cij.dot(Sij)
print('Here is the identity matrix!')
print(I)

Kv = ( Cij[0][0] + Cij[1][1] + Cij[2][2] ) / 9  + 2 * (Cij[0][1] + Cij[0][2] + Cij[1][2] ) / 9
Gv = ( Cij[0][0] + Cij[1][1] + Cij[2][2] - Cij[0][1] - Cij[0][2] - Cij[1][2] ) / 15 + ( Cij[3][3] + Cij[4][4] + Cij[5][5] ) / 5
Kr = 1 / (( Sij[0][0] + Sij[1][1] + Sij[2][2] ) + 2 * ( Sij[0][1] + Sij[0][2] + Sij[1][2] ))
Gr = 15 / (( 4 * ( Sij[0][0] + Sij[1][1] + Sij[2][2] )) - 4 * ( Sij[0][1] + Sij[0][2] + Sij[1][2] ) + 3 * ( Sij[3][3] + Sij[4][4] + Sij[5][5] ))

K = (Kv + Kr)/2
G = (Gv + Gr)/2
E = 9 * K * G /(3 * K + G)
eta = (3 * K - 2 * G)/(2 * (3 * K + G))

# the unit used in VASP is kBar, here we use GPa as our unit
print('K=',K / 10)
print('G=',G / 10)
print('E=',E / 10)
print('Eta=',eta)

f.close()

