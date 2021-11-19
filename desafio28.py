from random import randint
from time import sleep
m = randint(0, 5)
n = int(input('Tente advinhar o número escolhido pela máquina!\nInsira um número entre 0 e 5: '))
print('PROCESSANDO...')
sleep(3)
print('O número escolhido pela máquina foi: {}.'.format(m))
if n == m :
    print('Parabéns! Você Acertou!')
else:
    print('Que pena! Você errou.')