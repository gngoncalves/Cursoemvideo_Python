preco = float(input('Insira o preço do produto: R$ '))
print('''Formas de Pagamento:
[ 0 ] - À vista em dinheiro/cheque
[ 1 ] - À vista no cartão
[ 2 ] - Em até 2x no cartão
[ 3 ] - 3x ou mais no cartão''')
pag = int(input('Qual será a forma de pagamento? '))

if pag == 0:
    preco = preco - (preco * 10/100)
    print('O preço final do produto para pagamento à vista em dinheiro/cheque é de R$ {:.2f}.'.format(preco))
elif pag == 1:
    preco = preco - (preco * 5/100)
    print('O preço final do produto para pagamento à vista no cartão é de R$ {:.2f}.'.format(preco))
elif pag == 2:
    print('O preço do produto para pagamento em até 2x no cartão é de R$ {:.2f}, sendo pago em 2 parcelas de R$ {:.2f}.'.format(preco, preco/2))
elif pag == 3:
    preco = preco + (preco * 20/100)
    parcelas = int(input('Em quantas parcelas será pago? '))
    prestacao = preco / parcelas
    print('O preco do produto para pagamento em 3x ou mais no cartão é de R$ {:.2f}, sendo pago em {} parcelas de R$ {:.2f}.'.format(preco, parcelas, prestacao))
else:
    print('Opcão inválida. Por favor, refaça a operação.')
print('Obrigado!')
