import tkinter as tk
root = tk.Tk()
root.geometry("300x300")
root.resizable(False, False)
root.title("Generator")

tk.Entry(root).grid(column=0, row=0)
tk.Button(root, text="pridat").grid(column=1, row=0)


root.mainloop()