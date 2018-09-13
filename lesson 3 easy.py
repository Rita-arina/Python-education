__author__ = 'Давыдова А.И.'

# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.

def my_round(number, ndigits):
    pass


print(my_round(2.1234567, 5))
print(my_round(2.1999967, 5))
print(my_round(2.9999967, 5))


def my_round(number, ndigits):
    pass
    number_1 = number * (10 ** ndigits) + 0.41
    number_1 = number_1 // 1
    number_1 = number_1 / (10 ** ndigits)
    return number_1


print(my_round(2.1234567, 5))
print(my_round(2.1999967, 5))
print(my_round(2.9999967, 5))

# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить

def lucky_ticket(ticket_number):
    pass


print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))

def lucky_ticket(ticket_number):
    pass
    bilet = str(ticket_number)
    if len(bilet)<6:
        False
    else:
     a = int(bilet[0]) + int(bilet[1])
     b = int(bilet[4]) + int(bilet[5])
     if a == b:
        return True
     else:
        return False
pass

print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))