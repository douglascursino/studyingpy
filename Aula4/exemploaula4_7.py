numero = 55
for i in range(2,numero):
    if numero % i == 0:
        print(numero, "não é número primo.")
        break
else:
         print(numero, "é um número primo.")    