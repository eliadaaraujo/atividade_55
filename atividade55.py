# Peça ao usuário uma palavra e exiba-a invertida, sem usar [::-1].
# Dica: utilize um for percorrendo de trás para frente ou reversed().

palavra = input("Digite uma palavra: ")
invertida = ""
for letra in reversed(palavra):
    invertida += letra
print("Palavra invertida:", invertida)
