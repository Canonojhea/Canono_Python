print(f"{'STUDENT PROGRAM FILES'}")

students = [("Jonah Perez", "BSCS", 1),
            ("Alex Santos", "BSMT", 1),
            ("Micah Mendoza", "BSCS", 1),
            ("Allen Torres", "BSMT", 1),
            ("Datrell Quistadio", "BSCS", 3),
            ("Dean BustaMisa", "BSMT", 3),
            ("Kristana Sarabia", "BSCS", 4),
            ("Cat Dela Cruz", "BSMT", 4)]

print("Student Information")
for student in students:
    print("Name: ", student[0])
    print("Program: ", student[1])
    print("Year Level: ", student[2])
    print()

program = input("Search program: ")
print("Students in ", program.upper(), " program: ")

found = False
for student in students:
     if program == student[1].lower():
         print("Name: ", student[0])
         print("Program: ", student[1])
         print("Year Level: ", student[2])
         print()
         found = True

if not found:
    print("No students.")