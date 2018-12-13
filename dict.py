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


def calculate_average_mark(student):
    number_of_marks = len(student["grades"])
    sum_of_grades = sum(student["grades"])
    print(sum_of_grades/number_of_marks)
    return int(sum_of_grades/number_of_marks)

def show_details(student):
    print("{} has an average of {}".format(student["name"], calculate_average_mark(student)))

def show_all_details(students):
    for i, student in enumerate(students):
        print("id: ", i, student)
        show_details(student)


def menu():

    selection = input("""Press 'a' to add a student, 'l' to list students, 'd' to add a grade or 'q' to quit : \nType a letter: """)
    while selection != 'q':
        if selection == 'a':
            create_student()
        elif selection == 'l':
            show_all_details(students)
        elif selection == 'd':
            select = int(input('Which student ID do you want to add a grade to?'))
            grade = int(input('What grade?'))
            add_mark(students[select], grade)
        elif selection == 'q':
            break
        selection = input("""Press 'a' to add a student, 'l' to list students, 'd' to add a grade or 'q' to quit """)


menu()

