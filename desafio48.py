n = 0
c = 0
for i in range (1,501,2):
    if i % 3 == 0:
        c += 1
        n += i
print('A soma de todos os {} números ímpares e múltiplos de 3, é {}.'.format(c, n))