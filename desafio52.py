num = int(input('Insira um número: '))
c = 0
for i in range(1,(num+1)):
    if num % i == 0:
        c += 1
        print('\033[32m{}\033[m '.format(i), end='')
    else:
        print('\033[31m{}\033[m '.format(i), end='')
print('')
if c == 2:
    print('O número {} é um Número Primo, pois foi divisível {} vezes.'.format(num,c))
else:
    print('O número {} não é um Número Primo, pois foi divisível {} vezes.'.format(num,c))
