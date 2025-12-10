import tkinter as tk
root = tk.Tk()
root.geometry("300x300")
root.resizable(False, False)
root.title("Generator")
tk.Label(root, text="Generátor Vánočních přání").grid(row=0, column=0)
tk.Entry(root).grid(column=0, row=1)
tk.Button(root, text="Přidat").grid(column=1, row=1)
root.mainloop()