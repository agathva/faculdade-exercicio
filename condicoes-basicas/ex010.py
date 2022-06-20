largura = float(input('Largura da parede: '))
altura = float(input('Altura da parede: '))
area = largura * altura
tinta = area / 2
print(f'Área a ser pintada: {round(area, 2):.2f}m')
print(f'Quantidade de tinta necessária: {round(tinta, 2):.2f}')
