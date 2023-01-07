import numpy as np
import random
import scipy as sp
import os
import matplotlib.pylab as plt
from timeit import default_timer as timer

def generate_sparse_matrix(dim1,dim2,diag,non_zero):
    #generate random sparse matrix
    A = np.zeros((dim1,dim2), dtype = float)
    if diag == "yes" and dim1 == dim2:
        for i in range(dim1):
            A[i][i] = random.randint(-100,100)
    else:
        for _ in range(non_zero):
            A[random.randrange(dim1)][random.randrange(dim2)] = random.randint(-100,100)

    return A 

def generate_b(dim1):
    #generate random b array of 1 dimension
    rng = np.random.default_rng()
    b = rng.integers(low=-100, high=100, endpoint=True, size=(dim1,1))     

    return b  

def csr_format(A):
    #CSR format
    a, col_idx = np.nonzero(A)

    data = np.array([])
    row_ptr = np.array([])

    start = a[0]
    count = 0
    row_ptr = np.append(row_ptr, 0)

    for i in range(len(a)):
        data = np.append(data, A[a[i]][col_idx[i]])
        if start != a[i]:
            count += 1
            row_ptr = np.append(row_ptr, row_ptr[count-1] + np.count_nonzero(a == count-1))
            start = a[i]

    row_ptr = np.append(row_ptr, len(data))

    return data, col_idx, row_ptr

def csc_format(A):
    #CSC format
    A = A.T
    data, row_idx, col_ptr = csr_format(A)
    return data, row_idx, col_ptr

def coo_format(A):
    #COO format
    row, col = np.nonzero(A)

    data = np.array([])

    for i in range(len(row)):
        data = np.append(data, A[row[i]][col[i]])

    return data, col, row

def main():
    start = timer()
    while True:
        answer = input("Δώσε δίασταση του πίνακα (πχ.1000x1000), ναι ή οχι αν είναι διαγώνιος, πλήθος μη μηδενικών στοιχείων (enter για έξοδο): ")
        if answer == '':
            break
        else:
            dim, diag, non_zero = answer.split(",")
        dim1, dim2 = dim.split("x")
        dim1 = int(dim1)
        dim2 = int(dim2)
        non_zero = int(non_zero)
        while True:
            A = generate_sparse_matrix(dim1,dim2,diag,non_zero)
            b = generate_b(dim1)
            Ab = np.hstack((A,b)) 
            if np.linalg.matrix_rank(A) == np.linalg.matrix_rank(Ab):
                break
        
        data, col_idx, row_ptr = csr_format(A)
        B = sp.sparse.csr_matrix((data,col_idx,row_ptr), shape=(dim1,dim2)).toarray()
        x = sp.sparse.linalg.spsolve(B,b)
        end = timer()
        print("time: ",end-start)
        
main()
