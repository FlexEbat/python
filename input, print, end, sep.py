'''

----------------------------------------
					INPUT, END, SEP

name = input()
print(name)

name = input("Как вас зовут?: ")
print(f"Ваше имя: {name}")
print("Вас зовут - ", name, "." , "Вам -", age, "Лет", sep = '*')
minus = "-"
# В стоке, каждое новое слово разделяется пробелом, тут задаётся между каждый словом знак "-"
print("To4ka", "Ka", "Sh", "Ke", sep=minus)
 Каждая строка в стоке разделяется пробелом, тут задается интервал между строка в виде символа "-"
print("To4ka", "Ka", "Sh", "Ke", end=minus)
print("ogo sebe")
# Каждая строка в стоке разделяется пробелом, тут задается интервал между строка в виде символа "-"
 print("To4ka", "Ka", "Sh", "Ke", sep="#")
 print("To4ka", "Ka", "Sh", "Ke", end="#")
print("ogo sebe")
print("To4ka", "Ka", "Sh", "Ke", sep = "*", end = "finish")
Зшт print("")
----------------------------------------
                       MATH

number = 10
number += 5
print(number)  # 15
 
number -= 3
print(number)  # 12
 
number *= 4
print(number)  # 48


#Округление и функция round

print(2.0001 + 0.1)  # 2.1001000000000003
first_number = 2.0001
second_number = 0.1
third_number = first_number + second_number
print(round(third_number, 2))  # После переменной значение указывает сколько знаков после запятой нужно оставить.

# округление до целого числа
print(round(2.49))  # 2 - округление до ближайшего целого 2
print(round(2.51))  # 3
#Однако если округляемая часть равна одинаково удалена от двух целых чисел, то округление идет к ближайшему четному:
print(round(2.5))   # 2 - ближайшее четное
print(round(3.5))   # 4 - ближайшее четное
# - Округление производится до ближайшего кратного 10 в степени минус округляемая часть:
# округление до двух знаков после запятой
print(round(2.554, 2))      # 2.55
print(round(2.5551, 2))      # 2.56
print(round(2.554999, 2))   # 2.55
print(round(2.499, 2))      # 2.5

#Однако следует учитывать, что функция round() не идеальный инструмент.
 #Например, выше при округление до целых чисел применяется правило, согласно которому,
 # если округляемая часть одинаково удалена от двух значений, то округление производится до ближайшего четного значения.
 #  В Python в связи с тем, что десятичная часть числа не может быть точно представлена в виде числа float, то это может приводить к некоторым не совсем ожидаемым результатам. 
 #  Например:
# округление до двух знаков после запятой
print(round(2.545, 2))   # 2.54
print(round(2.555, 2))   # 2.56 - округление до четного
print(round(2.565, 2))   # 2.56
print(round(2.575, 2))   # 2.58
 
print(round(2.655, 2))   # 2.65 - округление не до четного
print(round(2.665, 2))   # 2.67
print(round(2.675, 2))   # 2.67

#print(2**(-2)) # Отриц. степень
#print((-3)**3) # Отриц. числов в степень


----------------------------------------

						PEREMENIE
name, surname = "Anton", "Gandon"
print(name, surname)
name1, surname1 = name, surname
print(name1, surname1)

hz
# Здесь используется String - строка
num11 = input()
num22 = input()
num33 = num11+num22
 print(num33)

# Здесь используется int - Целое число
num11 = int(input())
num22 = int(input())
num33 = num11+num22
 print(num33)
# Если бы используем String - то он будет складывать num11 и num22(50 и 50, возможно любое другое значение), но как строки - т.е получится 5050
# А если использовать Int - То он сложить 50 и 50, и получится 100

num1 = 17
num2 = 12
s = str(num1)
 print(s)
s1 = str(num2)
 print(num1+num2)
print(s + s1)


a = 1
if a > 2:
    print("a > 2", "a =", a)
else:
    print("a < 2", "a =", a)
----------------------------------------
						FLOAT
a = 45.5
b = 68.
print(a)
print(b)
x = 3.9e3
print(x)
----------------------------------------

						ВСТАВКА ЗНАЧЕНИЙ В СТРОКУ


name = "Tom"
age = 15
user = f"name: {name}, age: {age}"
print(user)

----------------------------------------

							ДИНАМИЧЕСКАЯ ТИПЕЗАЦИЯ

----------------------------------------


userid = "Abc"
print(userid, end = " ")


print(type(userid))
userid = 123
print(userid, end = " ")
print(type(userid))

----------------------------------------




----------------------------------------

				PRINT



print("Hello world", end = " and ")
print("Hello Metanit.com", end = " and ")
print("Hello python")
name = input("Как вас зовут: ")
age = int(input("Сколько вам лет: "))
if age > 1:
	print(f"Вас зовут: {name}, Bам: {age} лет.")
else:
	print("Вам не может быть меньше нуля лет")
----------------------------------------
				Операции сравнения


#Оператор in возвращает True если в некотором наборе значений есть определенное значение. Он имеет следующую форму:


message = "hello world!"
hello = "hello"
print(hello in message)
print(hello not in message)

gold = "gold"
print(gold in message)
print(gold not in message)


----------------------------------------
				Условная конструкция if

bilet = True
language = "Poland"
if language == "english":
	print("Ура ты сьебался с россии")
elif language == "germany":
	print("Ура Германия немцы сосите хуй")
elif language == "Poland":
	print("Привет Польшая пошли нахуй все")
elif language == "Russia":
	print("Заебала Россия как с неё сьебать")
	if bilet == True:
		print(f"Билет {bilet} ")
		print("Слава богу билет есть, можешь сьебаться", end = " ")
else: 
	print("Ты вообще где дебил")

----------------------------------------

			ELIF, FOR
			Циклы позволяют выполнять некоторое действие в зависимости от соблюдения некоторого условия. В языке Python есть следующие типы циклов:




number = 10

while number < 5:
	print(f"number = {number}")
	number +=1
else:
	print(f"number = {number}. Работа цилка завершена")
print("Готово")
			Другой тип циклов представляет конструкция for.
			Этот цикл пробегается по набору значений, помещает каждое значение в переменную, и затем в цикле мы можем с этой переменной производить различные действия

#message = "hello"
#
#for c in message:
#	print(c) 

for n in range(5,10):
	print(n, end=" ")
else:
	print(f"Последний символ цикла: {n}")
print("")

for n in range(10):
	print(n, end=" ")
else:
	print(f"Последний символ цикла: {n}")
print("")

for n in range(0, 10, 2):
	print(n, end=" ")
else:
	print(f"Последний символ цикла: {n}")
print("")
number = 10

while (number < 5):
	print(f"number = {number}")
	number +=1
else:
	print(f"number = {number}. Конца цикла.")
print("Конец программы")

for n in range(10):
	print(n, end= " ")

for n in range(0, 10, 2):
	print(n, end= " ")

message = "Hello"
for c in message:
	print(c)
else:
	print(f"Последний символ: {c}")


i = 1
j = 1
while i < 10:
	while j < 10:
		print(i * j, end = " ")
		j += 1
	print("\n")
	j = 1
	i += 1
----------------------------------------

    Функции - def
    Функции представляют блок кода, который выполняет определенную задачу и который можно повторно использовать в других частях программы. 
def print_message():
	# определение локальный функциц
	def say_hello(): print("Hello world")
	def say_goobye(): print("Goodbye")
	# вызов локальный функций
	say_hello()
	say_goobye()

print_message()


def person(name, age):
	print(f"Hello, {name}. Тебе {age} лет.")

person("Tom", 17)

def say_hello(name = "Pidor"):
	print(f"Ну привет {name}")

say_hello()
'''

age = 15
if (age < 15):
	print("Малышка")
elif (age > 30):
	print("Уже взрослый")
else:
	print("Ой...")