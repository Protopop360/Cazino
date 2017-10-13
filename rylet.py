import random
vip_list = input("Введите имя приглашенных гостей: ").split(", ")

guest = {"Лаве": 500}
guest['Имя'] = input("Представьтесь!! ")
#guest["Лаве"] = int(input("Сколько у вас денег? "))
if guest['Имя'] in vip_list:
    while True:
        if guest["Лаве"] > 0:
            print("Проходите и делайте ставку ")
            guest["Ставка"] = int(input(" Ваша ставка"))
            if guest["Ставка"] >  guest["Лаве"]:
                print("Ваша ставка превышает сумму кошелька")
                guest["Ставка"] = guest["Лаве"]
            guest["Поставили"] = int(input("На что ставите? "))
            guest["Выпало"] = random.randint(1,36)
            print("Выпало", guest["Выпало"], "очков")
            if guest["Поставили"] == guest["Выпало"]:
                guest["Лаве"] += guest["Ставка"]*36
                print(guest['Имя'] , ",Вы только что выиграли", guest["Ставка"]*36)
            else:
                print(guest['Имя'] + " вы проиграли" )
                guest["Лаве"] -= guest["Ставка"]
        else:
            print("У вас недостаточно денег?")
            nu = input("Если хотите внести денег, напишите Да, инече Нет ")
            if nu == "Да":
                guest["Лаве"] =  int(input("Введите сколько хотите ввести "))
                continue
            else: 
                print("Будем рады видеть вас снова")
                break
else:
    print("Уходи" + guest['Имя'])