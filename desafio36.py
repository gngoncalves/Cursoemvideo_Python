print('\033[7m-=\033[m'*16)
print('\033[41mPrograma aprovador de empréstimo\033[m')
print('\033[7m-=\033[m'*16)
imovel = float(input('Favor inserir o valor do imóvel a ser comprado: R$ '))
salario = float(input('Favor inserir o valor do salário do cliente: R$ '))
anos = int(input('Favor inserir a quantidade de anos para pagamento: '))
prestacao = imovel / (anos*12)
print('O imóvel desejado custa R$ {:.2f}, e a prestação será de R${:.2f}, durante {} anos.'.format(imovel,prestacao,anos))
if prestacao <= salario * 30/100:
    print('\033[1;32mSeu empréstimo foi aprovado!\033[m')
else:
    print('\033[1;31mInfelizmente, o seu empréstimo não pode ser aprovado.\033[m')
print('\nAnálise Finalizada.\nObrigado!')