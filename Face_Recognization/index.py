import tkinter as tk
from tkinter import *
from tkinter.simpledialog import askstring

import faceData
import face_identification

root = tk.Tk()
root.title('Face Recognization')
bg=PhotoImage(file="photo.png")

def getdata():
    name = askstring('Name', 'Enter your name?')
    faceData.fun(name)

w=bg.width()+200
h=bg.height()
dim=str(w)+'x'+str(h)
root.geometry(dim)
root.configure(bg='#f8f8f8')
l= Label(root,image=bg)
l.place(x=0,y=0)
button1 = tk.Button(root, text='Face Data', width=25, command=lambda: getdata())
button1.place(x=410,y=150)

button2 = tk.Button(root, text='Face Identification', width=25, command=lambda: face_identification.fun())
button2.place(x=410,y=200)

button3 = tk.Button(root, text='Exit', width=5, command=root.destroy)
button3.place(x=485,y=250)


root.mainloop()