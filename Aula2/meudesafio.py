# Leia dois números

numero1 = int(input("Entre com o primeiro número:"))
numero2 = int(input("Entre com o segundo número:"))
numero3 = int(input("Entre com o terceiro número:"))
numero4 = int(input("Entre com o quarto número:"))

#Escolha o maior

if numero1 > numero2 and numero1 > numero3 and numero1 > numero4:
    maior_numero = numero1

elif numero2 > numero1 and numero2 > numero3 and numero2 > numero4:
    maior_numero = numero2

elif numero3 > numero1 and numero3 > numero2 and numero3 > numero4:
    maior_numero = numero3

else: 
    maior_numero = numero4   
   
# Imprima o resultado
print("O maior numero é:", maior_numero)    