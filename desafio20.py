import random
nome1 = str(input('Isira o primeiro nome: '))
nome2 = str(input('Insira o segundo nome: '))
nome3 = str(input('Insira o terceiro nome: '))
nome4 = str(input('Insira o quarto nome: '))
lista = [nome1,nome2,nome3,nome4]
random.shuffle(lista)
print('A ordem da apresentação será:\n01 - {}\n02 - {}\n03 - {}\n04 - {}'.format(lista[0],lista[1],lista[2],lista[3]))