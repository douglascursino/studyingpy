x = int(input("Digite o primeiro número:"))
y = int(input("Digite o segundo número:"))
z = int(input("Digite o terceiro número:"))

if x>y and x>z:
   result = "x é o maior número"

elif y>x and y>z:
   result = "y é o maior número"

elif z>x and z>z:
   result = "z é o maior número"

elif x==y and x==z and y==x and y==z and z==x and z==y:  
   result = "todos numeros são iguais"  

print(result) 
