#__author__ = 'Давыдова А.И.'

fruits = ['apple', 'banana', 'kiwi', 'watermelon']
i = 1
for fruit in fruits:
    print ('{}. {:>}'.format(i, fruit))
    i += 1


# Задача-1:
# Дан список фруктов.
# Напишите программу, выводящую фрукты в виде нумерованного списка,
# выровненного по правой стороне.

# Пример:
# Дано: ["яблоко", "банан", "киви", "арбуз"]
# Вывод:
# 1. яблоко
# 2.  банан
# 3.   киви
# 4.  арбуз

# Подсказка: воспользоваться методом .format()





# Задача-2:
# Даны два произвольные списка.
# Удалите из первого списка элементы, присутствующие во втором списке.

fruits_one = ["яблоко", "банан", "киви", "арбуз"]
fruits_two = ["яблоко", "абрикос", "ананас", "арбуз"]
for fruit in fruits_two:
     if fruit in fruits_one:
         fruits_one.remove(fruit)
print (fruits_one)





# Задача-3:
# # # # # Дан произвольный список из целых чисел.
# # # # # Получите НОВЫЙ список из элементов исходного, выполнив следующие условия:
# # # # # если элемент кратен двум, то разделить его на 4, если не кратен, то умножить на два.

a = [5, 5, 25, 40, 15616, 45, 25]
b = []
for abc in a:
    if abc % 2.0 == 0:
        new_1 = abc / 4
        b.append(new_1)

    elif not abc % 2 == 0:
        new_2 = abc*2
        b.append(new_2)

print(b)