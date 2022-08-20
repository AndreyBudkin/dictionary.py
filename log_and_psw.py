# def vvod():

#     mass = []
#     n = int(input("Введите количество логинов и паролей: "))

#     for i in range(n):
#         log = input("Логин: ")
#         passw = input("Пароль: ")
#         dic = {
#             "логин": log,
#             "пароль": passw
#         }
    

#         mass.append(dic)
#     vivvod(mass)

# def vivvod(mass):

#     vivod = input("Что вы хотите вывести, логин или пароль? ")
#     for i in mass:
#         print(i[vivod])

# vvod()




def vvod():

    mass = []
    
    log = input("Введите логин: ")
    passw = input("Введите пароль: ")

    while log != "конец" or passw != "конец":
        log = input("Логин: ")
        passw = input("Пароль: ")
        dic = {
            "логин": log,
            "пароль": passw
        }
            

        mass.append(dic)
    vivvod(mass)

def vivvod(mass):

    vivod = input("Что вы хотите вывести, логин или пароль? ")
    for i in mass:
        print(i[vivod])

vvod()