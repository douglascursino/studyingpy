nota1 = float(input("Entre com a primeira nota:"))
nota2 = float(input("Entre com a segunda nota:"))
nota3 = float(input("Entre com a terceira nota:"))
nota4 = float(input("Entre com a quarta nota:"))

media = (nota1 + nota2 + nota3 + nota4) / 4

if media >= 7.0:
    print("Parabéns, você foi aprovado!")

elif media >= 5.0:
    print("Você está de recuperação, ainda tem chance!")

else:
    print("Infelizmente você foi reprovado!")

print("Sua média é:", media)    
