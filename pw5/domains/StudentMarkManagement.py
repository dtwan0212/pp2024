import numpy
from .Student import Student
from .Course import Course

class StudentMarkManagement:
    def __init__(self):
        self.students = []
        self.courses = []
        self.marks = {}

    def inputStudents(self, numStudents, studentsInfo): 
        for _ in range(numStudents):
            id, name, dob = studentsInfo[_]
            self.students.append(Student(id, name, dob))

    def inputCourses(self, numCourses, coursesInfo): 
        for _ in range(numCourses):
            id, name, credit = coursesInfo[_]
            self.courses.append(Course(id, name, credit))

    def inputMarks(self, marksInfo):
        for course in self.courses:
            for student in self.students:
                mark = marksInfo[(student.id, course.id)]
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
