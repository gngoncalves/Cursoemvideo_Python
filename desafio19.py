from random import choice
nome1 = str(input('Insira o primeiro nome: '))
nome2 = str(input('Insira o segundo nome: '))
nome3 = str(input('Insira o terceiro nome: '))
nome4 = str(input('Insira o quarto nome: '))
lista = [nome1, nome2, nome3, nome4]
escolha = choice(lista)

print('O(a) aluno(a) escolhido(a) para apagar o quadro é o(a) {}.'.format(escolha))