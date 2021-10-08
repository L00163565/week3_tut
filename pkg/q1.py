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
    STUDENT_NUMBER = 'student_number'
    GRADE = 'grade'
    students_enrolled = (student_1, student_2)
    modules = [module_1, module_2]
    grades_module_1 = [{STUDENT_NUMBER: student_1, GRADE: 40}, {STUDENT_NUMBER: student_2, GRADE: 70}]
    grades_module_2 = [{STUDENT_NUMBER: student_1, GRADE: 69.01}, {STUDENT_NUMBER: student_2, GRADE: 58.2}]
    INPUT_MODULE = input("Enter the Module name you want the grade of, (Java_ooprogramming or Python_Scripting)?: ")
    if INPUT_MODULE == modules[0]:
        for i in grades_module_1:
            print('Student id:' + i[STUDENT_NUMBER] + '\nGrade: ' + str(i[GRADE]))
    elif INPUT_MODULE == modules[1]:
        for i in grades_module_2:
            print('Student id:' + i[STUDENT_NUMBER] + '\nGrade: ' + str(i[GRADE]))