vel = float(input('Qual a velocidade do veículo: '))

if vel > 80:
    multa = (vel - 80)*7
    print('O seu veículo foi multado. O valor de multa a pagar é de R$ {:.2f}.'.format(multa))
else:
    print('Tenha um bom dia! Dirija com segurança.')