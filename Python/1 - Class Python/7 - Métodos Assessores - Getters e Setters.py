class Retangulo:

    def __init__(self, largura, altura):
        self.largura = 0
        self.altura = 0
        self.set_altura(altura)
        self.set_largura(largura)

    def set_altura(self, num):
        condition = isinstance(num, int) and (num > 0)
        if not condition:
            raise ValueError(f"Altura must be an integer: {num}")
        self.altura = num

    def set_largura(self, num):
        condition = isinstance(num, int) and (num > 0)
        if not condition:
            raise ValueError(f"Largura must be an integer: {num}")
        self.largura = num

    def get_area(self):
        return self.largura * self.altura

# r = Retangulo(largura=10, altura=5)
r = Retangulo(largura="10", altura=-5)