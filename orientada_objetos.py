class auto():
    def __init__(self,portas=0):
        self.portas = portas

    def setPortas(self, a):
        if a == "SIM":
            self.portas = 4
        else:
            self.portas = 2
    def getPortas (self):
        return self.portas

a = input("Possui portas, SIM ou NÃO?").upper()
novo = auto()
novo.setPortas(a)
print ("O número total de pneus é: " + str(novo.getPortas()))
