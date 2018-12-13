def create_student():
    name = input('Enter your student\'s name: ')
    marks = input("Enter student's grades as a comma separated list of values: ")
    marks_array = marks.split(',')
    if marks_array == ['']:
        marks_array = []
    student_details = {
        "name":name,
        "grades": [int(grade) for grade in marks_array]
    }
    print(student_details["grades"])
    return student_details

def add_mark(student, mark):
    student["grades"].append(mark)

s = create_student()


def calculate_average_mark(student):
    number_of_marks = len(student["grades"])
    sum_of_grades = sum(student["grades"])
    try:
        print(number_of_marks, sum_of_grades)
        return sum_of_grades / number_of_marks
    except ZeroDivisionError:
        print('No grades yet')



print(calculate_average_mark(s))