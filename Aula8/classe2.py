# para __init__ o primeiro item é usado como referencia
class Pessoa:
    def __init__(self, name, age): # __init__ é com dois underlines de cada lado
        self.name = name
        self.age = age
        
nome1 = Pessoa("Joaquina", 99) 

print(nome1.name)
print(nome1.age)