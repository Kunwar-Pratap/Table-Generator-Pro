from tkinter import *

def func_table():
    num = int(entry.get())
    strg = " Table of " + str(num) + "\n-----------------\n"
    for i in range(1, 11):
        strg =strg + " " +  str(num) + " x " + str(i) + " = " + str(num * i) + "\n"

    output_table.configure(text=strg, justify=LEFT, relief=RIDGE, bg="pink", pady=0, padx=0)

root = Tk()
root.geometry("688x733")
root.maxsize(788, 833)
root.title("Table Generator Pro - V1")
root.wm_iconbitmap("table.ico")

f = Label(root, text="Table Generator Pro", font="ubuntu 40 bold", relief=SUNKEN, bg="dark blue", fg="white")
f.pack(pady=40, fill=BOTH)
entry = Entry(root, font="lucida 20 bold", justify=CENTER)
entry.pack()
button = Button(root, text="Generate Table", font="lucida 15 bold", command=func_table, bg="indian red", fg="white")
button.pack(pady=20)
output_table = Label(root, font="lucida 22 bold")
output_table.pack()
statusvar = StringVar()
statusvar.set("Developed by- Kunwar Pratap")
sbar = Label(root, textvariable=statusvar, relief=SUNKEN, font="lucida 11 bold", bg="sky blue", padx=10)
sbar.pack(side=BOTTOM, fill=X)

root.mainloop()
