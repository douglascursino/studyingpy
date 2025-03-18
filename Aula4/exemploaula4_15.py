#4 - Faça um programa que peça ao usuário para digitar o número de vezes que ele quer jogar uma moeda.
#O programa deve simular o lançamento de uma moeda e imprimir o resultado de cada lançamento (cara ou coroa).
#No final, o programa deve imprimir o número total de caras e o número total de coroas.
#Use a biblioteca abaixo para números aleatórios:

import random

x = int(input("Quantas vezes quer jogar a moeda:"))

for i in range(1,x+1):
    if (random.randint(1,2))%2==0:
     print(i, "tentativa=","Cara")
    else:
       print(i, "tentativa=","Coroa") 