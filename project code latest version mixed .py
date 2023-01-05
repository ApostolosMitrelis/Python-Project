from timeit import default_timer as timer
from tkinter import ttk
from tkinter import *
import numpy as np
import scipy as sp
import random
import os
from timeit import default_timer as timer

root = Tk()
root.title('Project code tkinter')
root.geometry("500x300")
root.configure(bg='LightSkyBlue1')

# Set up options for radio buttons
OPTIONS = [
    ("Import from a file","import"),
    ("Generate a random matrix","generate")
]

######
f1 = Frame(root,bg='LightSkyBlue1')
f1.pack()
f2 = Frame(root,bg='LightSkyBlue1')
f2.pack()
f3 = Frame(root,bg='LightSkyBlue1')
f3.pack()
f4 = Frame(root,bg='LightSkyBlue1')
f4.pack()
f5 = Frame(root,bg='LightSkyBlue1')
f5.pack()
f6 = Frame(root,bg='LightSkyBlue1')
f6.pack()
f7 = Frame(root,bg='LightSkyBlue1')
f7.pack()
f8 = Frame(root,bg='LightSkyBlue1')
f8.pack()
f9 = Frame(root,bg='LightSkyBlue1')
f9.pack()
f10 = Frame(root,bg='LightSkyBlue1')
f10.pack(fill=BOTH,expand=1)
f12 = Frame(root,bg='LightSkyBlue1')
f12.pack(fill=BOTH,expand=1)
# Create a StringVar to store the selected option
matrix = StringVar()
matrix.set("Import from a file")
diap= BooleanVar()

# Create radio buttons
for text, option in OPTIONS:
    Radiobutton(f1, text=text, variable=matrix, value=option, font=("Arial", 14,'bold'), fg='#000000',bg='LightSkyBlue1',pady='3').pack()

def generate_sparse_matrix(dim1,dim2,diag,non_zero):
    #generate random sparse matrix
    A = np.zeros((dim1,dim2), dtype = float)
    if diag and dim1 == dim2:
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

def solver(A,b, dim1, dim2):
    data, col_idx, row_ptr = csr_format(A)
    A = sp.sparse.csr_matrix((data,col_idx,row_ptr), shape=(dim1,dim2)).toarray()
    start = timer()
    x = sp.sparse.linalg.spsolve(A,b)
    end = timer()
    print('time: ', end - start)

    return x

def import_file():
    x = ['1000no','2000no','3000no']
    y = x[random.randint(0,2)]
    dim1, dim2 = int(y[:4]), int(y[:4])
    with open('matrix{}'.format(y), 'rb') as f:
        data = np.load(f)
        col = np.load(f)
        row = np.load(f)
        b = np.load(f)

    A = sp.sparse.coo_matrix((data,(row,col)), shape=(dim1,dim2)).toarray()
    

    return A, b, dim1, dim2
    

def myGet():
    dim1 = int(e.get())
    dim2 = int(w.get())
    non_zero = int(p.get())
    diag = diap.get()
    while True:
        A = generate_sparse_matrix(dim1,dim2,diag,non_zero)
        b = generate_b(dim1)
        Ab = np.hstack((A,b)) 
        if np.linalg.matrix_rank(A) == np.linalg.matrix_rank(Ab):
            my_canvas = Canvas(f12,bg='LightSkyBlue1',highlightthickness=0)
            my_canvas.pack(side=LEFT,fill=BOTH,expand=1)
            my_scrollbar = ttk.Scrollbar(f12,orient=VERTICAL,command=my_canvas.yview)
            my_scrollbar.pack(side=RIGHT,fill=Y)
            my_canvas.configure(yscrollcommand=my_scrollbar.set)
            my_canvas.bind('<Configure>',lambda e: my_canvas.configure(scrollregion = my_canvas.bbox("all")))
            f13 = Frame(my_canvas,bg='LightSkyBlue1')
            my_canvas.create_window((0,0),window=f13,anchor='nw')
            print(solver(A,b,dim1,dim2))
            telos = Label(f13, text=(solver(A,b,dim1,dim2)), font=("Arial", 14), fg='black',bg='mint cream')
            telos.pack(fill='x',expand=1)
            break
        else:
            print("not solvable")

def main(value):
    if value == "import" :
        root.geometry("710x500")
        my_canvas1 = Canvas(f10,bg='LightSkyBlue1', highlightthickness=0)
        my_canvas1.pack(side=LEFT,fill=BOTH,expand=1)
        my_scrollbar1 = ttk.Scrollbar(f10,orient=VERTICAL,command=my_canvas1.yview)
        my_scrollbar1.pack(side=RIGHT,fill=Y)
        my_canvas1.configure(yscrollcommand=my_scrollbar1.set)
        my_canvas1.bind('<Configure>',lambda e: my_canvas1.configure(scrollregion = my_canvas1.bbox("all")))
        f11 = Frame(my_canvas1,bg='LightSkyBlue1')
        my_canvas1.create_window((0,0),window=f11,anchor='nw')
        A, b, dim1, dim2 = import_file()
        print(solver(A,b,dim1,dim2))
        telos = Label(f11, text=(solver(A,b,dim1,dim2)), font=("Arial", 14), fg='black',bg='mint cream')
        telos.pack(fill='x',expand=1)
        myButton3 = Button(f9, text="Restart", font=("Arial", 14), bg='black', fg='white',command=restart)
        myButton3.grid(row=0,column=1)

    elif value == "generate":
        root.geometry("900x700")
        myLabel1 = Label(f3, text="Δώσε δίασταση του πίνακα (Πρωτα γραμμες, μετα στηλες)", font=("Arial", 14,'bold'), fg='black',bg='LightSkyBlue1').pack()
        global e 
        e = Entry(f4, font=("Arial", 14,'bold'))
        e.grid(row=0,column=0,padx=2)
        global w
        w = Entry(f4, font=("Arial", 14,'bold'))
        w.grid(row=0,column=1,padx=2)
        myLabel2 = Label(f5, text="Ναι ή οχι αν είναι διαγώνιος", font=("Arial", 14,'bold'), fg='black',bg='LightSkyBlue1').pack()
        t = Radiobutton(f6, text='Yes', font=("Arial", 14,'bold'), fg='#000000',bg='LightSkyBlue1',pady='3',variable=diap,value=True)
        t.grid(row=0,column=0,padx=3)
        h = Radiobutton(f6, text='No', font=("Arial", 14,'bold'), fg='#000000',bg='LightSkyBlue1',pady='3',variable=diap,value=False)
        h.grid(row=0,column=1,padx=3)
        myLabel3 = Label(f7, text="Πλήθος μη μηδενικών στοιχείων", font=("Arial", 14,'bold'), fg='black',bg='LightSkyBlue1').pack()
        global p
        p = Entry(f7, font=("Arial", 14,'bold'))
        p.pack(pady=5)
        # Create button to save matrix information
        myButton1 = Button(f9, text="Save my choises", command=myGet, font=("Arial", 14), bg='black', fg='white')
        myButton1.grid(row=0,column=0,padx=4)
        # Create button to Restart the Program
        myButton2 = Button(f9, text="Restart", font=("Arial", 14), bg='black', fg='white',command=restart)
        myButton2.grid(row=0,column=1)
        
def restart():
    root.destroy()
    os.startfile("latest clean mixed.pyw")
    
# Create "Run" button to execute clicked function
myButton = Button(f2, text="Run", command=lambda:main(matrix.get()), font=("Arial", 14), bg='black', fg='white',pady='2').pack(side ='top')

root.mainloop()  
