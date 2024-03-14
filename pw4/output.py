def listStudents(students):
    for i, student in enumerate(students):
        print(f"ID: {student.id}, Name: {student.name}, DOB: {student.dob}, GPA: {student.gpa}")

def listCourses(courses):
    for i, course in enumerate(courses):
        print(f"ID: {course.id}, Name: {course.name}")

def showMarks(marks):
    for i, ((student_id, course_id), mark) in enumerate(marks.items()):
        print(f"Student {student_id} got {mark} in course {course_id}")
