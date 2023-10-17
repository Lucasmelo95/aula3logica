palavra = str(input("Digite uma palavra:")).lower()

tem_vogais = False
quantidade = 0 

for letra in palavra:
    if letra in "aeiou":
        tem_vogais = True
        quantidade = quantidade + 1
print(f"Sua palavra tem {quantidade} vogais ")



