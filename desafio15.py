dias = int(input('Quantidade de dias de aluguel do veículo: '))
km = float(input('Quantidade de quilômetros percorrida pelo veículo durante a locação: '))
total = (dias * 60) + (km * 0.15)

print('O valor total a pagar pela locação é de R${:.2f}'.format(total))