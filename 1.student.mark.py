students = []
courses = []
marks = []

def inputNumberOfStudent(): 
    numStudents = int(input("Enter number of student: "))
    
    for _ in range(numStudents): 
        studentInfo = {}
        studentInfo['id'] = input("Enter student id: ")
        studentInfo['name'] = input("Enter student name: ")
        studentInfo['dob'] = input("Enter student dob (dd/mm/yyyy): ")
        students.append(studentInfo)

def inputNumberOfCourses(): 
    numCourses = int(input("Enter number of courses: "))
    for _ in range(numCourses):
        courseInfo = {}
        courseInfo['id'] = input("Enter course id: ")
        courseInfo['name'] = input('Enter course name: ')
        courses.append(courseInfo)

def inputMarks():
    
    for courseInfo in courses: 
        print(f"Enter mark for course{courseInfo['name']}")
    for studentInfo in students:
        mark = float(input(f"Enter mark for student {studentInfo['name']}: "))
        marks[studentInfo['id'], courseInfo['id']] = mark
        

def listCourses(): 
    print("Courses: ")
    for courseInfo in courses: 
        print(f": ID: {courseInfo['id']}, Name: {courseInfo['name']}")
        
def listStudents(): 
    print('Student: ')
    for studentInfo in students: 
        print(f": ID: {studentInfo['id']}, Name: {studentInfo['name']}, DOB: {student['dob']}")
        
def showStudentMarks(): 
    for courseInfo in courses:
        print(f"Showing marks for course {courseInfo['name']}")
        for studentInfo in students: 
            if((studentInfo['id'], courseInfo['id']) in marks):
                print(f"Mark for student {studentInfo['name']}: {marks[(studentInfo['id'], courseInfo['id'])]}")



inputNumberOfStudent()
inputNumberOfCourses()
inputMarks()
listCourses()
listStudents()
showStudentMarks()


