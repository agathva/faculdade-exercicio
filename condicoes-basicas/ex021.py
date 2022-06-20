from math import sqrt
a = int(input('Valor de A: '))
b = int(input('Valor de B: '))
c = int(input('Valor de C: '))

delta = b**2 - 4 * a * c
x1 = (-b + sqrt(delta)) / (2 * a)
x2 = (-b - sqrt(delta)) / (2 * a)

print(f'{a}x² + {b}x + {c} = 0')
print(f'X1 = (-{b} + √{delta}) / (2 * {a}) = {x1}')
print(f'X2 = (-{b} - √{delta}) / (2 * {a}) = {x2}')
