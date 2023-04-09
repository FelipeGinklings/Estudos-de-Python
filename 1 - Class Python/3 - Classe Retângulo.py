class Retângulo:
    
    def __init__(self):
        self.largura = 0
        self.altura = 0
        
    def area(self):
        return self.largura * self.altura
        
r1 = Retângulo()
r2 = Retângulo()
r3 = Retângulo()

print(r1.area())