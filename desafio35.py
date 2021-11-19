l1 = float(input('Insira o primeiro lado do triângulo: '))
l2 = float(input('Insira o segundo lado do triângulo: '))
l3 = float(input('Insira o terceiro lado do triângulo: '))

c1 = abs(l2 - l3) < l1 < (l2 + l3)
c2 = abs(l1 - l3) < l2 < (l1 + l3)
c3 = abs(l1 - l2) < l3 < (l1 + l2)

if c1 == True and c2 == True and c3 == True:
    print('É possível formar um triângulo com os lados {}, {} e {}.'.format(l1, l2, l3))
else:
    print('Não é possível formar um triângulo com os lados {}, {} e {}.'.format(l1, l2, l3))