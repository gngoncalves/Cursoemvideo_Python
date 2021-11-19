salario = float(input('Informar o salário base do funcionário: '))
aumento = (15/100)

novo_salario = salario*(1+aumento)

print('O novo salário com aumento será de R${:.2f}.'.format(novo_salario))