def funcao_detecta(n):
    if(n % 2 == 0):
       return "É Par"
    else:
        return "É Impar"
    
print(funcao_detecta(int(input("Entre com o número: "))))   