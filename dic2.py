def vvod():

    mass = []
    
    log = input("Введите логин: ")
    passw = input("Введите пароль: ")

    while log != "конец" or passw != "конец":

        dic = {
            "логин": log,
            "пароль": passw
        }
        print('\n')
        log = input("Введите логин: ")
        passw = input("Введите пароль: ")
            

        mass.append(dic)

    vivvod(mass)



def vivod_vse(mas):
    res_ima = ''
    res_fam = ''
    
    res = 0 
        
    for k in mas:
        res_ima += k["логин"]
        res_fam += k["пароль"]
        res = res + 1 
                

        print('Пользователь',"№"+str(res))
        print('логин:',res_ima)
        print("пароль:",res_fam + '\n')
       
            
        res_ima = ''
        res_fam = ''
        
            




def vivvod(mass):

    vivod = input("Что вы хотите вывести, логин или пароль? ")
    if vivod == "всё":
        vivod_vse(mass)
    else:
        for i in mass:
            print(i[vivod])


vvod()


