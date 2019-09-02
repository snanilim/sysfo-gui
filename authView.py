from tkinter import *
from tkinter import messagebox

window = Tk()
window.title('Hello World')

header = Label(window, text="Login", font=("Arial Bold", 20))
header.grid(column=1, row=0)

userIDText = Label(window, text="User ID:", padx=10, pady=10)
userIDText.grid(column=0, row=1)

userIDInput = Entry(window, width=40)
userIDInput.grid(column=1, row=1)

passwordText = Label(window, text="Password:", padx=10, pady=10)
passwordText.grid(column=0, row=2)

passwordInput = Entry(window, width=40)
passwordInput.grid(column=1, row=2)

def clicked():
    resUserID = userIDInput.get()
    resPassword = passwordInput.get()
    messagebox.showerror('Error', 'Invalid Userd ID or Password')
    print('resUserID', resUserID)

btn = Button(window, text="Submit" , bg="#31a7d2", fg="white", command=clicked)
btn.grid(column=1, row=3)



window.geometry('500x350')

window.mainloop()

