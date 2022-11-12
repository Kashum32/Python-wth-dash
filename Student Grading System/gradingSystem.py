'''
Create a student grading system using Python that has the following functionalities:
1. Entering the Grades of a student
2. Removing a student from the system
3. Calculating the average grades of students
The user should be able to select whether he/she wants to remove a student, enter grades for a
student or find the average grades.
Also, perform the following as part of this project:

There should be a log-in system to allow only admin access to the grading system.
Make sure you use dictionaries and lists for storing student’s data.
Use Python functions as much as you can

'''
from statistics import mean as m

addmin = {'Python':'Pass123@','user2':'pass2'}

studentDict = {'jeff':[78,88,93],
                'Alex':[92,76,88],
                'Sam':[89,92,93]          
              }

# get the student name and grades
def enterGrades(): 
    nameToEnter = input("Student Name : ")
    gradeToEnter = input("Grade : ")

    if nameToEnter in studentDict :
        print("Adding Grade.....")
        studentDict[nameToEnter].append(float(gradeToEnter))
    
    else:
        print('Student does not exit')
    print(studentDict)

# remove the student
def removeStudent() :
    nameToRemove = input("What student to remove : ")
    if nameToRemove in studentDict:
        print("removing student.....")
        del studentDict[nameToRemove]

    print(studentDict)

def studentAVGs():
    for eachStudent in studentDict :
        gradeList = studentDict[eachStudent]
        avgGrade = m(gradeList)

        print(eachStudent,'has an average grade of : ',avgGrade)
'''
# Grade of student to remove
def removeGrade():
    removeName = input("Student Name : ")
    removeGrade = input("Grade : ")

    if removeGrade in studentDict:
        if studentDict[removeGrade] == removeGrade:
            print("removing grade.....")
            del studentDict[removeGrade]
    print(studentDict)
'''         

def main():
    print('''
    
    Welcome to Grade Centeral

    [1] - Enter Grades
    [2] - Remove Student
    [3] - Student Average Grades
    [4] - Exit
  
    ''')
    action = input("What would you like to do today? (Enter a number)")

    if(action == '1'):
        enterGrades()
    elif(action == '2'):
        removeStudent()
    elif(action == '3'):
        studentAVGs()
    else:
        print('No valid choiuce was given, try again')

login = input('Enter Username of Student : ')
password = input("Enter Password of Student : ")

if login in addmin :
    if addmin[login] == password :
        print('welcome, ',login)
        while True :
            main()
    else :
        print('Invalid password, will detonate in 5 second!')
else :
    print('Invalid username, calling the FBI to report this ')

