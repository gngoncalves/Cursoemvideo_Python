preco_original = (float(input('Insira o preço original: ')))
desconto = (5/100)

novo_preco = preco_original*(1-desconto)

print('O preço com desconto é R${:.2f}.'.format(novo_preco))