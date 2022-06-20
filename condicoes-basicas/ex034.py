base = float(input('Base do retângulo: '))
altura = float(input('Altura do retângulo: '))

area = base * altura
perimetro = 2 * (base + altura)
diagonal = (base**2 + altura**2) ** (1/2)
print(f'Área do retângulo: {area}')
print(f'Perímetro do retângulo: {perimetro}')
print(f'Diagonal do  retângulo: {diagonal}')
