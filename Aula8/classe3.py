# para __init__ o primeiro item é usado como referencia
class Pessoa:
    def __init__(self, name, age): # __init__ é com dois underlines de cada lado
        self.name = name
        self.age = age
        
    def apresentar(self):
        print(f"Olá, meu nome é {self.name} e \
              tenho {self.age} anos.")

# Uso da classe
pessoa1 = Pessoa("João", 30)
pessoa1.apresentar()