real1 = int(input('Número de moedas de 1 real: '))
cent50 = int(input('Número de moedas de 50 centavos: '))
cent25 = int(input('Número de moedas de 25 centavos: '))
cent10 = int(input('Número de moedas de 10 centavos: '))
cent5 = int(input('Número de moedas de 5 centavos: '))
cent1 = int(input('Número de moedas de 1 centavo: '))

total = 1.00*real1 + 0.50*cent50 + 0.25*cent25 + 0.10*cent10 + 0.05*cent5 + 0.01*cent1
print(f'Quantia total calculada: R${round(total, 2):.2f}')
