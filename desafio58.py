from random import randint
npc = randint(0, 10)
num = -1
c = 0
while num != npc:
    num = int(input('Insira um número entre 0 e 10: '))
    c += 1
    if num == npc:
        print('Parabéns! Você acertou!')
    else:
        if num > npc:
            print('Menos... Tente novamente!')
        else:
            print('Mais... Tente novamente!')
print('Jogo finalizado. Você precisou de {} tentativa(s) para acertar.'.format(c))