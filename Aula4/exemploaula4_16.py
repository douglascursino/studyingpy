#5 - Faça um programa que simule a urna eletrônica.
#A tela a ser apresentada deverá ser da seguinte forma:
#As opcoes sao:
#1. Candidato Jair Rodrigues
#2. Candidato Carlos Luz
#3. Candidato Neves Rocha
#4. Nulo
#5. Branco
#Entre com o seu voto:
#O programa deverá ler os votos dos eleitores e, quando for entrado o número 6, apresentar as seguintes
#informações:
#a) O número de votos de cada candidato;
#b) A porcentagem de votos nulos;
#c) A porcentagem de votos brancos;
#d) O candidato vencedor.

# Inicializa as variáveis para contar os votos de cada candidato e os votos nulos e brancos
votos_jair_rodrigues = 0
votos_carlos_luz = 0
votos_neves_rocha = 0
votos_nulos = 0
votos_brancos = 0
total_votos = 0

# Loop para receber os votos dos eleitores
while True:
    print("\nAs opcoes sao:")
    print("1. Candidato Jair Rodrigues")
    print("2. Candidato Carlos Luz")
    print("3. Candidato Neves Rocha")
    print("4. Nulo")
    print("5. Branco")
    print("6. Encerrar votação")
    
    # Solicita ao eleitor para entrar com o voto
    voto = int(input("Entre com o seu voto: "))
    
    # Verifica se o eleitor deseja encerrar a votação
    if voto == 6:
        break
    
    # Atualiza as contagens de votos de acordo com a escolha do eleitor
    if voto == 1:
        votos_jair_rodrigues += 1
    elif voto == 2:
        votos_carlos_luz += 1
    elif voto == 3:
        votos_neves_rocha += 1
    elif voto == 4:
        votos_nulos += 1
    elif voto == 5:
        votos_brancos += 1
    else:
        print("Opção inválida. Voto não computado.")

    # Incrementa o total de votos
    total_votos += 1

# Calcula as porcentagens
if total_votos > 0:
    porcentagem_nulos = (votos_nulos / total_votos) * 100
    porcentagem_brancos = (votos_brancos / total_votos) * 100
else:
    porcentagem_nulos = 0
    porcentagem_brancos = 0

# Determina o candidato vencedor
vencedor = max(votos_jair_rodrigues, votos_carlos_luz, votos_neves_rocha)

# Imprime os resultados
print("\nResultados da votação:")
print("Votos para Jair Rodrigues:", votos_jair_rodrigues)
print("Votos para Carlos Luz:", votos_carlos_luz)
print("Votos para Neves Rocha:", votos_neves_rocha)
print("Votos Nulos:", votos_nulos)
print("Votos em Branco:", votos_brancos)
print("Porcentagem de votos nulos: {:.2f}%".format(porcentagem_nulos))
print("Porcentagem de votos em branco: {:.2f}%".format(porcentagem_brancos))

# Determina e imprime o candidato vencedor
if vencedor == votos_jair_rodrigues:
    print("Candidato Vencedor: Jair Rodrigues")
elif vencedor == votos_carlos_luz:
    print("Candidato Vencedor: Carlos Luz")
else:
    print("Candidato Vencedor: Neves Rocha")