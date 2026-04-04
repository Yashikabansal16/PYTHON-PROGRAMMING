import tkinter as tk

# function for addition
def add():
    num1 = float(entry1.get())
    num2 = float(entry2.get())
    result_label.config(text="Result:"+str(num1 + num2))
    
# function for subtraction 
def subtract():
    num1 = float(entry1.get())
    num2 = float(entry2.get())
    result_label.config(text="Result:"+str(num1 - num2))
    
# function for multiplication
def multiply():
    num1 = float(entry1.get())
    num2 = float(entry2.get())
    result_label.config(text="Result:"+str(num1 * num2))
    
# function for division
def divide():
    num1 = float(entry1.get())
    num2 = float(entry2.get())
    if num2 == 0:
        result_label.config(text="Result:Cannot divide by zero")
    else:
        result_label.config(text="Result:"+str(num1 / num2))
        
# create main window
window = tk.Tk()
window.title("Basic Calculator")
window.geometry("350x350")
window.resizable(False,False)

# label for first number
label1 = tk.Label(window,text="Enter First number:")
label1.pack(pady = 5)

# entry for first number
entry1 = tk.Entry(window)
entry1.pack(pady=5)

# label for second number
label2 = tk.Label(window,text="Enter Second Number:")
label2.pack(pady=5)

# entry for second number
entry2 = tk.Entry(window)
entry2.pack(pady=5)

# buttons for operations
btn_add= tk.Button(window,text="Add",width=10,command=add)
btn_add.pack(pady=5)

btn_subtract = tk.Button(window,text="Sutract",width=10,command=subtract)
btn_subtract.pack(pady=5)

btn_multiply = tk.Button(window,text="Multiply",width=10,command=multiply)
btn_multiply.pack(pady=5)

btn_divide = tk.Button(window,text="Divide",width=10,command=divide)
btn_divide.pack(pady=5)

# label to display result
result_label = tk.Label(window,text="Result:",font=("Arial",12))
result_label.pack(pady=10)

# run the window
window.mainloop()
    