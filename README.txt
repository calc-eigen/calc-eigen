calc_eigen.py

A small Python3 tool for calulating complex-Hermitian or real-symmetric eigenvalue problem for the matrix files in the matrix-market format.

Type 1: Generalized eigenvalue problem ( A v_k = e_k B v_k )
Ex. python3 calc_eigen.py ELSES_MATRIX_BNZ30_A.mtx -b ELSES_MATRIX_BNZ30_B.mtx -e result_ev.txt -ipr result_ipr.txt
The output files: 
  result_ev.txt  : the file of eigenvalues ( e_1, e_2, ..., ) 
  result_ipr.txt : the file of invserse participation ratio (IPR) for eigenvectors ( IPR(v_1), IPR(v_2), .... )

Type 2: Standard eigenvalue problem ( A v_k = e_k v_k )
Ex. python3 calc_eigen.py ELSES_MATRIX_VCNT400std_A.mtx -e result_ev.txt -ipr result_ipr.txt
The output files: 
  result_ev.txt  : the file of eigenvalues ( e_1, e_2, ..., ) 
  result_ipr.txt : the file of invserse participation ratio for eigenvectors ( IPR(v_1), IPR(v_2), .... )

Note: This tool uses the dense-matrix solver library, scipy.linalg.eigh 

Note: The IPR is defined for a vector v as
  IPR(v) = sum_i |v_j|^4 


