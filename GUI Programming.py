
# Tkinter - Toolkit for python GUI Programming
import tkinter

#tkinter._test()

from tkinter import Tk
from tkinter import ttk
from tkinter import *
'''
root=Tk()
# CREATE LABELS

root.title("First GUI Using Python")
ttk.Button(root, text="Hello Python...!").grid()
root.mainloop()
'''
# CREATE BUTTONS
'''
frame= Frame(root)
labetText= StringVar()
label = Label(frame,textvariable= labetText)
button=Button(frame, text="Hey, I am a button")
labetText.set("Hey... Whatsapp...!")
label.pack()
button.pack()
frame.pack()

root,mainloop()

'''
# Create Frame with Buttons
'''
frame= Frame(root)
Label(frame, text="Hey!").pack()
Button(frame,text="B1").pack(side=LEFT, fill=Y)
Button(frame,text="B2").pack(side=RIGHT, fill=X)
Button(frame,text="B3").pack(side=TOP, fill=Y)
Button(frame,text="B4").pack(side=LEFT, fill=Y)
frame.pack()
root.mainloop()

'''

'''
# CREATE GRID - Means create entry box for taking input from user
# Create Input button, Radio Button & Check Button
Label(root, text="Name").grid(row=0, column=0, sticky=N)
Entry(root, width=50).grid(row=0,column=1)

Button(root, text="Submit").grid(row=0, column=5)

# CREATE RADIO BUTTON
Label(root, text="Gender").grid(row=1, column=0, sticky=N)
Radiobutton(root, text="M",value=1).grid(row=1, column=1, sticky=N)
Radiobutton(root, text="F",value=2).grid(row=1,column=2, sticky=N)
# CREATE CHECK BUTTON
Label(root, text="Courses").grid(row=2, column=0, sticky=N)
Checkbutton(root,text="Python").grid(row=2,column=1, sticky=N)
Checkbutton(root,text="Django").grid(row=3,column=1, sticky=N)
Checkbutton(root,text="Flask").grid(row=4,column=1, sticky=N)
root.mainloop()

'''
# CREATE EVENT USING ALL ABOVE

def square(event):
    a = int(num1.get())
    b = a*a
    result.delete(0,"end")
    result.insert(0,b)

root=Tk()

Label(root,text="Find the squre of a number").pack()
num1= Entry(root)
num1.pack(side=LEFT)

btn= Button(root,text="square to")
btn.bind("<Button-1>", square)
btn.pack(side=LEFT)

result= Entry(root)
result.pack(side=LEFT)
root.mainloop()