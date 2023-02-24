from main import Student

mystudent = Student.select()
for Student in mystudent:
    print(Student.student_name, Student.student_ID, Student.student_class)
