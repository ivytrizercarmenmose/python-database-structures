from main import Student

try:
    Student_name = input("enter your name \n")
    Student_ID = input("enter your ID \n")
    Student_class = input("enter your class \n")

    Student.create(student_name=Student_name, student_ID=Student_ID, student_class=Student_class)
    print("Student enrolled successfully")

except:
    print("failed to enroll student , check ID")
