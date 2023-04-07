class Retangulo:

    def __init__(self, largura, altura):
        self._largura = 0
        self._altura = 0
        self.__var = 0  # Colisão de nomes, desfigurado
        self.set_altura(altura)
        self.set_largura(largura)

    def set_altura(self, num):
        condition = isinstance(num, int) and (num > 0)
        if not condition:
            raise ValueError(f"Altura must be an integer: {num}")
        self._altura = num
        self.__var = 456

    def set_largura(self, num):
        condition = isinstance(num, int) and (num > 0)
        if not condition:
            raise ValueError(f"Largura must be an integer: {num}")
        self._largura = num

    def get_area(self):
        return self._largura * self._altura


# r = Retangulo(largura=10, altura=5)
# r = Retangulo(largura="10", altura=-5)
r = Retangulo(largura=10, altura=5)
r = Retangulo(largura=10, altura=5)
