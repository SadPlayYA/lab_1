import math



print('Введите коэффиценты квадратного уравнения вида:')
print('ax^2+bx+c=0')
a = float(input('Введите коэффицент а = '))
b = float(input('Введите коэффицент b = '))
c = float(input('Введите коэффицент c = '))
d = b * b - 4 * a * c
x1, x2, x = 0, 0, 0
print('Дискриминант = ', d)
print('Ответ: ')
if d > 0:
    x1 = (-b + math.sqrt(d)) / 2 * a ; print('x1 = ', x1)
    x2 = (-b - math.sqrt(d)) / 2 * a ; print('x2 = ', x2)
elif d == 0:
    x = -b / 2 * a ; print('x = ', x)
else:
    print("Ваше уравнение не имеет корней")