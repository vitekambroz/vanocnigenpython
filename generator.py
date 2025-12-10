import tkinter as tk
import random
root = tk.Tk()
root.geometry("1000x500")
root.resizable(False, False)
root.title("Generator")

tk.Label(root, text="Generátor Vánočních přání").grid(row=0, column=0)

a = tk.Entry(root)
a.grid(column=0, row=1)

def tlacitko():
    b= a.get()
    listbox.insert(tk.END, b)

def vybrat():
    size = listbox.size()
    if size == 0:
        label_vyber.config(text="(List je prázdný)")
        return
    index = random.randint(0, size - 1)
    text = listbox.get(index)
    label_vyber.config(text=text)

tk.Button(root, text="Přidat", command=tlacitko).grid(column=1, row=1)
tk.Button(root, text="Vybrat", command=vybrat).grid(column=1, row=2)

listbox = tk.Listbox(root, selectmode=tk.SINGLE)
listbox.grid(row=2, column=0, padx=5, pady=5)

label_vyber = tk.Label(root, text="")
label_vyber.grid(column=2, row=2)

root.mainloop()