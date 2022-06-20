sal_fixo = float(input('Salário fixo do funcionário: R$'))
vendas = float(input('Valor de suas vendas: R$'))
tot = sal_fixo + vendas * 0.04
print(f'Salário final: R${round(tot, 2):.2f}')
