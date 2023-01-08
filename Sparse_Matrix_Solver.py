from tkinter import *                              #Here is the programm we use to evaluate the acceleration of sparse matrices solvers with numba
import numpy as np                                 #We prefered not to use classes
import scipy as sp                                 #rry to usen=matrices which have some density more than 5% in order to fins easy a solvable matrix
import scipy.sparse
import random
import os
from timeit import default_timer as timer
import numba
import scipy.sparse.linalg

root = Tk()
root.title('Sparse Matrices Solver with Numba')
root.geometry("500x300")
root.configure(bg='LightSkyBlue1')

# Set up options for radio buttons
OPTIONS = [
    ("Import from a file", "import"),
    ("Generate a random matrix", "generate")
]

#Frames
f1 = Frame(root, bg='LightSkyBlue1')    #Creating Frames
f1.pack()                                   
f2 = Frame(root, bg='LightSkyBlue1')
f2.pack()
f3 = Frame(root, bg='LightSkyBlue1')
f3.pack()
f4 = Frame(root, bg='LightSkyBlue1')
f4.pack()
f5 = Frame(root, bg='LightSkyBlue1')
f5.pack()
f6 = Frame(root, bg='LightSkyBlue1')
f6.pack()
f7 = Frame(root, bg='LightSkyBlue1')
f7.pack()
f8 = Frame(root, bg='LightSkyBlue1')
f8.pack()
f9 = Frame(root, bg='LightSkyBlue1')
f9.pack()
f10 = Frame(root, bg='LightSkyBlue1')
f10.pack(fill=BOTH, expand=1)


# Create a StringVar to store the selected options
matrix = StringVar()
matrix.set("Import from a file")
diap = BooleanVar()

# Create radio buttons
for text, option in OPTIONS:
    Radiobutton(f1, text=text, variable=matrix, value=option, font=("Arial", 14, 'bold'), fg='#000000',
                bg='LightSkyBlue1', pady='3').pack()


@numba.jit(nopython=True)
def generate_sparse_matrix(dim1, dim2, diag, non_zero):    #We created our random from (-100,100) generator for sparse matrices or diagonal matrices
    A = np.zeros((dim1, dim2), dtype=float)                 
    if diag and dim1 == dim2:
        for i in range(dim1):
            A[i][i] = random.uniform(-100, 100)
    else:
        for _ in range(non_zero):
            A[random.randrange(dim1)][random.randrange(dim2)] = random.uniform(-100, 100)
    return A



@numba.jit(nopython=True)
def generate_b(dim1):           #Here we created a random generator for a dense array b
    b=np.empty(dim1)
    for i in range(dim1):
        b[i]=random.uniform(-100,100)
    return b


def csr_format(A):                          #Here is compressed type (csr_format) for the saprse matrices
    # CSR format
    a, col_idx = np.nonzero(A)

    data = np.empty(len(a), dtype=A.dtype)
    row_ptr = np.empty(A.shape[0] + 1, dtype=np.int64)

    start = a[0]
    count = 0
    row_ptr[0] = 0

    for i in range(len(a)):
        data[i] = A[a[i]][col_idx[i]]
        if start != a[i]:
            count += 1
            row_ptr[count] = row_ptr[count - 1] + np.count_nonzero(a == count - 1)
            start = a[i]

    row_ptr[-1] = len(data)

    return data, col_idx, row_ptr




@numba.jit(nopython=True)
def gauss_numba(A, b):  # A ο κυριος πινακας και β η στηλη      #Here is the gauss elimination method

    for k in range(len(b)):
        # We change the pivot element if it is zero
        if A[k, k] == 0:
            for i in range(k + 1, len(b)):
                if A[i, k] != 0:
                    for j in range(k, len(b)):
                        A[k, j], A[i, j] = A[i, j], A[k, j]
                    b[k], b[i] = b[i], b[k]
                    break

        # We divide the first row so that the pivot element become 1
        odhgo_stoixeio = A[k, k]
        for j in range(k, len(b)):
            A[k, j] /= odhgo_stoixeio
        b[k] /= odhgo_stoixeio
        # We make the other elements on the pivot column 0
        for i in range(0, len(b)):
            if i == k or A[i, k] == 0: continue  # We dont want to make the element on the diagon 0
            l=A[i,k]
            for j in range(k, len(b)):
                A[i, j] = A[i, j] - l * A[k, j]
            b[i] = b[i] - l* b[k]
    return b

def solver(A, b, dim1, dim2):  #Here is our main solver which solves matrices with nad without numba
    global start
    start = timer()
    data, col_idx, row_ptr = csr_format(A)
    A = sp.sparse.csr_matrix((data, col_idx, row_ptr), shape=(dim1, dim2)).toarray()
    x=scipy.sparse.linalg.spsolve(A,b)
    global end 
    end = timer()
    global start_n
    start_n = timer()
    x_n = gauss_numba(A, b)
    global end_n 
    end_n = timer()
    
    
    
    global solution    #Here we project the solution briefly in order to be nicer in the interface
    solution = "[{:.2f}, {:.2f}, {:.2f}, {:.2f} . . . {:.2f}, {:.2f}, {:.2f}, {:.2f}]".format(float(x[0]),float(x[1]),float(x[2]),float(x[3]),float(x[-1]),float(x[-2]),float(x[-3]),float(x[-4]))

    return solution


