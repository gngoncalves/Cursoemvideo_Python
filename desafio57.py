sexo = str(input('Insira o sexo [M/F]: ')).strip().upper()[0]
while sexo != 'F' and sexo != 'M':
    sexo = str(input('Dados inválidos. Insira novamente o sexo [M/F]: ')).strip().upper()[0]
print('Sexo {} cadastrado com sucesso.'.format(sexo))