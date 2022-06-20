m = int(input('Insira o valor de M: '))
n = int(input('Insira o valor de N: '))

if m > n:
    lado1= m**2 - n**2
    lado2= 2 * m * n
    hipo= m**2 + n**2
    print(f'Lado : {lado1}')
    print(f'Lado 2: {lado2}')
    print(f'Hipotenusa: {hipo}')
else:
    print('Impossível formar a tripla pitagórica')
