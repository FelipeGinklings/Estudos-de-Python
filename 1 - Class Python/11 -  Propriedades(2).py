# Builtins Property
"""
class Retangulo:

    def __init__(self, largura, altura):
        self._largura = 0
        self._altura = 0
        self._set_altura(altura)
        self._set_largura(largura)

    def _get_altura(self):
        return self._altura

    def _set_altura(self, num):
        condition = isinstance(num, int) and (num > 0)
        if not condition:
            raise ValueError(f"Altura must be an integer: {num}")
        self._altura = num

    def _get_largura(self):
        return self._largura

    def _set_largura(self, num):
        condition = isinstance(num, int) and (num > 0)
        if not condition:
            raise ValueError(f"Largura must be an integer: {num}")
        self._largura = num

    def _get_area(self):
        return self._largura * self._altura

    altura = property(fget=_get_altura, fset=_set_altura)
    largura = property(fget=_get_largura, fset=_set_largura)
    area = property(fget=_get_area)


r = Retangulo(largura=5, altura=5)
r.largura = 10
r.altura = 15
r.area = 1000
print(r.altura)
print(r.largura)
print()
"""

# Decorators #


class Retangulo:

    def __init__(self, largura, altura):
        self._largura = 0
        self._altura = 0
        self.altura = altura
        self.largura = largura

    @property
    def altura(self):
        return self._altura

    @altura.setter
    def altura(self, num):
        condition = isinstance(num, int) and (num > 0)
        if not condition:
            raise ValueError(f"Altura must be an integer: {num}")
        self._altura = num

    @property
    def largura(self):
        return self._largura

    @largura.setter
    def largura(self, num):
        condition = isinstance(num, int) and (num > 0)
        if not condition:
            raise ValueError(f"Largura must be an integer: {num}")
        self._largura = num

    @property
    def area(self):
        return self._largura * self._altura


r = Retangulo(largura=5, altura=5)
r.largura = 10
r.altura = 15
# r.area = 1000
print(r.altura)
print(r.largura)
print(r.area)
print()