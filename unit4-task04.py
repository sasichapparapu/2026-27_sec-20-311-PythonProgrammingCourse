students = {
    "S001": {"name": "Alex", "marks": 85},
    "S002": {"name": "Sam", "marks": 92},
    "S003": {"name": "Jordan", "marks": 78},
}

for student in students.values():
    print(f"Name: {student['name']}, Marks: {student['marks']}")