#3 - Faça um programa que peça ao usuário para digitar uma sequência de números inteiros.
#O programa deve imprimir a soma dos números digitados, mas parar a soma se o usuário digitar um número negativo.

x = int(input("Entre com o primeiro número: "))
y = int(input("Entre com o segundo número: "))
z = int(input("Entre com o terceiro número: "))

if x<0 or y<0 or z<0:
    print(x+y+z)
else:
    print("não soma")    