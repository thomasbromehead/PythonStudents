def add_marks():
    name = input('Enter your student\'s name: ')
    marks = input("Enter student's grades as a comma separated list of values: ")
    marks_array = marks.split(',')
    student_details = {
        "name":name,
        "grades": [int(grade) for grade in marks_array]
    }

    return student_details

print(add_marks())