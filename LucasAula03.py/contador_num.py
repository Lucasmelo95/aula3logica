frase = str(input("aonde voce mora ?"))
quantidade = 0
tem_num = False

for num in frase:
    if num in "1234567890":
        tem_num = True
        quantidade = quantidade + 1

if tem_num == True:
    print(f"tem {quantidade} numeros")
else:
    print("Não possui numeros")

#frase = str(input("Digite uma frase:"))

#for num in frase:
#    if num in "0123456789":
#        print(f"Númewro encontrado:{num}")