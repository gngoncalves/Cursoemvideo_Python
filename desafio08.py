medida = float(input('Insira a medida em metros: '))
cm = medida*100
mm = medida*1000

print('A medida informada é: {} metros.'.format(medida))
print('{} metros é equivalente a {} centímetros ou {} milímetros.'.format(medida,cm,mm))