calc_eigen.py

A small Python3 tool for calulating eigenvalues for the matrix files in the matrix-market format.

Type 1: Generalized eigenvalue equation ( A v = e B v )
Ex. python3 calc_eigen.py ELSES_MATRIX_BNZ30_A.mtx -b ELSES_MATRIX_BNZ30_B.mtx

Type 2: Standard eigenvalue problem ( A v = e v )
Ex. python3 calc_eigen.py ELSES_MATRIX_VCNT400std_A.mtx

