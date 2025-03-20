numeros = input("Digite uma lista de números separados por espaço: ")
numeros = [int(n) for n in numeros.split()]

numeros_sem_duplicatas = list(set(numeros))

for num in numeros_sem_duplicatas:
    print(num)