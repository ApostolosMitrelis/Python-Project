import numpy as np
import random
import scipy as sp


def generate_sparse_matrix(dim):
    A = np.zeros((dim,dim), dtype = float)

    for _ in range(10000):
        A[random.randrange(dim)][random.randrange(dim)] = random.randint(-100,100)

    return A 

def generate_b(dim):
    rng = np.random.default_rng()
    b = rng.integers(low=-100, high=100, endpoint=True, size=(dim,1))     

    return b  

def csr_format(A):
    #CSR format
    a, b = np.nonzero(A)

    data = np.array([])
    col_idx = b
    row_ptr = np.array([])

    start = a[0]
    count = 0
    row_ptr = np.append(row_ptr, 0)

    for i in range(len(a)):
        data = np.append(data,A[a[i]][b[i]])
        if start != a[i]:
            count += 1
            row_ptr = np.append(row_ptr, row_ptr[count-1] + np.count_nonzero(a == count-1))
            start = a[i]

    row_ptr = np.append(row_ptr, len(data))

    return data, col_idx, row_ptr

A = np.array([[3,2,0,0,0,0], [0,2,1,0,0,2], [0,2,1,0,0,0],[0,0,3,2,4,0], [0,4,0,0,1,0], [0,0,0,0,2,3]])

# for _ in range(10):
#     A = generate_sparse_matrix(1000)
#     b = generate_b(1000)
#     Ab = np.hstack((A,b)) 
#     if np.linalg.matrix_rank(A) == np.linalg.matrix_rank(Ab):
#         print(A)
#         break

data, col_idx, row_ptr = csr_format(A)
B = sp.sparse.csr_matrix((data,col_idx,row_ptr), shape=(6,6)).toarray()
b = np.array([1,2,3,4,5,6]).reshape(6,1)
x = sp.sparse.linalg.spsolve(B,b)
print(B)
print(b)
print(x)