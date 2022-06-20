sal = float(input('Salário do Funcionário: R$'))
aumento = sal + sal * 15 / 100
print(f'Salário com aumento de 15%: R${round(aumento, 2):.2f}')
