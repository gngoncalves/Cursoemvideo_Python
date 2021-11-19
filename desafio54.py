from datetime import date
atual = date.today().year
maior = 0
menor = 0
for i in range (1,8):
    print('=' * 45)
    nasc = int(input('Digite o de nascimento [Pessoa {}/7]: '.format(i)))
    if atual - nasc >= 21:
        maior += 1
    else:
        menor += 1
print('=' * 45)
print('Nos dados informados acima, temos \033[32m{}\033[m pessoas com idade acima de 21 anos.'.format(maior))
print('Nos dados informados acime, temos \033[36m{}\033[m pessoas com idade abaixo de 21 anos.'.format(menor))