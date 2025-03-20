# Escreva um programa que peça ao usuário para digitar uma lista de números e, em seguida, imprima apenas os números pares da lista.
x = [1,2,3,4,5]

for i in x:
    if x % 2 == 0:
        print(i)


    
# Solicita ao usuário que digite uma lista de números
entrada = input("Digite uma lista de números separados por espaço: ")

# Converte a entrada em uma lista de números
lista_numeros = [int(num) for num in entrada.split()]

# Filtra e imprime os números pares
print("Números pares da lista:")
for numero in lista_numeros:
    if numero % 2 == 0:
        print(numero)