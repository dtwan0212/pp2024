import numpy

class Student:
    def __init__ (self, id, name, dob):
        self.id = id
        self.name = name 
        self.dob = dob
        self.gpa = 0

class Course:
    def __init__(self, id, name, credit):
        self.id = id
        self.name = name
        self.credit = credit

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
            credit = int(input("Enter course credit: "))
            self.courses.append(Course(id, name, credit))

    def inputMarks(self):
        for course in self.courses:
            print(f"Entering marks for course {course.name}")
            for student in self.students:
                mark = float(input(f"Enter mark for student {student.name}: "))
                self.marks[(student.id, course.id)] = numpy.floor(mark * 10) / 10

    def calculateGPA(self):
        for student in self.students:
            marks = []
            credits = []
            for course in self.courses:
                mark = self.marks.get((student.id, course.id))
                if mark is not None:
                    marks.append(mark)
                    credits.append(course.credit)
            marksArray = numpy.array(marks)
            creditsArray = numpy.array(credits)
            student.gpa = numpy.average(marksArray, weights=creditsArray)

    def listStudents(self):
        gpas = numpy.array([student.gpa for student in self.students])
        sorted_indices = numpy.argsort(gpas)[::-1]
        for i in sorted_indices:
            student = self.students[i]
            print(f"ID: {student.id}, Name: {student.name}, DOB: {student.dob}, GPA: {student.gpa}")

    def listCourses(self):
        for i, course in enumerate(self.courses):
            print(f"ID: {course.id}, Name: {course.name}")

    def showMarks(self):
        for i, ((student_id, course_id), mark) in enumerate(self.marks.items()):
            print(f"Student {student_id} got {mark} in course {course_id}")

def main():
    obj = StudentMarkManagement()
    obj.inputStudents()
    obj.inputCourses()
    obj.inputMarks()
    obj.calculateGPA()
    obj.listStudents()
    obj.listCourses()
    obj.showMarks()

main()
