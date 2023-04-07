class Retângulo:
    
    def __init__(self, largura, altura):
        self._l = largura
        self._a = altura
        
    def area(self):
        return self._l * self._a
        
r = Retângulo(10, 5)

# r.l = "teste"

print(r.area())