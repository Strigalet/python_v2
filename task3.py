
from data import dataset
from task1 import *

#   Написати рекурсивну функцію, що зберігає інформацію кількість вмінь, що отримав студент
#   Рекурсивно необхідно пройтись по користувачам та по компаніям, де вони працювали.



def recursionByCompany(student,b,counter):

    if  company_list=[]

    return skills





def recursionByStudents(k=list(dataset.keys()),b=dict()):
    if k=[]:
        return b
    else:
        student = k[0]
        company_list = list(dataset[student].keys())
        skill = recursionByCompany(student, company_list)

        b[student] = skill

        return recursionByUsers(k[1:], b)






print("Task 3")

result = recursionByStudents()
print(result)

print("\n\n")



