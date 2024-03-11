from tkinter import *

window = Tk()

window.title("Sensors")

window.geometry('400x400')

temp = 68
lbl = Label(window, text="Temperature: {}".format(temp))
lbl.grid(column=0, row=0)

def clicked():
    global temp
    temp += 1
    lbl.configure(text="Temperature: {}".format(temp))

btn = Button(window, text="Increase Temperature", command=clicked)
btn.grid(column=200, row=200)

window.mainloop()
