from tkinter import *


root = Tk()
root.title('Project code tkinter')
root.geometry("400x400")



OPTIONS = [
    ("Import from a file","import"),
    ("Generate a random matrix","generate")
]

matrix = StringVar()
matrix.set("Import from a file")

for text, option in OPTIONS:
    Radiobutton(root,text=text,variable=matrix,value=option).pack(anchor=N)

def myGet():
    lbl = Label(root,text= e.get()+ "|" + t.get() +"|"+ g.get()).pack()
    e.delete(0,END)
    t.delete(0,END)
    g.delete(0,END)
    
def clicked(value):
    if value == "import" :
         label1= Label(root,text="hello").pack()
    elif value == "generate":
        myLabel1 = Label(root,text = "Δώσε δίασταση του πίνακα (πχ.1000x1000)").pack()
        global e
        e = Entry(root)
        e.pack()
        myLabel2 = Label(root,text = "ναι ή οχι αν είναι διαγώνιο").pack()
        global t
        t = Entry(root)
        t.pack()
        myLabel3 = Label(root,text = "πλήθος μη μηδενικών στοιχείων").pack()
        global g
        g = Entry(root)
        g.pack()
        myButton1= Button(root,text="Save my choises",command= myGet).pack()


myButton = Button(root,text="Run",command=lambda:clicked(matrix.get()))
myButton.pack()
mainloop()
