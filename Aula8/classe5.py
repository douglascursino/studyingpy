class Motor:
    def ligar(self):
        print("Motor ligado.")
    def desligar(self):
        print("Motor desligado.")

class Carro:
    def __init__ (self):
        self.motor = Motor()
    def ligar_carro(self):
        self.motor.ligar()
    def desligar_carro(self):
        self.motor.desligar()

# Uso das classes
meu_carro = Carro()
meu_carro.ligar_carro()
meu_carro.desligar_carro()                 

