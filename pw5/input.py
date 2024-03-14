

def inputStudents():
    numStudents = int(input("Enter number of students: "))
    studentsInfo = []
    for _ in range(numStudents):
        id = input("Enter student id: ")
        name = input("Enter student name: ")
        dob = input("Enter student DOB: ")
        studentsInfo.append((id, name, dob))
    with open('students.txt', 'w') as f:
        for student in studentsInfo:
            f.write(f"{student[0]}, {student[1]}, {student[2]}\n")
    return numStudents, studentsInfo
    

def inputCourses():
    numCourses = int(input("Enter number of courses: "))
    coursesInfo = []
    for _ in range(numCourses):
        id = input("Enter course id: ")
        name = input("Enter course name: ")
        credit = int(input("Enter course credit: "))
        coursesInfo.append((id, name, credit))
    with open('courses.txt', 'w') as f:
        for course in coursesInfo:
            f.write(f"{course[0]}, {course[1]}, {course[2]}\n")
    return numCourses, coursesInfo

def inputMarks(students, courses):
    marksInfo = {}
    for course in courses:
        for student in students:
            mark = float(input(f"Enter mark for student {student[1]} in course {course[1]}: "))
            marksInfo[(student[0], course[0])] = mark
        with open('marks.txt', 'w') as f:
            for key, value in marksInfo.items():
                f.write(f"Student {key[0]} got {value} in course {key[1]}\n")
    return marksInfo

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
