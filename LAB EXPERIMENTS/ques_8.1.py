import tkinter as tk 

# create new window
window = tk.Tk()

# set title of window
window.title("My First Tkinter Window")

# set fixed size of window
window.geometry("400x200")

# disable resizing
window.resizable(False,False)

# add a label inside window
label = tk.Label(window,text="Welcome to Tkinter GUI",font=("Arial",14))
label.pack(pady=50)

# run the window
window.mainloop()