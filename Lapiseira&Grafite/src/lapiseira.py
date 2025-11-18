from src.grafite import Grafite

class Lapiseira:

    def __init__(self, calibre:float):
        self.calibre = calibre
        self.grafites = None
        self.folhasEscritas = 0

    def inserir (self, grafite: Grafite):
        if self.calibre == grafite.calibre and self.getGrafite() == None:
            self.grafites = grafite
            self.folhasEscritas = 0
            return True
        return False

    def remover(self):
        if self.getGrafite() != None:
            self.grafites = None
            return True
        return False

    def escrever(self, folhas: int):
        if self.grafites == None:
            return False

        grafite = self.getGrafite()
        desgasteF = grafite.desgastePorFolha()
        tamanho = grafite.getTamanho()

        if self.getGrafite() != None:
            folhasPossiveis = (tamanho-(tamanho%desgasteF))/desgasteF

            if folhasPossiveis >= folhas+self.folhasEscritas:
                self.folhasEscritas += folhas
                tamanho = tamanho-(folhas*desgasteF)

                if tamanho == 0:
                    self.grafites = None
                else:
                    self.grafites = grafite
                return True
            else:
                self.folhasEscritas += folhas
                self.folhasEscritas -= self.folhasEscritas - folhasPossiveis
                self.grafites = None

    def getGrafite(self):
        return self.grafites

    def getCalibre(self):
        return self.calibre

    def getFolhasEscritas(self):
        return self.folhasEscritas