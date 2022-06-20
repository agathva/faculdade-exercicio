prova1 = float(input('Prova 1: '))
prova2 = float(input('Prova 2: '))
lista1 = float(input('Lista 1: '))
lista2 = float(input('Lista 2: '))
lista3 = float(input('Lista 3: '))
lista4 = float(input('Lista 4: '))
lista5 = float(input('Lista 5: '))
trabalho = float(input('Trabalho: '))

mediaLista = (lista1 + lista2 + lista3 + lista4 + lista5) / 5
media = prova1*0.3 + prova2*0.4 + 0.2*(mediaLista) + 0.1*trabalho
print(f'Média: {round(media, 1):.1f}')
