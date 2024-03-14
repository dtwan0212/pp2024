def inputStudents():
    numStudents = int(input("Enter number of students: "))
    studentsInfo = []
    for _ in range(numStudents):
        id = input("Enter student id: ")
        name = input("Enter student name: ")
        dob = input("Enter student DOB: ")
        studentsInfo.append((id, name, dob))
    return numStudents, studentsInfo

def inputCourses():
    numCourses = int(input("Enter number of courses: "))
    coursesInfo = []
    for _ in range(numCourses):
        id = input("Enter course id: ")
        name = input("Enter course name: ")
        credit = int(input("Enter course credit: "))
        coursesInfo.append((id, name, credit))
    return numCourses, coursesInfo

def inputMarks(students, courses):
    marksInfo = {}
    for course in courses:
        for student in students:
            mark = float(input(f"Enter mark for student {student[1]} in course {course[1]}: "))
            marksInfo[(student[0], course[0])] = mark
    return marksInfo
