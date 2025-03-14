from datetime import datetime

ano_atual = datetime.now().year
ano_nascimento = int(input("Digite o ano de nascimento: "))
idade = ano_atual - ano_nascimento

if idade >= 16:
    print("Vocé já pode votar esse ano")
else:
    print("Vocé ainda não pode votar esse ano")    