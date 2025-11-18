from src.dureza import Dureza


class Grafite:

    def __init__(self, calibre: float, dureza: Dureza, tamanho: int):
        self.calibre = calibre
        self.dureza = dureza
        self.tamanho = tamanho

    def desgastePorFolha(self):
        if self.dureza == Dureza.G_HB:
            return 1
        if self.dureza == Dureza.G_2B:
            return 2
        if self.dureza == Dureza.G_4B:
            return 4
        if self.dureza == Dureza.G_6B:
            return 6

    def getDureza(self):
        return self.dureza

    def getCalibre(self):
        return self.calibre

    def getTamanho(self):
        return self.tamanho

    def setTamanho(self, tamanho:int):
        self.tamanho = tamanho