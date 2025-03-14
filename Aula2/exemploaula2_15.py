idade = int(input("Digite sua idade:"))
estudante = bool(input("É estudante digite 0 para não e 1 para sim:"))
aposentado = bool(input("É aposentado digite 0 para não e 1 para sim:"))
dia_semana = bool(input("Hoje não é segunda: "))



if idade <=20 or estudante or aposentado or dia_semana:
    print("Você possui desconto")       

else:
    print("Você não possui desconto")       
