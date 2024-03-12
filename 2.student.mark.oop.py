
        
class Student:
    def __init__ (self, id, name, dob):
        self.id = id
        self.name = name 
        self.dob = dob
        

class Course:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        

class Mark:
    def __init__(self, student, course, mark):
        self.student = student
        self.course = course
        self.mark = mark
        

class StudentMarkManagement:
    def __init__(self):
        self.students = []
        self.courses = []
        self.marks = {}
        
        
    
    def inputStudents(self): 
        studentInfo = {}
        studentInfo['id'] = input("Enter student id: ")
        studentInfo['name'] = input("Enter student name: ")
        studentInfo['dob'] = input("Enter student DOB: ")
        self.students.append(Student(studentInfo))
        
    def inputCourses(self): 
        courseInfo = {}
        courseInfo['id'] = input("Enter course id: ")
        courseInfo['name'] = input("Enter course name: ")
        self.courses.append(Course(courseInfo))
        
    def inputMarks(self):
        for courseInfo in self.courses:
             print(f"Entering marks for course {courseInfo.id}")
        for studentInfo in self.students:
                mark = float(input(f"Enter mark for student {studentInfo['id']}: "))
                self.marks[studentInfo['id'], courseInfo['id']] = mark
    
    def listStudents(self):
        for studentInfo in self.students:
            print(f"ID: {studentInfo['id']}, Name: {studentInfo['name']}, DOB: {studentInfo['dob']}")
        
    def listCourses(self):
        for courseInfo in self.courses:
            print(f"ID: {courseInfo['id']}, Name: {courseInfo['name']}")
    
    def showMarks(self):
        for (studentInfo, courseInfo), mark in self.marks.items():
            print(f"Student {studentInfo['name']} got {mark} in course {courseInfo['name']}")
        
        
    
obj = StudentMarkManagement()
obj.inputStudents
obj.inputCourses()
obj.inputMarks()
obj.listStudents()
obj.listCourses()
obj.showMarks()
