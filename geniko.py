import numpy as np
import random
import scipy as sp


def generate_sparse_matrix(dim):
    #generate random sparse matrix
    A = np.zeros((dim,dim), dtype = float)

    for _ in range(10000):
        A[random.randrange(dim)][random.randrange(dim)] = random.randint(-100,100)

    return A 

def generate_b(dim):
    #generate random b array of 1 dimension
    rng = np.random.default_rng()
    b = rng.integers(low=-100, high=100, endpoint=True, size=(dim,1))     

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

#A = np.array([[3,2,0,0,0,0], [0,2,1,0,0,2], [0,2,1,0,0,0],[0,0,3,2,4,0], [0,4,0,0,1,0], [0,0,0,0,2,3]])

# for _ in range(10):
#     A = generate_sparse_matrix(1000)
#     b = generate_b(1000)
#     Ab = np.hstack((A,b)) 
#     if np.linalg.matrix_rank(A) == np.linalg.matrix_rank(Ab):
#         print(A)
#         break

#B = sp.sparse.csc_matrix((data,row_idx,col_ptr), shape=(3,3)).toarray()
# b = np.array([1,2,3,4,5,6]).reshape(6,1)
# x = sp.sparse.linalg.spsolve(B,b)
#print(B)
# print(b)
# print(x)

