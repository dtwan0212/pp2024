import curses
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
    def __init__(self, stdscr):
        self.stdscr = stdscr
        self.students = []
        self.courses = []
        self.marks = {}

    def inputStudents(self): 
        numStudents = int(self.stdscr.getstr(0, 0, "Enter number of students: ").decode())
        for _ in range(numStudents):
            id = self.stdscr.getstr(0, 0, "Enter student id: ").decode()
            name = self.stdscr.getstr(0, 0, "Enter student name: ").decode()
            dob = self.stdscr.getstr(0, 0, "Enter student DOB: ").decode()
            self.students.append(Student(id, name, dob))

    def inputCourses(self): 
        numCourses = int(self.stdscr.getstr(0, 0, "Enter number of courses: ").decode())
        for _ in range(numCourses):
            id = self.stdscr.getstr(0, 0, "Enter course id: ").decode()
            name = self.stdscr.getstr(0, 0, "Enter course name: ").decode()
            credit = int(self.stdscr.getstr(0, 0, "Enter course credit: ").decode())
            self.courses.append(Course(id, name, credit))

    def inputMarks(self):
        for course in self.courses:
            self.stdscr.addstr(0, 0, f"Entering marks for course {course.name}")
            for student in self.students:
                mark = float(self.stdscr.getstr(0, 0, f"Enter mark for student {student.name}: ").decode())
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
            self.stdscr.addstr(i+1, 0, f"ID: {student.id}, Name: {student.name}, DOB: {student.dob}, GPA: {student.gpa}")

    def listCourses(self):
        for i, course in enumerate(self.courses):
            self.stdscr.addstr(i+1, 0, f"ID: {course.id}, Name: {course.name}")

    def showMarks(self):
        for i, ((student_id, course_id), mark) in enumerate(self.marks.items()):
            self.stdscr.addstr(i+1, 0, f"Student {student_id} got {mark} in course {course_id}")

def main(stdscr):
    obj = StudentMarkManagement(stdscr)
    obj.inputStudents()
    obj.inputCourses()
    obj.inputMarks()
    obj.calculateGPA()
    obj.listStudents()
    obj.listCourses()
    obj.showMarks()

curses.wrapper(main)
