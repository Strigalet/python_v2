from data import dataset


#    Створити пакет validators та написати функції, що валідують усі дані. Імпорутвати дані функції.

from validators.lib import getStudent
from validators.lib import getCompany
from validators.lib import getSkill


from task1 import addStudentSkill


#   Написати функцію, що зберігає інформацію про вміння студента у певній компанії
#   Усі дані вводить користувач. Використати валідатори. Викликати функцію

def addStudentSkillValidator():

    student=getStudent()
    if not student:
        print("Print correct data:" )
        student = getStudent()

    company=getCompany()
    if not company:
        print("Print correct data:" )
        company = getCompany()
    skill=getSkill()
    if not skill:
        print("Print correct data:" )
        skill = getSkill()

    addStudentSkill(student, company, skill)



print("Task 1")
addStudentSkillValidator()
print(dataset)


print("\n\n")