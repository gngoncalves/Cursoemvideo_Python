peso = float(input('Insira o seu peso: '))
altura = float(input('Insira a sua altura (em metros): '))

imc = peso / (altura ** 2)

if imc < 18.5:
    print('O seu IMC é de {:.1f}. Segundo a tabela do IMC, você está abaixo do peso.'.format(imc))
elif imc >= 18.5 and imc < 25:
    print('O seu IMC é de {:.1f}. Segundo a tabela do IMC, você está no seu peso ideal.'.format(imc))
elif imc >= 25 and imc < 30:
    print('O seu IMC é de {:.1f}. Segundo a tabela do IMC, você está com sobrepeso.'.format(imc))
elif imc >= 30 and imc < 40:
    print('O seu IMC é de {:.1f}. Segundo a tabela do IMC, você está com obesidade.'.format(imc))
else:
    print('O seu IMC é de {:.1f}. Segundo a tabela do IMC, você está com obesidade mórbida.'.format(imc))
