class Retângulo:

    def area(self):
        return self.l * self.a

def membros_retângulo(r):
    r.l = 0
    r.a = 0

r1 = Retângulo()
membros_retângulo(r1)
r1.l = 5
r1.a = 6

print(r1.area())
