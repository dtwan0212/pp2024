students = []
courses = []
marks = {}

def inputNumberOfStudent(): 
    numStudents = int(input("Enter number of student: "))
    student = []
    for _ in range(numStudents): 
        student = {}
        student['id'] = input("Enter student id: ")
        student['name'] = input("Enter student name: ")
        student['dob'] = input("Enter student dob (dd/mm/yyyy): ")
        students.append(student)

def inputNumberOfCourses(): 
    numCourses = int(input("Enter number of courses: "))
    for course in range(numCourses):
        course = {}
        course['id'] = input("Enter course id: ")
        course['name'] = input('Enter course name: ')
        courses.append(course)

def inputMarks():
    
    for course in courses: 
        print(f"Enter mark for course{course['name']}")
    for student in students:
        mark = float(input(f"Enter mark for student {student['name']}: "))
        marks[student['id'], course['id']] = mark
        

def listCourses(): 
    print("Courses: ")
    for course in courses: 
        print(f": ID: {course['id']}, Name: {course['name']}")
        
def listStudents(): 
    print('Student: ')
    for student in students: 
        print(f": ID: {student['id']}, Name: {student['name']}, DOB: {student['dob']}")
        
def showStudentMarks(): 
    for course in courses:
        print(f"Showing marks for course {course['name']}")
        for student in students: 
            if((student['id'], course['id']) in marks):
                print(f"Mark for student {student['name']}: {marks[(student['id'], course['id'])]}")



inputNumberOfStudent()
inputNumberOfCourses()
inputMarks()
listCourses()
listStudents()
showStudentMarks()


