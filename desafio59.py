n1 = 0
n2 = 0
menu = -1
while menu != 5:
    n1 = int(input('Insira o primeiro número: '))
    n2 = int(input('Insira o segundo número: '))
    print('='*20)
    print('''Menu:
[1] - Somar os dois números
[2] - Multiplicar os dois números
[3] - Identificar o maior dos dois números
[4] - Digitar novos números
[5] - Sair do programa''')
    menu = int(input('Digite a opção desejada: '))
    print('='*20)
    if menu == 1:
        soma = n1 + n2
        print('A soma entre {} e {} é {}.'.format(n1,n2,soma))
        print('Vamos iniciar novamente!\n')
    elif menu == 2:
        mult = n1 * n2
        print('O produto entre {} e {} é {}.'.format(n1,n2,mult))
        print('Vamos iniciar novamente!\n')
    elif menu == 3:
        if n1 > n2:
            print('O número {} é o maior dentre os dois números inseridos.'.format(n1))
            print('Vamos iniciar novamente!\n')
        elif n2 > n1:
            print('O número {} é o maior dentre os dois números inseridos.'.format(n2))
            print('Vamos iniciar novamente!\n')
        else:
            print('Os números {} e {} são iguais.'.format(n1,n2))
            print('Vamos iniciar novamente!\n')
    elif menu == 4:
        print('Ok! Vamos recomeçar!\n')
    else:
        print('Opção Inválida. Tente novamente.\n')
print('Você saiu do programa.')
