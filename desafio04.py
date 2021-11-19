entrada = input("Digite Algo:")
print("Esta variável é do tipo", type(entrada))

print("Esta entrada é Alfanumérica?",entrada.isalnum())
print("Esta entrada é uma string de apenas letras?",entrada.isalpha())
print("Esta entrada é um Número?",entrada.isnumeric())
print("Esta entrada é em caixa alta?",entrada.isupper())
print("Esta entrada é caixa baixa?",entrada.islower())
print("Esta entrada é Capitalizada?",entrada.istitle())