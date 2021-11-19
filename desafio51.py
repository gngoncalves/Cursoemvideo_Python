print('== 10 Primeiros Termos de uma Progressão Aritmética ==')
a1 = int(input('Insira o primeiro termo da Progressão Aritmética: '))
r = int(input('Insira a razão da Progressão Aritmética: '))
for i in range (1,11):
    an = a1 + (i-1) * r
    print('O {}º termo da PA é {}.'.format(i,an))