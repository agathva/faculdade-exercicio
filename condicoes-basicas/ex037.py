nota1 = float(input('Nota 1: '))
peso1 = float(input('Peso 1: '))
nota2 = float(input('Nota 2: '))
peso2 = float(input('Peso 2: '))
nota3 = float(input('Nota 3: '))
peso3 = float(input('Peso 3: '))

media = (nota1*peso1 + nota2*peso2 + nota3*peso3) / (peso1 + peso2 + peso3)
print(f'Média: {round(media, 1)}')
