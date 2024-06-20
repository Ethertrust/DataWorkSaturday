import numpy as np
from time import sleep
from os import system

def print_Z(Z):
    A = Z.copy()
    A = A.astype(str)
    A[A == '0'] = ' '
    A[A == '1'] = '*'
    str1 = ''
    for line in A:
        str1 = ''.join(line)
        print(str1)

def generation(Z):
    b = np.zeros([Z.shape[0]+2, Z.shape[1]+2],dtype = np.int16)
    b[1:-1,1:-1] = Z[...]
    b[1:-1,0] = Z[:,-1]
    b[1:-1, -1] = Z[:, 0]
    b[0, 1:-1] = Z[-1, :]
    b[-1, 1:-1] = Z[0, :]
    b[0, 0] = Z[-1, -1]
    b[-1, -1] = Z[0, 0]
    b[0, -1] = Z[-1, 0]
    b[-1, 0] = Z[0, -1]
    # print(b)
    N = (b[0:-2, 0:-2] + b[0:-2, 1:-1] + b[0:-2,2:]
       + b[1:-1, 0:-2] +               + b[1:-1,2:]
       + b[2:,   0:-2] + b[2:,   1:-1] + b[2:,  2:])
    # print(N)
    birth = (Z==0) & (N==3)
    survive = (Z==1) &((N==2) | (N==3))
    Z[...] = 0
    Z[birth|survive] = 1
    # print(Z)
    return Z


np.set_printoptions(linewidth=1000, edgeitems=41)
# Z = np.random.randint(0,2, (13, 45))
with open(r"C:\Users\HYPER\PycharmProjects\Classes B\Saturday\numpy\Datasets\5", "r") as f:
    Z = np.stack([np.fromiter(line.strip(), dtype=np.int16) for line in f])

A = Z.copy()
A = A.astype(str)
print_Z(Z)
# print(A)
while(True):
    Z=generation(Z)
    sleep(0.05)
    system('cls')
    print_Z(Z)
