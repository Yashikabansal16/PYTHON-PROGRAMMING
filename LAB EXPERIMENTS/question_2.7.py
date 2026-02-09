# take student details from user
name = input("Enter name: ")
rollno = input("Enter roll number: ")
sapid = int(input("Enter SAP ID: "))
sem = int(input("Enter Semester: "))
course = input("Enter course: ")

# take marks of 5 subjects from user
pds = int(input("\nEnter marks of PDS: "))
python = int(input("Enter marks of Python: "))
chem = int(input("Enter marks of Chemistry: "))
eng = int(input("Enter marks of English: "))
phy = int(input("Enter marks of Physics: "))

# calculating total,percentage,CGPA
total = pds + python + chem + eng + phy
percentage = total / 5
cgpa = percentage / 10

# determining grades based on cgpa
if cgpa <= 3.4:
    grade = "F"
elif cgpa <= 5.0:
    grade = "C+"
elif cgpa <= 6.0:
    grade = "B"
elif cgpa <= 7.0:
    grade = "B+"
elif cgpa <= 8.0:
    grade = "A"
elif cgpa <= 9.0:
    grade = "A+"
else:
    grade = "O (Outstanding)"

# print result
print("\t----GRADE SHEET----")
print("Name: ",name)
print("Roll Number: ",rollno,"\tSAP ID: ",sapid)
print("Semester: ",sem,"\t\tCourse: ",course)
print("\nSubject name\tMarks")
print("PDS\t\t",pds)
print("Python\t\t",python)
print("Chemistry\t",chem)
print("English\t\t",eng)
print("Physics\t\t",phy)

print("\nPercentage: ",percentage)
print(f"CGPA: {cgpa:.2f}")
print("Grades: ",grade)



