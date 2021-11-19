num1 = int(input('Insira o primeiro número para comparação: '))
num2 = int(input('Insira o segundo número para comparação: '))

if num1 > num2:
    print('O primeiro número ,\033[1;34m{}\033[m, é o maior número.'.format(num1))
elif num2 > num1:
    print('O segundo número ,\033[1;31m{}\033[m, é o maior número.'.format(num2))
else:
    print('\033[4mNão existe valor maior.\033[m Os dois números são iguais.')

