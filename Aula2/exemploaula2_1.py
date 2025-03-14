n1 = float(input("Entre com a primeira nota: "))
n2 = float(input("Entre com a segunda nota: "))
n3 = float(input("Entre com a terceira nota: "))
me = float(input("Digite a média dos exercícios: "))

ma = (n1 + n2*2 + n3*3 + me)/7

if ma >= 9:
    conceito = "A"
elif ma >= 7.5:
    conceito = "B"
elif ma >= 6:
    conceito = "C"
elif ma >=4:
    conceito = "D"
else:
    conceito = "E"
print("Média de aproveitamento: {:.2f}".format(ma))
print("Conceito:", conceito)                    