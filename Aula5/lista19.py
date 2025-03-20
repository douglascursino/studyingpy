numeros = input("Digite uma lista de números separados por espaço: ")
numeros = [int(n) for n in numeros.split()]

media = sum(numeros) / len(numeros)

print(media)