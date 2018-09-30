import tkinter

def zlącz_napisy():
    a = a_entry.get()
    b = b_entry.get()
    print(a+b)

root = tkinter.Tk()
root.tittle("Prosty kalkulator")

a_label = tkinter.Label(master=root, text="a")
a_label.pack()
a_entry = tkinter.Entry(master=root)
a_entry.pack()
b_label = tkinter.Label(master=root, text="b")
b_label.pack()
b_entry = tkinter.Entry(master=root)

root.mainloop()