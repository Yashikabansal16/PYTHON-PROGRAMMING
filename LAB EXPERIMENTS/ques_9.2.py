class Student:
    def __init__(self, name, sap_id, marks):
        self.name = name
        self.sap_id = sap_id
        self.marks = marks 

    
    def display(self):
        print("\nSTUDENT DETAILS:")
        print("Name:", self.name)
        print("SAP ID:", self.sap_id)
        print("Physics:", self.marks[0])
        print("Chemistry:", self.marks[1])
        print("Maths:", self.marks[2])

    def marks_percentage(self):
        total = sum(self.marks)
        percentage = total / 3
        return percentage

    def result(self):
        if all(m > 40 for m in self.marks):
            return "Pass"
        else:
            return "Fail"

def class_average(students):
    total = 0
    for s in students:
        total += s.marks_percentage()
    return total / len(students)

n = int(input("Enter number of students: "))
students = []

for i in range(n):
    print(f"\nEnter details for Student {i+1}:")
    name = input("Enter Name: ")
    sap_id = int(input("Enter SAP ID: "))
    
    print("Enter marks (Physics, Chemistry, Maths):")
    phy = float(input("Physics: "))
    chem = float(input("Chemistry: "))
    maths = float(input("Maths: "))
    
    marks = [phy, chem, maths]
    
    s = Student(name, sap_id, marks)
    students.append(s)

# Display all details
for s in students:
    s.display()
    print("Percentage:", s.marks_percentage())
    print("Result:", s.result())

# Class average
print("\nClass Average Percentage:", class_average(students))