



class Student:
    def __init__ (self, id, name, dob):
        self.id = id
        self.name = name 
        self.dob = dob
        

class Course:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        

class StudentMarkManagement:
    def __init__(self):
        self.students = []
        self.courses = []
        self.marks = {}
        
    def inputStudents(self): 
        numStudents = int(input("Enter number of students: "))
        for _ in range(numStudents):
            id = input("Enter student id: ")
            name = input("Enter student name: ")
            dob = input("Enter student DOB: ")
            self.students.append(Student(id, name, dob))
        
    def inputCourses(self): 
        numCourses = int(input("Enter number of courses: "))
        for _ in range(numCourses):
            id = input("Enter course id: ")
            name = input("Enter course name: ")
            self.courses.append(Course(id, name))
        
    def inputMarks(self):
        for course in self.courses:
            print(f"Entering marks for course {course.name}")
            for student in self.students:
                mark = float(input(f"Enter mark for student {student.name}: "))
                self.marks[(student.id, course.id)] = mark
    
    def listStudents(self):
        for student in self.students:
            print(f"ID: {student.id}, Name: {student.name}, DOB: {student.dob}")
        
    def listCourses(self):
        for course in self.courses:
            print(f"ID: {course.id}, Name: {course.name}")
    
    def showMarks(self):
        for (student_id, course_id), mark in self.marks.items():
            print(f"Student {student_id} got {mark} in course {course_id}")
        
        
    
obj = StudentMarkManagement()
obj.inputStudents()
obj.inputCourses()
obj.inputMarks()
obj.listStudents()
obj.listCourses()
obj.showMarks()
