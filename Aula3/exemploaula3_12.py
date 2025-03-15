tentativas = 0
senha1 = input("Crie sua senha: ")
print("Bem vindo á XLabs")
while tentativas < 3:
    senha2 = input("Digite a senha: ")
    if senha2 == senha1:
        print("Acesso concedido")
        break
    else:
        print("Senha incorreta. Tenta novamente.")
        tentativas +=1
else:
    print("Você excedeu o número máximo de tentativas.")        
