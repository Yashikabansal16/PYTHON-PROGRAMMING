import tkinter as tk
from tkinter import messagebox
import sqlite3

# ---------------- Database ----------------
conn = sqlite3.connect("students.db")
cursor = conn.cursor()

# FIX: recreate table properly
cursor.execute("DROP TABLE IF EXISTS students")

cursor.execute("""
CREATE TABLE students(
    name TEXT,
    roll_no TEXT,
    course TEXT,
    email TEXT,
    phone TEXT
)
""")
conn.commit()

# ---------------- GUI ----------------
root = tk.Tk()
root.title("Student Registration")

# Labels
tk.Label(root, text="Name").grid(row=0, column=0)
tk.Label(root, text="Roll No").grid(row=1, column=0)
tk.Label(root, text="Course").grid(row=2, column=0)
tk.Label(root, text="Email").grid(row=3, column=0)
tk.Label(root, text="Phone").grid(row=4, column=0)

# Entries
name_entry = tk.Entry(root)
roll_entry = tk.Entry(root)
course_entry = tk.Entry(root)
email_entry = tk.Entry(root)
phone_entry = tk.Entry(root)

name_entry.grid(row=0, column=1, padx=10, pady=5)
roll_entry.grid(row=1, column=1, padx=10, pady=5)
course_entry.grid(row=2, column=1, padx=10, pady=5)
email_entry.grid(row=3, column=1, padx=10, pady=5)
phone_entry.grid(row=4, column=1, padx=10, pady=5)

# ---------------- Function ----------------
def register_student():
    name = name_entry.get()
    roll = roll_entry.get()
    course = course_entry.get()
    email = email_entry.get()
    phone = phone_entry.get()

    if not (name and roll and course):
        messagebox.showerror("Error", "Name, Roll No, and Course are required!")
        return

    cursor.execute(
        "INSERT INTO students (name, roll_no, course, email, phone) VALUES (?, ?, ?, ?, ?)",
        (name, roll, course, email, phone)
    )
    conn.commit()

    messagebox.showinfo("Success", "Student registered successfully!")

    # Clear fields
    name_entry.delete(0, tk.END)
    roll_entry.delete(0, tk.END)
    course_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)

# ---------------- Button ----------------
tk.Button(root, text="Register", command=register_student)\
    .grid(row=5, column=0, columnspan=2, pady=10)

root.mainloop()

conn.close()