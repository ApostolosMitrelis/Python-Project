from timeit import default_timer as timer
from tkinter import ttk
from tkinter import *
import numpy as np
import scipy as sp
import scipy.sparse
import random
import os
from timeit import default_timer as timer
import matplotlib.pyplot as plt
import numba


root = Tk()
root.title('Project code tkinter')
root.geometry("500x300")
root.configure(bg='LightSkyBlue1')

# Set up options for radio buttons
OPTIONS = [
    ("Import from a file", "import"),
    ("Generate a random matrix", "generate")
]

#Frames
f1 = Frame(root, bg='LightSkyBlue1')
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


# Create a StringVar to store the selected option
matrix = StringVar()
matrix.set("Import from a file")
diap = BooleanVar()

# Create radio buttons
for text, option in OPTIONS:
    Radiobutton(f1, text=text, variable=matrix, value=option, font=("Arial", 14, 'bold'), fg='#000000',
                bg='LightSkyBlue1', pady='3').pack()


@numba.jit(nopython=True)
def generate_sparse_matrix(dim1, dim2, diag, non_zero):
    A = np.zeros((dim1, dim2), dtype=float)
    if diag and dim1 == dim2:
        for i in range(dim1):
            A[i][i] = random.randint(-100, 100)
    else:
        for _ in range(non_zero):
            A[random.randrange(dim1)][random.randrange(dim2)] = random.randint(-100, 100)
    return A


@numba.jit(nopython=True)
def generate_b(dim1):
    #generate random b array of 1 dimension
    b=np.empty(dim1)
    for i in range(dim1):
        b[i]=random.randint(-100,100)
    return b


@numba.jit(nopython=True)
def csr_format(A):
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


def csc_format(A):
    # CSC format
    A = A.T
    data, row_idx, col_ptr = csr_format(A)
    return data, row_idx, col_ptr


def coo_format(A):
    # COO format
    row, col = np.nonzero(A)

    data = np.array([])

    for i in range(len(row)):
        data = np.append(data, A[row[i]][col[i]])

    return data, col, row


def solver(A, b, dim1, dim2):
    data, col_idx, row_ptr = csr_format(A)
    A = sp.sparse.csr_matrix((data, col_idx, row_ptr), shape=(dim1, dim2)).toarray()
    global start
    start = timer()
    x = np.linalg.solve(A, b)
    global end 
    end = timer()
    print('time: ', end - start)
    global solution
    solution = "[{:.2f}, {:.2f}, {:.2f}, {:.2f} . . . {:.2f}, {:.2f}, {:.2f}, {:.2f}]".format(float(x[0]),float(x[1]),float(x[2]),float(x[3]),float(x[-1]),float(x[-2]),float(x[-3]),float(x[-4]))

    return solution


def import_file():
    x = ['1000no', '2000no', '3000no','1000yes']
    y = x[random.randint(0, 3)]
    dim1, dim2 = int(y[:4]), int(y[:4])
    with open('matrix{}'.format(y), 'rb') as f:
        data = np.load(f)
        col = np.load(f)
        row = np.load(f)
        b = np.load(f)

    A = sp.sparse.coo_matrix((data, (row, col)), shape=(dim1, dim2)).toarray()

    return A, b, dim1, dim2


def myGet():
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
            lbl2 = Label(f10, text= solver(A, b, dim1, dim2), font=("Arial", 14, 'bold'), fg='black',bg='gray').pack()
            lbl3 = Label(f10, text="Time with numba: " + str(end - start)+'s' , font=("Arial", 14, 'bold'), fg='black',bg='LightSkyBlue1').pack()
            lbl4 = Label(f10, text="Time without numba: "+ str(end - start)+'s', font=("Arial", 14, 'bold'), fg='black',bg='LightSkyBlue1').pack()
            break
        else:
            print("not solvable")


def main(value):
    if value == "import":
        root.geometry("650x500")
        A, b, dim1, dim2 = import_file()
        print(solver(A, b, dim1, dim2))
        lbl1= Label(f10, text="SOLUTION:", font=("Arial", 14, 'bold'), fg='black',bg='LightSkyBlue1').pack()
        lbl2 = Label(f10, text=solver(A, b, dim1, dim2), font=("Arial", 14, 'bold'), fg='black',bg='gray').pack()
        lbl3 = Label(f10, text="Time with numba: " + str(end - start)+'s' , font=("Arial", 14, 'bold'), fg='black',bg='LightSkyBlue1').pack()
        lbl4 = Label(f10, text="Time without numba: "+ str(end - start)+'s', font=("Arial", 14, 'bold'), fg='black',bg='LightSkyBlue1').pack()
        myButton3 = Button(f9, text="Restart", font=("Arial", 14), bg='black', fg='white', command=restart)
        myButton3.grid(row=0, column=1)

    elif value == "generate":
        root.geometry("650x600")
        myLabel1 = Label(f3, text="Δώσε δίασταση του πίνακα (Πρωτα γραμμες, μετα στηλες)", font=("Arial", 14, 'bold'),fg='black', bg='LightSkyBlue1').pack()
        global e
        e = Entry(f4, font=("Arial", 14, 'bold'))
        e.grid(row=0, column=0, padx=2)
        global w
        w = Entry(f4, font=("Arial", 14, 'bold'))
        w.grid(row=0, column=1, padx=2)
        myLabel2 = Label(f5, text="Ναι ή οχι αν είναι διαγώνιος", font=("Arial", 14, 'bold'), fg='black',bg='LightSkyBlue1').pack()
        t = Radiobutton(f6, text='Yes', font=("Arial", 14, 'bold'), fg='#000000', bg='LightSkyBlue1', pady='3',variable=diap, value=True)
        t.grid(row=0, column=0, padx=3)
        h = Radiobutton(f6, text='No', font=("Arial", 14, 'bold'), fg='#000000', bg='LightSkyBlue1', pady='3',variable=diap, value=False)
        h.grid(row=0, column=1, padx=3)
        myLabel3 = Label(f7, text="Πλήθος μη μηδενικών στοιχείων", font=("Arial", 14, 'bold'), fg='black',bg='LightSkyBlue1').pack()
        global p
        p = Entry(f7, font=("Arial", 14, 'bold'))
        p.pack(pady=5)
        # Create button to save matrix information
        myButton1 = Button(f9, text="Save my choises", command=myGet, font=("Arial", 14), bg='black', fg='white')
        myButton1.grid(row=0, column=0, padx=4)
        # Create button to Restart the Program
        myButton2 = Button(f9, text="Restart", font=("Arial", 14), bg='black', fg='white', command=restart)
        myButton2.grid(row=0, column=1)


def restart():
    root.destroy()
    os.startfile("omada 16.pyw")
    

# Create "Run" button to execute clicked function
myButton = Button(f2, text="Run", command=lambda: main(matrix.get()), font=("Arial", 14), bg='black', fg='white', pady='2').pack(side='top')

root.mainloop()
