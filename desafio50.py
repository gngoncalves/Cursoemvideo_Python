soma = 0
c = 0
for i in range(1,7):
    num = int(input('Insira um número [{}/6]: '.format(i)))
    if num % 2 == 0:
        c += 1
        soma += num
print('A soma dos {} números pares inseridos é de {}.'.format(c,soma))