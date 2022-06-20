sal = float(input('Salário: R$'))
conta1 = float(input('Primeira conta: R$'))
conta2 = float(input('Segunda conta: R$'))

tot = sal - (conta1 + conta1*0.02) - (conta2 + conta2*0.02)
print(f'Sobrou R${round(tot, 2):.2f}')
