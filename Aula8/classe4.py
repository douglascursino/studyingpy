class Calculadora:
    def adicionar(self, a, b):
        return a+b
    
    def subtrair(self, a, b):
        return a-b
    
 # Uso de classe
calc = Calculadora()
print(calc.adicionar(10,5))
print(calc.subtrair(10,5))   