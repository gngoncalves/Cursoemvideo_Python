from datetime import date
sexo = str(input('''Qual é o seu sexo?
[ M ] - Masculino
[ F ] - Feminino
Por favor, insira uma opção acima: ''')).upper()
sexo = sexo[0]
nasc = int(input('Insira o seu ano de nascimento: '))
ano_atual = date.today().year
idade = ano_atual - nasc

if sexo == 'M' and idade < 18:
    print('Ainda faltam {} ano(s) para o seu alistamento.'.format(18 - idade))
elif sexo == 'M' and idade == 18:
    print('Você já tem {} anos. É hora de realizar o seu alistamento.'.format(idade))
elif sexo == 'M' and idade > 18:
    print('Você já ultrapassou o período de alistamento militar em {} ano(s).'.format(idade - 18))
else:
    print('O alistamento é obrigatório para pessoas do sexo masculino.')
