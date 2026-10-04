students = {
    "Ana": 85,
    "Ben": 90,
    "Carlo": 78,
    "Diana": 95
}
print("STUDENT GRADES")
print("==============")
print("Ana:", students["Ana"])
print("Ben:", students["Ben"])
students["Ella"] = 88
students["Carlo"] = 82
students["Diana"] = 91
name1 = input("Enter student name: ")
grade1 = int(input("Enter student grade: "))
students[name1] = grade1
print(students)
print("\nUpated Student Grades")
print("=====================")

for name,grade in students.items():
    print(name, ":", grade)
search = input("\nEnter student name to search: ")
if search in students:
    print(search, "has a grade of", students[search])
else:
    print("Student not found.")

print()
lowest_student = min(students, key=students.get)
lowest_grade = students[lowest_student]
print(lowest_student)
highest_student = max(students, key=students.get)
highest_grade = max[highest_student]
print(highest_student)
difference = (highest_grade - lowest_grade)
print(difference)
average = sum(students.values()).len(students)
print(average)