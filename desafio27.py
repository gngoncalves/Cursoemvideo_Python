nome = str(input('Insira o seu nome completo: '))
lista = nome.split()
print('Primeiro nome : {}'.format(lista[0]))
print('Último nome: {}'.format(lista[len(lista)-1]))
