#Você pode usar While ou For.

#0 - Peça para  o usuário entrar com dois valores (primeiro e último).
#Faça a contagem entre esses números.
#Caso o último for menor que  o primeiro faça a contagem decrescente.
#Caso o último número for maior que o primeiro faça a contagem crescente.

x = int(input("Entre com o primeiro número: "))
y = int(input("Entre com o segundo número: "))

if x > y:
   for i in range(x,y-1,-1):
    print(i)
else:
    for i in range(x,y):
       print(i)
    