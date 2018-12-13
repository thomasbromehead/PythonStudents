students = []

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
    students.append(student_details)
    return student_details

def add_mark(student, mark):
    student["grades"].append(mark)

s = create_student()



def calculate_average_mark(student):
    number_of_marks = len(student["grades"])
    sum_of_grades = sum(student["grades"])
    print(int(sum_of_grades / number_of_marks))
    return int(sum_of_grades / number_of_marks)

def show_details(student):
    print("{} has an average of".format(student["name"], calculate_average_mark(student)))

def show_all_details(students):
    for student in students:
        show_details(student)
        calculate_average_mark(student)



print(students)
show_all_details(students)
