cigarros = int(input('Quantida de cigarros por dia: '))
anos_fumante = int(input('Anos como fumante: '))
vida_perdida = anos_fumante * 365 * cigarros * 10 / 1440

print(f'Você perdeu {round(vida_perdida)} dias de vida.')
