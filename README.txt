calc_eigen.py

A small Python3 tool for calulating hermitian or real-symmetric eigenvalues for the matrix files in the matrix-market format.

Type 1: Generalized eigenvalue equation ( A v = e B v )
Ex. python3 calc_eigen.py ELSES_MATRIX_BNZ30_A.mtx -b ELSES_MATRIX_BNZ30_B.mtx -e result_ev.txt -ipr result_ipr.txt
The output files: 
result_ev.txt  : the file for eigenvalues
result_ipr.txt : the file invserse participation ratio for each eigenvector  

Type 2: Standard eigenvalue problem ( A v = e v )
Ex. python3 calc_eigen.py ELSES_MATRIX_VCNT400std_A.mtx -e result_ev.txt -ipr result_ipr.txt
The output files: 
result_ev.txt  : the file for eigenvalues
result_ipr.txt : the file invserse participation ratio for each eigenvector  

Note: This tool uses the dense-matrix solver library, scipy.linalg.eigh 

