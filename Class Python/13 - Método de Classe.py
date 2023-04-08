class Bichos:
    qnt_bichos = 0

    def __init__(self):
        self.add_bicho()
        print("self: ",self.qnt_bichos)

    def __del__(self):
        self.del_bicho()
        print("self: ",self.qnt_bichos)

        if self.qnt_bichos == 0:
            print("All creatures are destroyed")

    @classmethod
    def add_bicho(cls): # type: ignore
        cls.qnt_bichos += 1
        print("cls: ",cls.qnt_bichos)

    @classmethod
    def del_bicho(cls): # type: ignore
        cls.qnt_bichos -= 1
        print("cls: ",cls.qnt_bichos)


b1 = Bichos()
b2 = Bichos()
b3 = Bichos()
print(Bichos.qnt_bichos)    

# del(b1)
# print(Bichos.qnt_bichos)
# del(b2)
# print(Bichos.qnt_bichos)
# del(b3)
# print(Bichos.qnt_bichos)
