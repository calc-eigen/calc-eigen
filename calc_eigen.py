import scipy
import numpy
import argparse
from scipy import linalg
from scipy.io import mmwrite, mmread
import numpy as np

parser = argparse.ArgumentParser()
parser.add_argument('arg1', help='help for arg1', default='no_arg1')
parser.add_argument('-b', help='help for arg2', default='no_B_matrix')

args = parser.parse_args()
print('matrix A = ',args.arg1)
print('matrix B = ',args.b)

if args.b != 'no_B_matrix' :
    print('generalized eigenvalue problem')
    print('  matrix A : ',args.arg1)
    print('  matrix B : ',args.b)
    A=scipy.io.mmread(args.arg1).todense()
    B=scipy.io.mmread(args.b).todense()
    w, v = scipy.linalg.eigh(A,B)
elif args.arg1 != 'no_arg1' :
    print('standard eigenvalue problem')
    print('  matrix A : ',args.arg1)
    A=scipy.io.mmread(args.arg1).todense()
    w, v = scipy.linalg.eigh(A)
else:
    print('ERROR:No input for matrix')


for i in range(len(w)):
    print (i+1, w[i])
    

