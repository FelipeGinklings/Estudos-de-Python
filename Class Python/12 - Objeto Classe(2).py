# class MinhaClasse:
#     membro_cls = 50
    
#     def __init__(self):
#         self.membro_inst = -10
    
#     def func(self):
#         print(self.membro_inst)
#         print(self.membro_cls)
#         print(MinhaClasse.membro_cls)
#         # print("The method func() is called")

# i1 = MinhaClasse()
# i2 = MinhaClasse()

# print(MinhaClasse.membro_cls)
# print(i1.membro_cls)
# print(i2.membro_cls)

# print("-"*15)

# i1.membro_cls = 1000
# # MinhaClasse.membro_cls = 1000
# print(MinhaClasse.membro_cls)
# print(i1.membro_cls) # Membro de Instância
# print(i2.membro_cls) # Membro de Classe

# i1.membro_inst = 10
# MinhaClasse.membro_inst = 10 Erro, não é possível alterar todos os membros de instância
# print("i1: ", i1.membro_inst)
# print("i2: ", i2.membro_inst)

# MinhaClasse.membro_cls = 9

# print("-"*15)
# print("i1: ", i1.membro_cls)
# print("i2: ", i2.membro_cls)


# i1.func()

# print(i1.membro_inst)
# print(i1.membro_cls)
# print(MinhaClasse.membro_cls)

# print(MinhaClasse.membro_cls)
# MinhaClasse.membro_cls = 10
# print(MinhaClasse.membro_cls)

class AAA:
    pass

bbb = AAA()

AAA.var_cls =  "AAA.var_cls"
bbb.var_inst = "bbb.var_inst"

bbb.var_cls = "bbb.var_cls"
print()