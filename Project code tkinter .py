from tkinter import *

root = Tk()
root.title('Project code tkinter')
root.geometry("500x500")
root.configure(bg='deep sky blue')

# Set up options for radio buttons
OPTIONS = [
    ("Import from a file","import"),
    ("Generate a random matrix","generate")
]

# Create a StringVar to store the selected option
matrix = StringVar()
matrix.set("Import from a file")

# Create radio buttons
for text, option in OPTIONS:
    Radiobutton(root, text=text, variable=matrix, value=option, font=("Arial", 14,'bold'), fg='#000000',bg='deep sky blue').pack(anchor=N)

# Function to display entered information
def myGet():
    lbl = Label(root, text=e.get()+ "|" + t.get() +"|"+ g.get(), font=("Arial", 14,'bold'), fg='black',bg='deep sky blue').pack()
    e.delete(0,END)
    t.delete(0,END)
    g.delete(0,END)

# Function to execute based on selected option
def clicked(value):
    if value == "import" :
        label1= Label(root, text="hello", font=("Arial", 14), fg='#333333').pack()
    elif value == "generate":
        # Display prompts and entry fields for matrix information
        myLabel1 = Label(root, text="Δώσε δίασταση του πίνακα (πχ.1000x1000)", font=("Arial", 14,'bold'), fg='black',bg='deep sky blue').pack()
        global e
        e = Entry(root, font=("Arial", 14,'bold'))
        e.pack()
        myLabel2 = Label(root, text="Ναι ή οχι αν είναι διαγώνιος", font=("Arial", 14,'bold'), fg='black',bg='deep sky blue').pack()
        global t
        t = Entry(root, font=("Arial", 14,'bold'))
        t.pack()
        myLabel3 = Label(root, text="πλήθος μη μηδενικών στοιχείων", font=("Arial", 14,'bold'), fg='black',bg='deep sky blue').pack()
        global g
        g = Entry(root, font=("Arial", 14,'bold'))
        g.pack()
        # Create button to save matrix information
        myButton1 = Button(root, text="Save my choises", command=myGet, font=("Arial", 14), bg='black', fg='white').pack()

# Create "Run" button to execute clicked function
myButton = Button(root, text="Run", command=lambda:clicked(matrix.get()), font=("Arial", 14), bg='black', fg='white')
myButton.pack()

root.mainloop()
