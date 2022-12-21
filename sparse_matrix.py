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

# for _ in range(10):
#     A = generate_sparse_matrix(1000)
#     b = generate_b(1000)
#     Ab = np.hstack((A,b)) 
#     if np.linalg.matrix_rank(A) == np.linalg.matrix_rank(Ab):
#         print(A)
#         break


A = np.array([[3,2,0,0,0,0], [0,2,1,0,0,2], [0,2,1,0,0,0],[0,0,3,2,4,0], [0,4,0,0,1,0], [0,0,0,0,2,3]])


#CSR format
a, b = np.nonzero(A)
print("indices of rows: ", a)
print("indices of cols: ", b)

data = np.array([])
col_idx = b
row_ptr = np.array([])

count = a[0]
row_ptr = np.append(row_ptr, np.where(data == A[a[0]][b[0]]))


for i in range(len(a)):
    data = np.append(data,A[a[i]][b[i]])

    if count != a[i]:
        row_ptr = np.append(row_ptr, np.where(data == A[a[i]][b[i]]))
        count = a[i]

row_ptr[0]

print("data: ", data)
print("col_idx: ", col_idx)
print("row_ptr: ", row_ptr)

#test = np.array([[1,2,3], [4,5,6], [7,8,9]])
# test = np.array([1,2,3,4,5])
# print(test)
# print(np.where(test == 2)[0] == 1)
