from math import hypot
cateto_op = float(input('Insira o valor do cateto oposto: '))
cateto_adj = float(input('Insira o valor do cateto adjacente: '))
hipotenusa = hypot(cateto_op, cateto_adj)

print('A hipotenusa deste triângulo é {:.2f}.'.format(hipotenusa))