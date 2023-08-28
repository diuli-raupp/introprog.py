class IntSet:

    def __init__(self, numero):
        self.vals = []
        self.numero = numero

    def func(self):
        if self.numero in self.vals:
            pass
        else:
            (self.vals).append(self.numero)
    
    def isNumber(self):
        try:
            int(self.numero)
        except Exception:
            return False
        else:
            return True
        return isNumber
    
    def func2(self):
        print("Conjunto de inteiros:")
        print(self.vals)
    
algarismo = input()
variavel = IntSet(algarismo)
if variavel.isNumber():
    variavel.func()

while algarismo != "sair":
    algarismo = input()
    if algarismo == "sair":
        variavel.func2()
    if variavel.isNumber():
        variavel.func()
