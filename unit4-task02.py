student = {
    "name": "Sasi",
    "age": 18,
    "course": "Python Programming",
    "city": "New York",
}

print("Keys:", student.keys())
print("Values:", student.values())
print("Items:", student.items())

print("Name:", student.get("name"))
print("GPA:", student.get("gpa", "Not provided"))

student.update({"age": 21, "course": "AIML"})
print("After update:", student)

removed_city = student.pop("city")
print("Popped city:", removed_city)
print("Final dictionary:", student)