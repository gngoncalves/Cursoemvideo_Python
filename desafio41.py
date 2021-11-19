from datetime import date
print('Vamos definir a sua categoria na confederação:')
ano = int(input('Insira seu ano de nascimento: '))
idade = date.today().year - ano
if idade <= 9:
    print('Como a sua idade é {} anos, sua categoria é a MIRIM.'.format(idade))
elif idade <= 14:
    print('Como a sua idade é {} anos, sua categoria é a INFANTIL.'.format(idade))
elif idade <= 19:
    print('Como a sua idade é {} anos, sua categoria é a JÚNIOR.'.format(idade))
elif idade <= 25:
    print('Como a sua idade é {} anos, sua categoria é a SÊNIOR.'.format(idade))
else:
    print('Como a sua idade é {} anos, sua categoria é a MASTER.'.format(idade))
