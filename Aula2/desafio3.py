# Leia dois números

numero1 = int(input("Entre com o primeiro número:"))
numero2 = int(input("Entre com o segundo número:"))
numero3 = int(input("Entre com o terceiro número:"))

#Escolha o maior

maior_numero = numero1

if numero2 > maior_numero:
    maior_numero = numero2

if numero3 > maior_numero:
    maior_numero = numero3
    1
# Imprima o resultado
print("O maior numero é:", maior_numero)    