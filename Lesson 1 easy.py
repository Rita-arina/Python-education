__author__ = 'Давыдова А.И.'

# Задача-1: Дано произвольное целое число (число заранее неизвестно).
# Вывести поочередно цифры исходного числа (порядок вывода цифр неважен).
# Подсказки:
# * постарайтесь решить задачу с применением арифметики и цикла while;
# * при желании решите задачу с применением цикла for.

a = int(input('введите целое число: '))
if a == 0:
    print(a)
else:
    while a > 0:
        print(a % 10)
        a=a//10


# Задача-2: Исходные значения двух переменных запросить у пользователя.
# Поменять значения переменных местами. Вывести новые значения на экран.
# Подсказка:
# * постарайтесь сделать решение через дополнительную переменную
#   или через арифметические действия
# Не нужно решать задачу так:
# print("a = ", b, "b = ", a) - это неправильное решение!

a = int(input('введите первое число: '))
b = int(input('введите второе число: '))
c = a
d = b
print("теперь первое число", d)
print("а второе число", c)

# Задача-3: Запросите у пользователя его возраст.
# Если ему есть 18 лет, выведите: "Доступ разрешен",
# иначе "Извините, пользование данным ресурсом только с 18 лет"

a = int(input('введите свой возраст: '))
if a > 18:
    print ("Доступ разрешен")
else:
    print("Извините, пользование данным ресурсом только с 18 лет")