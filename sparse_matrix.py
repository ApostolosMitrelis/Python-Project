import numpy as np
import random


#sparse_matrix = {(0,0): 1, (0,2): 2, (1,1): 3, (2,2): 4, (1000,1000): 5, (10000,10000): 6}

def generate_sparse_matrix(dim):

    A = np.zeros((dim,dim), dtype = float)

    for _ in range(30):
        A[random.randrange(dim)][random.randrange(dim)] = random.randint(-100,100)

    return A 

def generate_b(dim):

    rng = np.random.default_rng()
    b = rng.integers(low=-100, high=100, endpoint=True, size=(dim,1))     

    return b  

b = generate_b(100)
print(b)
A = generate_sparse_matrix(100)
print(A)
Ab = np.hstack((A,b))
print(Ab)
print(np.linalg.matrix_rank(A))
print(np.linalg.matrix_rank(Ab))

        

    
