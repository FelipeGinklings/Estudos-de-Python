class Retângulo:
    
    def __init__(self):
        self.largura = 0
        self.altura = 0
        
    def area(self):
        return self.largura * self.altura
        
r1 = Retângulo()
r1.largura = 5
r1.altura = 6

print(r1.area())