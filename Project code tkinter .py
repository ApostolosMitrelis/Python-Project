from tkinter import *
from PIL import ImageTk,Image

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


def clicked(value):
    myLabel = Label(root,text=value)
    myLabel.pack()
    if text == "Import from a file" :
         label1= Label(root,text="hello").pack()
    elif text == "Generate a random matrix":
        label2= Label(root,text="world").pack()


myButton = Button(root,text="Click to finalize option",command=lambda:clicked(matrix.get()))
myButton.pack()
mainloop()
