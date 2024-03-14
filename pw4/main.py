# from domains.Student import Student
# from domains.Course import Course
from domains.StudentMarkManagement import StudentMarkManagement
import input
import output

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
