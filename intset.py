class IntSet:

    def __init__(self):
        self.vals = []

    def func(self, numero):
        if numero in self.vals:
            pass
        else:
            (self.vals).append(numero)
    
    def isNumber(self, numero):
        try:
            int(numero)
        except Exception:
            return False
        else:
            return True

    def func2(self):
        print("Conjunto de inteiros:")
        print(self.vals)
    
algarismo = input()
variavel = IntSet()
if variavel.isNumber(algarismo):
    variavel.func(algarismo)

while algarismo != "sair":
    algarismo = input()
    if algarismo == "sair":
        variavel.func2()
    if variavel.isNumber(algarismo):
        variavel.func(algarismo)
