from tkinter import *

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=100, pady=100)

#label
my_label = Label(text="I Am a Label", font=('Arial', 24))
my_label.config(text="New Text", padx=20, pady=20)
my_label.grid(column=0, row=0)

#button
def button_clicked():
    my_label.config(text=input.get())

button = Button(text="Click Me", command=button_clicked)
button.grid(column=1, row=1)

new_button = Button(text="New Button", command=button_clicked)
new_button.grid(column=2, row=0)

#input
input = Entry(width=10)
input.grid(column=3, row=2)


window.mainloop()