students = [
    {"name": "Alex", "marks": 85},
    {"name": "Sam", "marks": 92},
    {"name": "Jordan", "marks": 78},
]

ascending = sorted(students, key=lambda student: student["marks"])
descending = sorted(students, key=lambda student: student["marks"], reverse=True)

print("Ascending:")
for student in ascending:
    print(student)

print("Descending:")
for student in descending:
    print(student)