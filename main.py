sides = [3, 2, 4, 7, 5, 12, 11, 13, 15, 16, 14, 14]
sides = sorted(sides, reverse=True)
smax = 0
for i in range(len(sides)):
   for j in range(i + 1, len(sides)):
       for k in range(j + 1, len(sides)):
           a = sides[i]
           b = sides[j]
           c = sides[k]
           if a + b > c and a + c > b and b + c > a:
               p = (a + b + c) / 2
               s = (p * (p - a) * (p - b) * (p - c)) ** (1 / 2)
               if s > smax:
                   smax = s

print("Максимальная площадь треугольника", smax)

import math
print("Домашнее задание\nВведите коэффициенты для уравнения\nax^2 + bx + c = 0:")
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))
discriminant = b ** 2 - 4 * a * c
print("Дискриминант D = %.2f" % discriminant)
if discriminant > 0:
   x1 = (-b + math.sqrt(discriminant)) / (2 * a)
   x2 = (-b - math.sqrt(discriminant)) / (2 * a)
   print("x1 = %.2f \nx2 = %.2f" % (x1, x2))
elif discriminant == 0:
   x = -b / (2 * a)
   print("x = %.2f" % x)
else:
   print("Корней нет")