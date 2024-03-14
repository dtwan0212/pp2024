# from domains.Student import Student
# from domains.Course import Course
from domains.StudentMarkManagement import StudentMarkManagement
import input
import output
import pickle
import os

def saveData(obj):
    with open('students.dat', 'wb') as f:
        pickle.dumb(obj, f)
        
def loadData():
    if os.path.exists('students.dat'):
        with open('students.dat', 'rb') as f:
            return pickle.load((f))
    else: return None
    

def main():
    obj = StudentMarkManagement()
    numStudents, studentsInfo = input.inputStudents()
    numCourses, coursesInfo = input.inputCourses()
    marksInfo = input.inputMarks(studentsInfo, coursesInfo)
    obj.inputStudents(numStudents, studentsInfo)
    obj.inputCourses(numCourses, coursesInfo)
    obj.inputMarks(marksInfo)
    obj.calculateGPA()
    output.listStudents(obj.students)
    output.listCourses(obj.courses)
    output.showMarks(obj.marks)

main()
