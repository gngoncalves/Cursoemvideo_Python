from random import randint
from time import sleep
print('Vamos jogar Pedra, Papel e Tesoura?')
print('''Selecione a opção desejada:
[ 0 ] - Pedra
[ 1 ] - Papel
[ 2 ] - Tesoura''')
player = int(input('Selecione uma das opções acima: '))
lista = ['Pedra','Papel','Tesoura']
npc = randint(0,2)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!')
if player <= 2:
    print('-='*10)
    print('Você escolheu a opção {}.'.format(lista[player]))
    print('A máquina escolheu a opção {}.'.format(lista[npc]))
    print('-='*10)
    if npc == 0 and player == 0 or npc == 1 and player == 1 or npc == 2 and player == 2:
        print('Empate. Vamos jogar novamente!')
    elif npc == 0 and player == 2:
        print('A máquina venceu. {} ganha de {}.'.format(lista[npc], lista[player]))
    elif npc == 1 and player == 0:
        print('A máquina venceu. {} ganha de {}.'.format(lista[npc], lista[player]))
    elif npc == 2 and player == 1:
        print('A máquina venceu. {} ganha de {}.'.format(lista[npc], lista[player]))
    elif player == 0 and npc == 2:
        print('Você venceu. {} ganha de {}.'.format(lista[player], lista[npc]))
    elif player == 1 and npc == 0:
        print('Você venceu. {} ganha de {}.'.format(lista[player], lista[npc]))
    elif player == 2 and npc == 1:
        print('Você venceu. {} ganha de {}.'.format(lista[player], lista[npc]))
else:
    print('Opcão inválida. Tente Novamente.')
