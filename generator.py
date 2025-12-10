import tkinter as tk
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

tk.Button(root, text="Přidat", command=tlacitko).grid(column=1, row=1)

listbox = tk.Listbox(root, selectmode=tk.SINGLE)
listbox.grid(row=2, column=0, padx=5, pady=5),

root.mainloop()