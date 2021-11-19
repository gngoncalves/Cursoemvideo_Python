from math import trunc
num = int(input('Insira um número entre 0 e 9999: '))
numero = str(num)
numero = numero[::-1]
print('Modo String:')
print('Milhar: {:<1}'.format(numero[3:4]))
print('Centena: {:<1}'.format(numero[2:3]))
print('Dezena: {:<1}'.format(numero[1:2]))
print('Unidade: {:<1}\n'.format(numero[0:1]))

print('Modo Matemático:')
milhar = num/1000
print('Milhar: {}'.format(trunc(milhar)))
centena = (num%1000)/100
print('Centena: {}'.format(trunc(centena)))
dezena = (num%100)/10
print('Dezena: {}'.format(trunc(dezena)))
unidade = (num%10)
print('Unidade: {}'.format(unidade))