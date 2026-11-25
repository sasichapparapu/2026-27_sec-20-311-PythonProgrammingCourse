subject_marks = {
    "Math": 90,
    "Science": 85,
    "English": 88,
}

print("Keys:")
for subject in subject_marks:
    print(subject)

print("Values:")
for marks in subject_marks.values():
    print(marks)

print("Items:")
for subject, marks in subject_marks.items():
    print(subject, marks)