def import_file():
    x = ['1000no', '2000no', '3000no','1000yes']  #Here is the code we used to  import from the binary type files that we created
    y = x[random.randint(0, 3)]
    dim1, dim2 = int(y[:4]), int(y[:4])
    with open('matrix{}'.format(y), 'rb') as f:
        data = np.load(f)
        col = np.load(f)
        row = np.load(f)
        b = np.load(f)

    A = sp.sparse.coo_matrix((data, (row, col)), shape=(dim1, dim2)).toarray()

    return A, b, dim1,dim2


def myGet():                    #this function takes the elements from the interface, generate solvable matrices and project them in the interface 
    dim1 = int(e.get())
    dim2 = int(w.get())
    non_zero = int(p.get())
    diag = diap.get()
    while True:
        A = generate_sparse_matrix(dim1, dim2, diag, non_zero)
        b = generate_b(dim1)
        Ab=np.concatenate((A, b[:, np.newaxis]), axis=1)
        if np.linalg.matrix_rank(A) == np.linalg.matrix_rank(Ab):
            lbl1= Label(f10, text="SOLUTION:", font=("Arial", 14, 'bold'), fg='black',bg='LightSkyBlue1').pack()
            lbl2 = Label(f10, text= solver(A, b, dim1, dim2), font=("Arial", 14, 'bold'), fg='black',bg='LightSkyBlue1').pack()
            lbl3 = Label(f10, text="Time with numba: " + str(end_n - start_n)[:6]+' sec' , font=("Arial", 14, 'bold'), fg='black',bg='LightSkyBlue1').pack()
            lbl4 = Label(f10, text="Time without numba: "+ str(end - start)[:6]+' sec', font=("Arial", 14, 'bold'), fg='black',bg='LightSkyBlue1').pack()
            break
        else:
            print("not solvable")


def main(value):
    if value == "import":   #Here is the import from a file option 
        root.geometry("650x500")
        A, b, dim1, dim2 = import_file()
        lbl1= Label(f10, text="SOLUTION:", font=("Arial", 14, 'bold'), fg='black',bg='LightSkyBlue1').pack(pady=10)
        lbl2 = Label(f10, text=solver(A, b, dim1, dim2), font=("Arial", 14, 'bold'), fg='black',bg='LightSkyBlue1').pack(pady=10)
        lbl3 = Label(f10, text="Time with numba: " + str(end_n - start_n)[:6]+' sec' , font=("Arial", 14, 'bold'), fg='black',bg='LightSkyBlue1').pack(pady=10)
        lbl4 = Label(f10, text="Time without numba: "+ str(end - start)[:6]+' sec', font=("Arial", 14, 'bold'), fg='black',bg='LightSkyBlue1').pack()
        myButton3 = Button(f9, text="Restart", font=("Arial", 14), bg='black', fg='white', command=restart)
        myButton3.grid(row=0, column=1)

    elif value == "generate":   #Here is the generate option
        root.geometry("650x600")
        myLabel1 = Label(f3, text=" Give dimensions (First rows, then columns)", font=("Arial", 14, 'bold'),fg='black', bg='LightSkyBlue1').pack()
        global e
        e = Entry(f4, font=("Arial", 14, 'bold'))
        e.grid(row=0, column=0, padx=2)
        global w
        w = Entry(f4, font=("Arial", 14, 'bold'))
        w.grid(row=0, column=1, padx=2)
        myLabel2 = Label(f5, text=" Is it diagonal?", font=("Arial", 14, 'bold'), fg='black',bg='LightSkyBlue1').pack()
        t = Radiobutton(f6, text='Yes', font=("Arial", 14, 'bold'), fg='#000000', bg='LightSkyBlue1', pady='3',variable=diap, value=True)
        t.grid(row=0, column=0, padx=3)
        h = Radiobutton(f6, text='No', font=("Arial", 14, 'bold'), fg='#000000', bg='LightSkyBlue1', pady='3',variable=diap, value=False)
        h.grid(row=0, column=1, padx=3)
        myLabel3 = Label(f7, text="Non zero values", font=("Arial", 14, 'bold'), fg='black',bg='LightSkyBlue1').pack()
        global p
        p = Entry(f7, font=("Arial", 14, 'bold'))
        p.pack(pady=5)
        myButton1 = Button(f9, text="Save my choises", command=myGet, font=("Arial", 14), bg='black', fg='white')
        myButton1.grid(row=0, column=0, padx=4)
        myButton2 = Button(f9, text="Restart", font=("Arial", 14), bg='black', fg='white', command=restart)
        myButton2.grid(row=0, column=1)


def restart():   #The restart buttons detroys the program an reopens it
    root.destroy()
    os.startfile("Project.pyw")
    

# Create "Run" button to execute clicked function
myButton = Button(f2, text="Run", command=lambda: main(matrix.get()), font=("Arial", 14), bg='black', fg='white', pady='2').pack(side='top')

root.mainloop()
