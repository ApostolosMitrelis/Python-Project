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

def gauss(A, b):  # A ο κυριος πινακας και β η στηλη
    A = np.array(A, float)
    b = np.array(b, float)

    for k in range(0, len(b)):
        # Αλλαζουμε το οδηγο στοιχειο αμα αυτο ειναι 0
        if A[k, k] == 0:
            for i in range(k + 1, len(b)):
                if A[i, k] != 0:
                    for j in range(k, len(b)):
                        A[k, j], A[i, j] = A[i, j], A[k, j]
                    b[k], b[i] = b[i], b[k]
                    break

        # Διαιρουμε την πρωτη γραμμη ωστε το οδηγο στοιχειο να γινει 1
        odhgo_stoixeio = A[k, k]
        for j in range(k, len(b)):
            A[k, j] /= odhgo_stoixeio
        b[k] /= odhgo_stoixeio
        # Κανουμε τα στοιχεια κατω απο το οδηγο στοιχειο 0
        for i in range(0, len(b)):
            if i == k or A[i, k] == 0: continue  # Δεν θελουμε να κανουμε 0 τα στοιχεια πανω στην διαγωνιο
            l=A[i,k]
            for j in range(k, len(b)):
                A[i, j] = A[i, j] - l * A[k, j]
            b[i] = b[i] - l* b[k]

    return b

b = generate_b(100)
print(b)
A = generate_sparse_matrix(100)
print(A)
Ab = np.hstack((A,b))
print(Ab)
print(np.linalg.matrix_rank(A))
print(np.linalg.matrix_rank(Ab))

        

    
