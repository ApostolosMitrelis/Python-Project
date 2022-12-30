from tkinter import *
import os
import sys

root = Tk()
root.title('Project code tkinter')
root.geometry("700x700")
root.configure(bg='deep sky blue')

# Set up options for radio buttons
OPTIONS = [
    ("Import from a file","import"),
    ("Generate a random matrix","generate")
]
######
f1 = Frame(root,bg='deep sky blue')
f1.pack()
f2 = Frame(root,bg='deep sky blue')
f2.pack()
f3 = Frame(root,bg='deep sky blue')
f3.pack()
f4 = Frame(root,bg='deep sky blue')
f4.pack()
f5 = Frame(root,bg='deep sky blue')
f5.pack()
f6 = Frame(root,bg='deep sky blue')
f6.pack()
f7 = Frame(root,bg='deep sky blue')
f7.pack()


######
# Create a StringVar to store the selected option
matrix = StringVar()
matrix.set("Import from a file")
diag= IntVar()

# Create radio buttons
for text, option in OPTIONS:
    Radiobutton(f1, text=text, variable=matrix, value=option, font=("Arial", 14,'bold'), fg='#000000',bg='deep sky blue',pady='3').pack()

# Function to display entered information
def myGet():
    global lbl
    control = diag.get()
    if control == 1:
        lbl = Label(f7, text=e.get()+ "|" + 'Nαι' +"|"+ g.get(), font=("Arial", 14,'bold'), fg='black',bg='deep sky blue')
        lbl.pack()
        e.delete(0,END)
        t.deselect()
        g.delete(0,END)
    elif control == 2:
        lbl = Label(f7, text=e.get()+ "|" + 'Oχι' +"|"+ g.get(), font=("Arial", 14,'bold'), fg='black',bg='deep sky blue')
        lbl.pack()
        e.delete(0,END)
        h.deselect()
        g.delete(0,END)

# Function to execute based on selected option
def clicked(value):
    if value == "import" :
        label1= Label(f7, text="hello", font=("Arial", 14), fg='#333333').pack()
    elif value == "generate":
        # Display prompts and entry fields for matrix information
        myLabel1 = Label(f3, text="Δώσε δίασταση του πίνακα (πχ.1000x1000)", font=("Arial", 14,'bold'), fg='black',bg='deep sky blue').pack()
        global e
        e = Entry(f3, font=("Arial", 14,'bold'))
        e.pack()
        myLabel2 = Label(f3, text="Ναι ή οχι αν είναι διαγώνιος", font=("Arial", 14,'bold'), fg='black',bg='deep sky blue').pack()
        global t
        t = Radiobutton(f4, text='Ναι', font=("Arial", 14,'bold'), fg='#000000',bg='deep sky blue',pady='3',variable=diag,value=1)
        t.grid(row=0,column=0,padx=3)
        global h 
        h = Radiobutton(f4, text='Οχι', font=("Arial", 14,'bold'), fg='#000000',bg='deep sky blue',pady='3',variable=diag,value=2)
        h.grid(row=0,column=1,padx=3)
        myLabel3 = Label(f5, text="Πλήθος μη μηδενικών στοιχείων", font=("Arial", 14,'bold'), fg='black',bg='deep sky blue').pack()
        global g
        g = Entry(f5, font=("Arial", 14,'bold'))
        g.pack(pady=5)
        # Create button to save matrix information
        myButton1 = Button(f6, text="Save my choises", command=myGet, font=("Arial", 14), bg='black', fg='white')
        myButton1.grid(row=0,column=0,padx=4)
        myButton2 = Button(f6, text="Restart", font=("Arial", 14), bg='black', fg='white',command=restart)
        myButton2.grid(row=0,column=1)


def restart():
    root.destroy()
    os.startfile("frame test.pyw")
    
# Create "Run" button to execute clicked function
myButton = Button(f2, text="Run", command=lambda:clicked(matrix.get()), font=("Arial", 14), bg='black', fg='white',pady='2').pack(side ='top')


root.mainloop()
