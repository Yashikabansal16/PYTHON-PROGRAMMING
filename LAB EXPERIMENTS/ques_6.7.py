'''7.Write functions to explain mentioned concepts:
a.	Keyword argument
b.	Default argument
c.	Variable length argument'''

def student(name, age):
    print("Name:", name)
    print("Age:", age)

# calling using keyword arguments
student(age=20, name="Riya")

def greet(name="Guest"):
    print("Hello", name)

greet("Aman")   # user value
greet()         # default value

def add(*numbers):
    total = 0
    for n in numbers:
        total += n
    print("Sum =", total)

add(10,20)
add(5,10,15,20)

