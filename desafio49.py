num = int(input('Qual tabuada deseja calcular? '))
nome = ' Tabuada de {} '.format(num)
print('{:=^40}'.format(nome))
for i in range(1,11):
    p = num * i
    print('{:^2} x {:^2} = {:>2}'.format(num,i,p))