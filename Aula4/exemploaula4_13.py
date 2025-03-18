#1 - Ler um valor inteiro (aceitar somente valores entre 1 e 10) e escrever a tabuada de 1 a 10 do valor lido.
import random
secret_number = random.randint(1,2)
x = int(input("Entre com o número: "))

if secret_number == x:
    print("Acertou o número")
else:
    print("Errou o número")    

    