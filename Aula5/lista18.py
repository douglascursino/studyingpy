#Escreva um programa que peça ao usuário para digitar uma lista de números e, em seguida, encontre o número máximo e o número mínimo da lista.


entrada = input("Digite uma lista de números separados por espaço: ")


lista_numeros = [int(num) for num in entrada.split()]

max = max(lista_numeros)
min = min(lista_numeros)

print(max,min)