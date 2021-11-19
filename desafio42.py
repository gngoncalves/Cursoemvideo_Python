l1 = float(input('Insira o primeiro lado do triângulo: '))
l2 = float(input('Insira o segundo lado do triângulo: '))
l3 = float(input('Insira o terceiro lado do triângulo: '))
c1 = l1 < (l2 + l3)
c2 = l2 < (l1 + l3)
c3 = l3 < (l1 + l2)
if c1 == True and c2 == True and c3 == True:
    if l1 == l2 == l3:
        print('Estes lados nos permitem formar um triângulo equilátero.')
    elif l1 == l2 or l1 == l3 or l2 == l3:
        print('Estes lados nos permitem formar um triângulo isósceles.')
    elif l1 != l2 != l3 != l1:
        print('Estes lados nos permitem formar um triângulo escaleno.')
else:
    print('Estes lados não permitem formar um triângulo.')
print('Obrigado.')