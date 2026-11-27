class InvalidMarksError(Exception):
    pass

try:
    marks = int(input("Enter marks: "))
    if marks < 0 or marks > 100:
        raise InvalidMarksError
    print("Pass" if marks >= 40 else "Fail")
except InvalidMarksError:
    print("Marks must be 0–100")
finally:
    print("Finished")