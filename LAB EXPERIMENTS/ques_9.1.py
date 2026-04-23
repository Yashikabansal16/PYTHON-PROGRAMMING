class Student:
    def __init__(self,name,sap_id,marks):
        self.name = name
        self.sap_id = sap_id
        self.marks = marks
        
    def display(self):
        print("\nSTUDENT DETAILS:")
        print("Name: ",self.name)
        print("SAP ID: ",self.sap_id)
        print("Physics: ",self.marks[0])
        print("Chemistry: ",self.marks[1])
        print("Maths: ",self.marks[2])
        
students = []

for i in range(3):
    print(f"\nEnter details for students{i+1}: ")
    name = input("Enter Student name: ")
    sap_id = int(input("Enter SAP ID: "))
    
    print("Enter marks(Physics,Chemistry,Maths):")
    phy = float(input("Physics:"))
    chem = float(input("Chemistry:"))
    maths = float(input("Maths:"))
    
    marks = [phy,chem,maths]
    
    s = Student(name, sap_id, marks)
    students.append(s)

for s in students:
    s.display()


        