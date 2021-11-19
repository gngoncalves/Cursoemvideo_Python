n1 = float(input('Insira o primeiro número:'))
n2 = float(input('Insira o segundo número:'))
n3 = float(input('Insira o terceiro número: '))
menor = n1
if n2<n1 and n2<n3:
    menor = n2
if n3<n1 and n3<n2:
    menor = n3

maior = n1
if n2>n1 and n2>n3:
    maior = n2
if n3>n1 and n3>n2:
    maior = n3

print('O maior número inserido é {}.'.format(maior))
print('O menor número inserido é {}.'.format(menor))