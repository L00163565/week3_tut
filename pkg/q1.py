"""
# File : q1.py
# Created : 08-10-2021 15:07
# Author : Snehal Shirsath
# Python Version : 3.9.7
# File Version : v1.0.0
# Description :
"""

if __name__ == "__main__":
    module_1 = "Java_ooprogramming"
    module_2 = "Python_Scripting"
    student_1 = "L12345"
    student_2 = "L54321"
    Student_Number = 'L number'
    Grade = ""
    modules = [module_1, module_2]
    # list of grades and module
    grades_module_1 = [{Student_Number: student_1, Grade: 40}, {Student_Number: student_2, Grade: 70}]
    grades_module_2 = [{Student_Number: student_1, Grade: 69.01}, {Student_Number: student_2, Grade: 58.2}]

    #check the student number and then grades
    Module = input("Enter the Module name you want the grade of, (Java_ooprogramming or Python_Scripting)?: ")
    if Module == modules[0]:
        for i in grades_module_1:
            print("Gardes of Student id:" + i[Student_Number] + "are : " + str(i[Grade]))
    elif Module == modules[1]:
        for i in grades_module_2:
            print("Grades of Student id:" + i[Student_Number] + "are: " + str(i[Grade]))
