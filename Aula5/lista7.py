# Criando uma lista de números
numeros = [10, 20, 30, 40, 50]

soma = sum(numeros)
min = min(numeros)
max = max(numeros)
ordenado = sorted(numeros)
numeros.sort()

# Imprimindo o resultado
print("A soma dos números na lista é:", soma)
print("Menor valor:", min)
print("Maior valor:", max)
print("Lista ordenada:", ordenado)
print("Lista ordenada:", numeros)
numeros.sort(reverse=True)
print("Lista ordenada:", numeros)