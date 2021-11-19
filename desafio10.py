real = (float(input('Qual o valor para conversão: R$')))

dolar = real/3.27

print('Você pode comprar ${:.2f}, com o valor de R${:.2f}.'.format(dolar,real))