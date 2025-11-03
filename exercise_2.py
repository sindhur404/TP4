class rectangle:
    def __init__ (self,Base,Hauteur):
        self.Base = Base
        self.Hauteur = Hauteur
    def calcul_aire(self):
        print(self.Base * self.Hauteur)

answer=rectangle(5,6)
answer.calcul_aire()
