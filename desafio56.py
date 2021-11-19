soma = 0
media = 0
nomehvelho = ''
idadehvelho = 0
cont = 0
for i in range(1,5):
    print('[======[Dados pessoa {}/4]======]'.format(i))
    nome = str(input('Insira o nome: ')).strip()
    idade = int(input('Insira a idade: '))
    genero = str(input('Insira o gênero [M/F]: ')).upper().strip()[:1]
    if soma >= 0:
        soma += idade
    media = soma / i
    if genero == 'M' and idade > idadehvelho:
        idadehvelho = idade
        nomehvelho = nome
    if genero == 'F' and idade < 20:
        cont += 1
print('\nA média de idade inserida deste grupo, é {} anos.'.format(media))
if nomehvelho != '':
    print('O {} é o homem mais velho deste grupo, com {} anos.'.format(nomehvelho,idadehvelho))
else:
    print('Não existem homens neste grupo.')
if cont > 0:
    print('Existem {} mulheres com menos de 20 anos neste grupo.'.format(cont))
else:
    print('Não existem mulheres com menos de 20 anos neste grupo.')