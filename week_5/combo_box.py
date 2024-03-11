from tkinter import *

from tkinter.ttk import *

window = Tk()

window.title("Combo Box Example")

window.geometry('400x400')

combo = Combobox(window)

combo['values']= ("Apple", "Mango", "Lime", "Banana", "Sugarcane", "Text")

combo.current(1) #set the selected item

combo.grid(column=0, row=0)


chk_state = BooleanVar()

chk = Checkbutton(window, text='Male', var=chk_state)

chk.grid(column=100, row=100)

chk1 = Checkbutton(window, text='Female', var= False)

chk1.grid(column=200, row=100)



window.mainloop()