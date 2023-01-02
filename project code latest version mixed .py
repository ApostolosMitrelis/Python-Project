import numpy as np
import random
import scipy as sp
import os
import matplotlib.pylab as plt
from timeit import default_timer as timer
from tkinter import *
import os
import sys

root = Tk()
root.title('Project code tkinter')
root.geometry("700x700")
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
f10.pack()
######
# Create a StringVar to store the selected option
matrix = StringVar()
matrix.set("Import from a file")
diap= IntVar()
#numpa= IntVar()

# Create radio buttons
for text, option in OPTIONS:
    Radiobutton(f1, text=text, variable=matrix, value=option, font=("Arial", 14,'bold'), fg='#000000',bg='LightSkyBlue1',pady='3').pack()

diag = diap.get()
def generate_sparse_matrix(dim1,dim2,diag,non_zero):
    #generate random sparse matrix
    A = np.zeros((dim1,dim2), dtype = float)
    if diag == "Yes" and dim1 == dim2:
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

# Function to display entered information
##def myGet():
##    global lbl
##    noompa = numpa.get()
##    if diag == 1 and noompa == 1 :
##        lbl = Label(f10, text=e.get()+ "-----" + 'Nαι' +"-----"+ non_zero.get()+ "-----"+'Χρησιμοποιεις Numba', font=("Arial", 14,'bold'), fg='black',bg='LightSkyBlue1')
##        lbl.pack()
##        e.delete(0,END)
##        dim2.delete(0,END)
##        t.deselect()
##        non_zero.delete(0,END)
##        q.deselect()
##    elif diag == 2 and noompa == 1 :
##        lbl = Label(f10, text=e.get()+ "-----" + 'Oχι' +"-----"+ non_zero.get()+ "-----"+'Χρησιμοποιεις Numba', font=("Arial", 14,'bold'), fg='black',bg='LightSkyBlue1')
##        lbl.pack()
##        e.delete(0,END)
##        dim2.delete(0,END)
##        h.deselect()
##        non_zero.delete(0,END)
##        q.deselect()
##    elif diag == 1 and noompa == 2:
##        lbl = Label(f10, text=e.get()+ "-----" + 'Nαι' +"-----"+ non_zero.get()+ "-----"+'Δεν χρησιμοποιεις Numba', font=("Arial", 14,'bold'), fg='black',bg='LightSkyBlue1')
##        lbl.pack()
##        e.delete(0,END)
##        dim2.delete(0,END)
##        t.deselect()
##        non_zero.delete(0,END)
##        v.deselect()
##    elif diag == 2 and noompa == 2:
##        lbl = Label(f10, text=e.get()+ "-----" + 'Oχι' +"-----"+ non_zero.get+ "-----"+'Δεν χρησιμοποιεις Numba', font=("Arial", 14,'bold'), fg='black',bg='LightSkyBlue1')
##        lbl.pack()
##        e.delete(0,END)
##        dim2.delete(0,END)
##        h.deselect()
##        non_zero.delete(0,END)
##        v.deselect()

def myGet():
    global dim1
    dim1 = int(dim1.get())
    A = generate_sparse_matrix(dim1,dim2,diag,non_zero)
    b = generate_b(dim1)
    Ab = np.hstack((A,b)) 
    if np.linalg.matrix_rank(A) == np.linalg.matrix_rank(Ab):
        pass
        
    data, col_idx, row_ptr = csr_format(A)
    B = sp.sparse.csr_matrix((data,col_idx,row_ptr), shape=(dim1,dim2)).toarray()
    x = sp.sparse.linalg.spsolve(B,b)
        




def main(value):
        if value == "import" :
            label1= Label(f10, text="hello", font=("Arial", 14), fg='black',bg='LightSkyBlue1').pack()
        elif value == "generate":
            myLabel1 = Label(f3, text="Δώσε δίασταση του πίνακα (Πρωτα γραμμες, μετα στηλες)", font=("Arial", 14,'bold'), fg='black',bg='LightSkyBlue1').pack()
            global dim1 
            dim1 = Entry(f4, font=("Arial", 14,'bold'))
            dim1.grid(row=0,column=0,padx=2)
            global dim2
            dim2 = Entry(f4, font=("Arial", 14,'bold'))
            dim2.grid(row=0,column=1,padx=2)
            myLabel2 = Label(f5, text="Ναι ή οχι αν είναι διαγώνιος", font=("Arial", 14,'bold'), fg='black',bg='LightSkyBlue1').pack()
            global t
            t = Radiobutton(f6, text='Yes', font=("Arial", 14,'bold'), fg='#000000',bg='LightSkyBlue1',pady='3',variable=diap,value=1)
            t.grid(row=0,column=0,padx=3)
            global h 
            h = Radiobutton(f6, text='No', font=("Arial", 14,'bold'), fg='#000000',bg='LightSkyBlue1',pady='3',variable=diap,value=2)
            h.grid(row=0,column=1,padx=3)
            myLabel3 = Label(f7, text="Πλήθος μη μηδενικών στοιχείων", font=("Arial", 14,'bold'), fg='black',bg='LightSkyBlue1').pack()
            global non_zero
            non_zero = Entry(f7, font=("Arial", 14,'bold'))
            non_zero.pack(pady=5)
            #myLabel4 = Label(f7, text="Θες να χρησιμοποιησεις numba?", font=("Arial", 14,'bold'), fg='black',bg='LightSkyBlue1').pack()
##        global q
##        q = Radiobutton(f8, text='Ναι', font=("Arial", 14,'bold'), fg='#000000',bg='LightSkyBlue1',pady='3',variable=numpa,value=1)
##        q.grid(row=0,column=0,padx=3)
##        global v
##        v = Radiobutton(f8, text='Οχι', font=("Arial", 14,'bold'), fg='#000000',bg='LightSkyBlue1',pady='3',variable=numpa,value=2)
##        v.grid(row=0,column=1,padx=3)
        # Create button to save matrix information
            myButton1 = Button(f9, text="Save my choises", command=myGet, font=("Arial", 14), bg='black', fg='white')
            myButton1.grid(row=0,column=0,padx=4)
            myButton2 = Button(f9, text="Restart", font=("Arial", 14), bg='black', fg='white',command=restart)
            myButton2.grid(row=0,column=1)
        #if answer == '':
            #break
        #else:
        #dim, diag, non_zero = answer.split(",")
        #dim1, dim2 = dim.split("x")
        #dim1 = int(dim1)
        #dim2 = int(dim2)
       #non_zero = int(non_zero)
        
        

def restart():
    root.destroy()
    os.startfile("Project code tkinter latest version.pyw")
    
# Create "Run" button to execute clicked function
myButton = Button(f2, text="Run", command=lambda:main(matrix.get()), font=("Arial", 14), bg='black', fg='white',pady='2').pack(side ='top')

root.mainloop()  

