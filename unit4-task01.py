student = {
    "name": input("Enter student name: "),
    "age": int(input("Enter student age: ")),
    "course": input("Enter course: "),
}

student["age"] = int(input("Enter updated age: "))
student["city"] = input("Enter city: ")

print(student)