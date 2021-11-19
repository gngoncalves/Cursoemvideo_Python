n1 = float(input('Insira a primeira nota: '))
n2 = float(input('Insira a segunda nota: '))
media = (n1 + n2) / 2

if media < 5:
    print('Sua média foi de {:.1f}. Infelizmente, você está \033[1;31mREPROVADO(A)\033[m.'.format(media))
elif media >= 5 and media < 7:
    print('Sua média foi de {:.1f}. Você está de \033[1;33mRECUPERAÇÃO\033[m.'.format(media))
else:
    print('Parabéns!Sua média foi de {:.1f}! Você foi \033[1;32mAPROVADO(A)\033[m!'.format(media))
