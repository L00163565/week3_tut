"""
# File : q2.py
# Created : 08-10-2021 15:49
# Author : Snehal Shirsath
# Python Version : 3.9.7
# File Version : v1.0.0
# Description :
"""
import random
if __name__ == "__main__":
    Week_1 = ["Joe", "John", "Jane", "Mick", "Mary", "Ann", "Rick", "John", "Aine", "Brenda"]
    Week_2 = ["Jack", "Mary", "Phil", "John", "Pat", "Joe", "Luke", "Bill", "Ben", "Nathan"]
    list_of_numbers = input("insert random numbers from 1 to 20:")
    list_of_numbers_1 = [random.randrange(1, 10) for i in range(0, 10)]
    print(list_of_numbers)