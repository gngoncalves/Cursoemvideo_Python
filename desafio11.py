altura = (float(input('Qual a altura da parede a ser pintada, em metros: ')))
largura = (float(input('Qual a largura da parde a ser pintada, em metros: ')))

area = altura*largura
tinta = area/2

print('Serão necessários {:.1f} litros de tinta para pintar esta parede.'.format(tinta))