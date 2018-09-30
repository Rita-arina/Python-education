# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.

class Triangle:
    def __init__(self, A, B, C):
        # Функция вычисляет длину стороны согласно координатам точек
        def sideLen(dot1, dot2):
            return math.sqrt((dot1[0] - dot2[0]) ** 2
                             + (dot1[1] - dot2[1]) ** 2)

        self.A = A
        self.B = B
        self.C = C
        # На основании соседних координат вычисляем длину стороны AB
        self.AB = sideLen(self.A, self.B)
        self.BC = sideLen(self.B, self.C)
        self.CA = sideLen(self.C, self.A)

    # Вычисление площади треугольника по формуле Герона
    def areaTriangle(self):
        semi_perimeter = self.perimeterTriangle() / 2

        return math.sqrt(semi_perimeter
                         * (semi_perimeter - self.AB)
                         * (semi_perimeter - self.BC)
                         * (semi_perimeter - self.CA))

    # вычисляем периметр треугольника
    def perimeterTriangle(self):
        return self.AB + self.BC + self.CA

    # Вычисляем высоту треугольника
    def heightTriangle(self):
        return self.areaTriangle() / (self.AB / 2)

import math

treugolnik1 = Triangle((3, 2), (6, 7), (0, 12))

print(treugolnik1.areaTriangle())
print(treugolnik1.heightTriangle())
print(treugolnik1.perimeterTriangle())

# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.

class Trapeze:
   def __unit__(self, D, E, F, G):
        self.D = D
        self.E = E
        self.F = F
        self.G = G

    # Функция вычисляет длину стороны согласно координатам точек
    def sideLen(self, dot1, dot2):
        return math.sqrt((dot1[0] - dot2[0]) ** 2 + (dot1[1] - dot2[1]) ** 2)

    # На основании соседних координат вычисляем длины сторон
    self.DE = sideLen(self.D + self.E)
    self.EF = sideLen(self.F + self.E)
    self.FG = sideLen(self.F + self.G)
    self.DG = sideLen(self.D + self.G)

    print(self.DE, self.EF, self.FG, self.DG)

    #проверяем равнобокость трапеции
    def quilaterial (self):
        if self.DE == self.FG:
         print("Равнобокая трапеция")
        else:
         print("НЕ Равнобокая трапеция")

    #считаем длину периметра
    def perimeter (self):
        return self.DE+self.EF+self.FG+self.DG

    #считаем площадь
    def area (self):
        return ((self.DG+self.EF)/2)*math.sqrt((self.DE**2)-(((((self.DG-self.EF)**2)+self.DE**2)+self.FG**2)/2*(self.DG- self.EF)))**2

trapeze_now = Trapeze ((4, 2), (3, 6), (6, 6), (2, 8))

print(trapeze_now.area())
print(trapeze_now.perimeter())

