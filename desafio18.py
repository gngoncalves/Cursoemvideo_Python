from math import sin, cos, tan, radians
num = int(input('Insira um ângulo: '))

print('Valores em Rad:')
print('O seno de {}º é {:.2f}.'.format(num,sin(num)))
print('O cosseno de {}º é {:.2f}.'.format(num,cos(num)))
print('A tangente de {}º é {:.2f}.\n'.format(num,tan(num)))

print('Valores em Deg:')
print('O seno de {}º é {:.2f}.'.format(num,sin(radians(num))))
print('O cosseno de {}º é {:.2f}.'.format(num,cos(radians(num))))
print('A tangente de {}º é {:.2f}.'.format(num,tan(radians(num))))