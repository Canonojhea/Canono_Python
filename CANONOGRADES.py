Canononame = input("Enter student's name: ")

Canonomath = float(input("Enter Math grade: "))
Canonoscience = float(input("Enter Science grade: "))
Canonoenglish = float(input("Enter English grade: "))

Canonototal = Canonomath + Canonoscience + Canonoenglish
Canonoaverage = Canonototal / 3

print()
print("STUDENT GRADE REPORT")
print("Student Name:", Canononame)
print()
print("Math Grade:", Canonomath)
print("Science Grade:", Canonoscience)
print("English Grade:", Canonoenglish)
print()
print("Total Grade:", Canonototal)
print("Average Grade:", Canonoaverage)