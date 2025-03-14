idade = int(input("Digite sua idade: "))
cliente_fiel = input("Digite True ou False: ")

if idade < 18 or cliente_fiel == True:
    print("Desconto aplicável")
else:
    print("Sem desconto")      