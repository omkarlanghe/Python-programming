'''
# WAP to implement student management system. we should implement a class student:
class student
{

name
address
dob
course
division
list<marks>

};

Implement getter and setter methods for it. all should be set as private attributes. class should contain following methods mention below:

AddStudent()
SuspendStudent()
UpdateAddress()
UpdateMarks()
Print all student details and their percentage.

also write menu driven program containing..

# WAP to implement employee management system;
AddEmployee()
KickEmployee()
ApprailEmployee()
'''
class Student:
    auto_roll_no = 1

    def __init__(self, name, address, dob, course, division):
        self.__roll_no = Student.auto_roll_no
        Student.auto_roll_no += 1
        self.__name = name
        self.__address = address
        self.__dob = dob
        self.__course = course
        self.__division = division
        self.__marks = dict()
    
    #getter methods
    def getName(self):
        return self.__name
    
    def getAddress(self):
        return self.__address
    
    def getdob(self):
        return self.__dob

    def getCourse(self):
        return self.__course

    def getDivision(self):
        return self.__division

    def getRollNo(self):
        return self.__roll_no

    def getMarks(self):
        return self.__marks

    #setter methods
    def updateAddress(self, address):
        self.__address = address
    
    def updateMarks(self, subject, marks):
        self.__marks[subject] = marks
    
    def updateCourse(self, course):
        self.__course = course

    def updateDivision(self, division):
        self.__division = division
    
    def __repr__(self): #used to convert object to string
        return "Name:"+self.__name+"\nAddress:"+self.__address+"\nDOB:"+self.__dob+"\nRollNo:"+str(self.__roll_no)

def unitTest():
    student = Student("Omkar", "Pune", "26-03-96", "BE", "B")
    print("Name :"+student.getName())
    print("Address :"+student.getAddress())
    print("DOB :"+student.getdob())
    print("Course :"+student.getCourse())
    print("Division :"+student.getDivision())
    
    student.updateAddress("Redmond")
    print("updated address :"+student.getAddress())
    student.updateMarks("Principles of programming language", 90)
    print("updated marks :", student.getMarks())
    student.updateMarks("Python programming", 80)
    print("updated marks :", student.getMarks())

class StudentManager:
    def __init__(self, no_of_students):
        self.__no_of_students = no_of_students
        self.__enrolled_students = dict()
        self.__suspend_students = dict()
    
    def AddStudents(self, name, address, dob, course, division):
        st = Student(name, address, dob, course, division)
        self.__enrolled_students[st.getRollNo()] = st

    def SuspendStudent(self, rollNo):
        if rollNo in self.__suspend_students:
            pass
        elif rollNo in self.__enrolled_students:
            st = self.__enrolled_students.pop(rollNo)
            self.__suspend_student[rollNo] = st
        else:
            return False
        return True

    def getEnrolledStudents(self):
        return self.__enrolled_students

    def getSuspendedStudents(self):
        return self.__suspend_students

    def updateMarks(self, rollNo, subject, marks):
        if rollNo in self.__enrolled_students:
            self.__enrolled_students[rollNo].updateMarks(subject, marks)
            return True
        return False
    
    def getMarks(self, rollNo):
        return self.__enrolled_students[rollNo].getMarks()

    def updateAddress(self, rollNo, address):
        if rollNo in self.__enrolled_students[rollNo].updateAddress(address):
            return True
        return False

    def getAddress(self, rollNo):
        return self.__enrolled_students[rollNo].getAddress()

    def updateCourse(self, rollNo, course):
        if rollNo in self.__enrolled_students:
            self.__enrolled_students[rollNo].updateCourse(course)
            return True
        return False

    def getCourse(self, rollNo):
        return self.__enrolled_students[rollNo].getCourse()

    def updateDivision(self, rollNo, division):
        if rollNo in self.__enrolled_students:
            self.__enrolled_students[rollNo].updateDivision(division)
            return True
        return False
    
    def getDivision(self, rollNo):
        return self.__enrolled_students[rollNo].getDivision()

class unitTestStudentManager():
    sm = StudentManager(50)

    sm.AddStudents("amit mhaske","pune", "17-02-95", "BE", "A")
    sm.AddStudents("avc","pune", "17-04-95", "BE", "A")
    sm.AddStudents("jksdng","pugdsne", "17-02-95", "BE", "A")

    print("######### Displaying Enrolled students ###########")
    students = sm.getEnrolledStudents()
    for st in students:
        print(students[st])
    #sm.SuspendStudent(1)

    print("*************Displaying Enrolled students ***************\n")
    students = sm.getEnrolledStudents()
    for st in students:
        print(students[st])

    print("*************Displaying suspended students***************\n");
    students = sm.getSuspendedStudents()
    for st in students:
        print(students[st])
    print(sm.getMarks(2))
    sm.updateMarks(1, "Science", 45)
    print(sm.getMarks(2))
    print(sm.getCourse(2))
    sm.updateCourse(2, "Science")
    print(sm.getCourse(2))

def Menu():
    choice = eval(input("Enter your choice:\n"))
    return choice

def StudentDetailMenu():
    choice = eval(input("Enter your choice to update student details:\n"))
    return choice

class StudentManagementSystem():
    n = eval(input("Enter number of students:\n"))
    sm = StudentManager(n)

    print("******** welcome to student management system ***********\n")
    print("1.Enroll Student\n2. Suspend Student\n3. Print All Student\n4. Print Enrolled Students with Percentage\n5.Print Suspended students\n6. Update Student details\n7. Exit\n")

    while True:
        ch = Menu()
        #if-elif choice
        if ch == 1:
            print("Enroll Student\n");
            name = input("Enter name of the student\n")
            address = input("Enter addess of the student\n")
            dob = input("Enter birth date of the student\n")
            course = input("Enter the course of the student:\n")
            div = input("Enter student division:\n")

            sm.AddStudents(name, address, dob, course, div)
        
        elif ch == 2:
            print("Suspend Student\n");
        
        elif ch == 3:
            print("displaying details of all students present in this system:\n")
            students = sm.getEnrolledStudents()
            for st in students:
                print(students[st])

        elif ch == 4:
            print("Print enrolled students with percentage\n")
        elif ch == 5:
            print("Print Suspended students\n")
        elif ch == 6:
            print("Update student details\n")
            choice = StudentDetailMenu()
            
            if choice == 1:
                rollNo = input("Enter roll nummber of the student:\n")
                address = input("Enter Address to update:\n")
                sm.updateAddress(rollNo, address)
                print("Address successfully updated\n")

            elif choice == 2:
                rollNo = input("Enter roll number of the student:\n")
                division = input("Enter the division to be updated:\n")
                sm.updateDivision(rollNo, division)
                print("Division successfully updated\n")

            elif choice == 3:
                rollNo = input("Enter roll number of the student:\n")
                course = input("Enter the course to update:\n")
                sm.updateCourse(rollNo, course)
                print("Course successfully updated\n")

            elif choice == 4:
                rollNo = input("Enter roll number of the student:\n")
                subject = input("Enter Subject:\n")
                marks = input("Enter marks to update:\n")
                sm.updateMarks(rollNo, subject, marks)
                print("Marks successfully updated\n")

        elif ch == 7:
            print("Exiting from system..!")

def main():
    StudentManagementSystem()
if __name__ == '__main__':
    main()

