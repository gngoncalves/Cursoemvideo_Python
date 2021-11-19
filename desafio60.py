num = int(input('Insira um número, para calcular o seu fatorial: '))
n = num
fact = 1
while n > 0:
    print('{}'.format(n), end='')
    print(' x ' if n > 1 else ' = {} '.format(fact), end='')
    fact *= n
    n -= 1
print('')
print('O fatorial de {} é igual a {}.'.format(num,fact))