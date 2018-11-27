from data import dataset

#   Написати функцію, що зберігає інформацію про улюблену страву користувача у певній країні
#   Викликати функцію


def addStudentSkill(student, company, skill):
    if student in dataset:
        if company in dataset[student]:
            dataset[student][company].add(skill)
        else:
            dataset[student][company]=[skill]
    else:
        dataset[student]={company: {skill}}



print("Task 1")

#Додати нового студента та вміння у новій компанії
addStudentSkill("MB-99999999","blizzard","playing")

#Додати існуючому студенту нове вміння у новій компанії
addStudentSkill("КВ-12121212","google","reading")

#Додати існуючому студенту нове вміння в існуючій компанії
addStudentSkill("КВ-12121212","privat24","fishing")

print(dataset)


print("\n\n")