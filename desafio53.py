p1 = str(input('Insira uma frase para verificação: ')).strip()
palavra = p1.upper()
count = len(palavra) - palavra.count(' ')
ns = ''
rev = ''
for i in palavra:
    if i != ' ':
        ns += i
for i in range(count-1,-1,-1):
    rev += ns[i]
if ns == rev:
    print('A palavra "{}" É um palíndromo.'.format(p1))
else:
    print('A palavra "{}" NÃO É um palíndromo.'.format(p1))