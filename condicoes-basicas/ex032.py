anos = int(input('Anos: '))
meses = int(input('Meses: '))
dias = int(input('Dias: '))

totDias = anos*365 + meses*30.417 + dias
print(f'{anos} anos, {meses} meses e {dias} dias = {round(totDias)} dias')
