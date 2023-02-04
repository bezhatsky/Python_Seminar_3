"""
1. Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
Напишите два варианта решения: через list и через dict.

Пример:
Введите номер месяца: 10
Результат через список: Осень
Результат через словарь: Осень
"""

# Через список:

month_num=int(input("введите номер месяца: "))
seasons=['зима','весна','лето','осень']
index=(month_num-1)//3
print("результат через список: {}".format(seasons[index]))

# Через словарь:

month_num=int(input("введите номер месяца: "))
season_dict={1:'зима',2:'зима',3:'весна',4:'весна',5:'весна',6:'лето',7:'лето',8:'лето',9:'осень',10:'осень',11:'осень',12:'зима'}
print("результат через словарь: {}".format(season_dict[month_num]))
