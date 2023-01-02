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
numpa= IntVar()


# Create radio buttons
for text, option in OPTIONS:
    Radiobutton(f1, text=text, variable=matrix, value=option, font=("Arial", 14,'bold'), fg='#000000',bg='LightSkyBlue1',pady='3').pack()

# Function to display entered information
def myGet():
    print(type(int(dim1.get())))
    global lbl
    diag = diap.get()
    noompa = numpa.get()
    if diag == 1 and noompa == 1 :
        lbl = Label(f10, text=dim1.get()+ "-----" + 'Nαι' +"-----"+ non_zero.get()+ "-----"+'Χρησιμοποιεις Numba', font=("Arial", 14,'bold'), fg='black',bg='LightSkyBlue1')
        lbl.pack()
        dim1.delete(0,END)
        dim2.delete(0,END)
        t.deselect()
        non_zero.delete(0,END)
        q.deselect()
    elif diag == 2 and noompa == 1 :
        lbl = Label(f10, text=dim1.get()+ "-----" + 'Oχι' +"-----"+ non_zero.get()+ "-----"+'Χρησιμοποιεις Numba', font=("Arial", 14,'bold'), fg='black',bg='LightSkyBlue1')
        lbl.pack()
        dim1.delete(0,END)
        dim2.delete(0,END)
        h.deselect()
        non_zero.delete(0,END)
        q.deselect()
    elif diag == 1 and noompa == 2:
        lbl = Label(f10, text=dim1.get()+ "-----" + 'Nαι' +"-----"+ non_zero.get()+ "-----"+'Δεν χρησιμοποιεις Numba', font=("Arial", 14,'bold'), fg='black',bg='LightSkyBlue1')
        lbl.pack()
        dim1.delete(0,END)
        dim2.delete(0,END)
        t.deselect()
        non_zero.delete(0,END)
        v.deselect()
    elif diag == 2 and noompa == 2:
        lbl = Label(f10, text=dim1.get()+ "-----" + 'Oχι' +"-----"+ non_zero.get+ "-----"+'Δεν χρησιμοποιεις Numba', font=("Arial", 14,'bold'), fg='black',bg='LightSkyBlue1')
        lbl.pack()
        dim1.delete(0,END)
        dim2.delete(0,END)
        h.deselect()
        non_zero.delete(0,END)
        v.deselect()

# Function to execute based on selected option
def clicked(value):
    if value == "import" :
        label1= Label(f10, text="hello", font=("Arial", 14), fg='black',bg='LightSkyBlue1').pack()
    elif value == "generate":
        # Display prompts and entry fields for matrix information
        myLabel1 = Label(f3, text="Δώσε δίασταση του πίνακα (Πρωτα γραμμες, μετα στηλες)", font=("Arial", 14,'bold'), fg='black',bg='LightSkyBlue1').pack()
        global dim1
        dim1 = Entry(f4, font=("Arial", 14,'bold'))
        dim1.grid(row=0,column=0,padx=2)
        global dim2
        dim2 = Entry(f4, font=("Arial", 14,'bold'))
        dim2.grid(row=0,column=1,padx=2)
        myLabel2 = Label(f5, text="Ναι ή οχι αν είναι διαγώνιος", font=("Arial", 14,'bold'), fg='black',bg='LightSkyBlue1').pack()
        global t
        t = Radiobutton(f6, text='Ναι', font=("Arial", 14,'bold'), fg='#000000',bg='LightSkyBlue1',pady='3',variable=diap,value=1)
        t.grid(row=0,column=0,padx=3)
        global h 
        h = Radiobutton(f6, text='Οχι', font=("Arial", 14,'bold'), fg='#000000',bg='LightSkyBlue1',pady='3',variable=diap,value=2)
        h.grid(row=0,column=1,padx=3)
        myLabel3 = Label(f7, text="Πλήθος μη μηδενικών στοιχείων", font=("Arial", 14,'bold'), fg='black',bg='LightSkyBlue1').pack()
        global non_zero
        non_zero = Entry(f7, font=("Arial", 14,'bold'))
        non_zero.pack(pady=5)
        myLabel4 = Label(f7, text="Θες να χρησιμοποιησεις numba?", font=("Arial", 14,'bold'), fg='black',bg='LightSkyBlue1').pack()
        global q
        q = Radiobutton(f8, text='Ναι', font=("Arial", 14,'bold'), fg='#000000',bg='LightSkyBlue1',pady='3',variable=numpa,value=1)
        q.grid(row=0,column=0,padx=3)
        global v
        v = Radiobutton(f8, text='Οχι', font=("Arial", 14,'bold'), fg='#000000',bg='LightSkyBlue1',pady='3',variable=numpa,value=2)
        v.grid(row=0,column=1,padx=3)
        # Create button to save matrix information
        myButton1 = Button(f9, text="Save my choises", command=myGet, font=("Arial", 14), bg='black', fg='white')
        myButton1.grid(row=0,column=0,padx=4)
        myButton2 = Button(f9, text="Restart", font=("Arial", 14), bg='black', fg='white',command=restart)
        myButton2.grid(row=0,column=1)


def restart():
    root.destroy()
    os.startfile("Project code tkinter latest version.pyw")
    
# Create "Run" button to execute clicked function
myButton = Button(f2, text="Run", command=lambda:clicked(matrix.get()), font=("Arial", 14), bg='black', fg='white',pady='2').pack(side ='top')


root.mainloop()
