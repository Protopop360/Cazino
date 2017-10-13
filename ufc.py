import random 

def creat_fighter():
	person = {"Сила": 100, "Выносливость": 1000}
	person["Имя"] = input("Введи имя, боец")
	choose = input("1- прирост к силе\
		2-прирост к выносливости")
	if choose == 1:
		person["Сила"] += 40
	else:
		person["Выносливость"] += 400
	return person

def health(person1):
	print("У игрока", person1["Имя"], "осталось", person1["Выносливость"])

def attack(attacker, defender):
	damage = random.randint(attacker["Сила"]- 40,
	attacker["Сила"] + 40)
	print("Игрок", attacker["Имя"], "Нанес", attacker["Сила"], "урона")
	defender["Выносливость"] -= damage

person1 = creat_fighter()
person2 = creat_fighter()

while True:
	health(person1)
	health(person2)
	attack(person1,person2)
	attack(person2,person1)
	input()
	if person1["Выносливость"] <= 0:
		print("Боец", person2["Имя"], "выиграл")
		break
	if person2["Выносливость"] <= 0:
		print("Боец", person1["Имя"], "выиграл")
		break


