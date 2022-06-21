import scipy
import argparse
from scipy import linalg
from scipy.io import mmwrite, mmread

parser = argparse.ArgumentParser()
parser.add_argument('arg1', help='help for arg1', default='no_arg1')
parser.add_argument('-b', help='help for arg2', default='no_B_matrix')
parser.add_argument('-e', help='help for arg2', default='result_ev.txt')
parser.add_argument('-ipr', help='help for arg2', default='result_ipr.txt')

args = parser.parse_args()
#print('matrix A = ',args.arg1)
#print('matrix B = ',args.b)

if args.b != 'no_B_matrix' :
    print('Generalized eigenvalue problem')
    print('  matrix A : ',args.arg1)
    print('  matrix B : ',args.b)
    A=scipy.io.mmread(args.arg1).todense()
    B=scipy.io.mmread(args.b).todense()
    w, v = scipy.linalg.eigh(A,B)
elif args.arg1 != 'no_arg1' :
    print('Standard eigenvalue problem')
    print('  matrix A : ',args.arg1)
    A=scipy.io.mmread(args.arg1).todense()
    w, v = scipy.linalg.eigh(A)
else:
    print('ERROR:No input for matrix')

with open(args.e, 'w') as f:
    for i in range(len(w)):
        print (i+1, w[i], file=f)

with open(args.ipr, 'w') as f:
    for i in range(len(w)):
        y=w
        for j in range(len(w)):
#           print('i,j=',i,j)
            w[j] = v[j,i]**4
        print (i+1, sum(w), file=f)


