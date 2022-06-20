sal_min = float(input('Salário-mínimo vigente: R$'))
sal = float(input('Salário do funcionário: R$'))
qtdd = sal // sal_min
print(f'Este funcionário ganha {round(qtdd)} salários-mínimo ')
