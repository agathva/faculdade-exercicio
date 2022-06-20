preço = float(input('Preço do produto R$'))
promoçao = preço - preço * 5 / 100
print(f'Preço promocional com 5% de desconto: R${round(promoçao, 2):.2f}')