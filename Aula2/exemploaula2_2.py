ano_atual = int(input("Digite o ano atual: "))
ano_nascimento = int(input("Digite o ano de nascimento: "))
idade = ano_atual - ano_nascimento

if idade >= 16:
    print("Vocé já pode votar esse ano")
else:
    print("Vocé ainda não pode votar esse ano")    