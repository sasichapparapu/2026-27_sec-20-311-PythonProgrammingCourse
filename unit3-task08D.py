def student_details(**marks):
    for subject, mark in marks.items():
        print(subject, ":", mark)


student_details(name="Krishna", Maths=90, Science=85, English=88)