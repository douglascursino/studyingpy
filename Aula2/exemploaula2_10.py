x = int(input("Digite o primeiro número:"))
y = int(input("Digite o segundo número:"))
z = int(input("Digite o terceiro número:"))

if x>(y+z):
   print("X é maior que a soma de Y,Z")

elif y>(x+z):
   print("Y é maior que a soma de X,Z")

elif z>(x+y):
   print("Z é maior que a soma de X,y")

else:
   print("Não existe numero maior que a soma de outros dois numeros")

