quilometro = float(input('Quilômetro rodado: '))
dias = int(input('Dias com o carro alugado: '))
total = 90 * dias + 0.20 * quilometro
print(f'Total a pagar: R${round(total, 2):.2f}')
