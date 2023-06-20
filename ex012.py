preco = float(input('Informe o valor do produto: R$ '))
desconto = float(input('Informe o percentual do desconto: '))
preco_com_desconto = preco - (preco * desconto / 100)

print('Para um produto que custa {}, o valor com desconto de {}, será {}.'.format(preco, desconto, preco_com_desconto))