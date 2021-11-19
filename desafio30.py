print('Vamos verificar se um número é par ou ímpar?')
num = int(input('Insira um número: '))

if num % 2 == 0:
    print('O número {} é PAR.'.format(num))
else:
    print('O número {} é Ímpar.'.format(num))