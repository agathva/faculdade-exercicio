totDias = int(input('Dias: '))
anos = totDias // 365
meses = (totDias % 365) // 30
dias = (totDias % 365) % 30
print(f'{totDias} dias = {anos} anos, {meses} meses e {dias} dias')
