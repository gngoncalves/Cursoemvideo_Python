print('Conversor de números na base 10, para a números binários, octadecimais e hexadecimais')
num = int(input('Por favor, insira o número a ser convertido: '))
base = int(input('Bases de conversão:\n1 - número binário\n2 - número octadecimal\n3 - número hexadecimal\nEscolha uma opção válida: '))

if base == 1:
    print('O número {} convertido para base binária, é igual a \033[31m{}\033[m.'.format(num,bin(num)[2:]))
elif base == 2:
    print('O número {} convertido para a base octal, é igual a \033[32m{}\033[m.'.format(num,oct(num)[2:]))
elif base == 3:
    print('O número {} convertido para base hexadecimal, é igual a \033[35m{}.\033[m'.format(num,hex(num)[2:]))
else:
    print('Você não escolheu uma opção válida.')
print('Obrigado.')