salario = float(input('Insira o valor do salário: R$'))
if salario <= 1250:
    reajuste = salario + (salario * 15 / 100)
else:
    reajuste = salario + (salario * 10 / 100)
print('O novo sálario será de R$ {:.2f}.'.format(reajuste))
