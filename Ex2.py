# # Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
# Пример:
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

x = int(input('Введите данные для X: '))
y = int(input('Введите данные для Y: '))
z = int(input('Введите данные для Z: '))

a = x * y * z
b = x + y + z

if a > 0:
     a = 0
elif a < 1:
     a = 1
if b > 0:
     b = 1
elif b < 1:
     b = 1

if a == b:
     print('Утверждение истинно')
elif a != b:
     print('Утверждение ложно')

leftSide = not (x or y or z)
rightSide = not x and not y and not z
result = leftSide == rightSide

if result == True:
     print('Утверждение истинно')
else:
     print('Утверждение ложно')