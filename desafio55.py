maiorpeso = 0
menorpeso = 0
for i in range (1,6):
    print('='* 30)
    peso = float(input('Insira o peso em Kg [{}/5]: '.format(i)))
    if peso > maiorpeso:
        maiorpeso = peso
    elif peso < menorpeso or menorpeso <= 0:
        menorpeso = peso
print('=' * 30)
print('O menor peso informado foi de {} Kg.'.format(menorpeso))
print('O maior peso informado foi de {} Kg.'.format(maiorpeso))