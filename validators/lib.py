
"""
    Валідація квитка студента
    студентський квиток: дві великі літери англійської абетки у верхньому регістрі, потім -, потім 8 цифр.
"""

import re

def getStudent():

    user_input = input("Print the name of student's ticket: ")

    if (re.match(r"^[A-Z]{2}\-\d{8}$", user_input) ):
        return user_input
    else:
        return False


"""
    Валідація компанії
    назва компанії: не більше 10 літер англійської абетки у нижньому регістрі, у кінці можуть бути дві цифри, наприклад privat24
"""

def getCompany():

    user_input = input("Print the name of complany: ")

    if (re.match(r"^[a-z]+8\w{0,2}$", user_input)):
        return user_input
    else:
        return False



"""
    Валідація навичків
    назва навички: не більше 30 літер англійської абетки у нижньому регістрі
"""


def getSkill():
    user_input = input("Print the name of skill: ")

    if (re.match(r"^[a-z]+$", user_input)):
        return user_input
    else:
        return False