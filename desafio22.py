nome = str(input('Insira o nome completo: ')).strip()

print('Seu nome com letras maiúsculas é {}.'.format(nome.upper()))
print('Seu nome com letras minúsculas é {}.'.format(nome.lower()))
print('Seu nome completo possui {} caracteres.'.format(len(nome)-nome.count(' ')))
lista = nome.split()
print('Seu primeiro nome possui {} letras.'.format(len(lista[0])))
