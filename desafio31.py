print('== Calculador de tarifa de viagem ==')
dist = float(input('Quantos Km será a viagem: '))

if dist <= 200:
    tarifa = dist * 0.5
else:
    tarifa = dist * 0.45
print('A tarifa para esta viagem de {} Km é de R${:.2f}.'.format(dist,tarifa))