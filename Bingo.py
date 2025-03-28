import random
from Carton import Carton


class Bingo:
    def __init__(self, cartones: list[Carton]):
        self.cartones = cartones
        self.cantadas = []

    def cantar_ficha(self):
        ficha,letra = self.sacar_ficha()
        print("Ficha:", letra+str(ficha))
        self.rellenar_cartones(letra,ficha)


    def rellenar_cartones(self, letra, ficha):
        ganadores = []
        for i in range(len(self.cartones)):
            self.cartones[i].marcar_carton(letra, ficha)
            if self.cartones[i].gano_carton_lleno():
                ganadores.append(i)
        return ganadores

    def sacar_ficha(self):
        while True:
            ficha = round(random.randint(1,75))

            if ficha >= 1 and ficha <= 15:
                letra = "B"
            elif ficha >= 16 and ficha <= 30:
                letra = "I"
            elif ficha >= 31 and ficha <= 45:
                letra = "N"
            elif ficha >= 46 and ficha <= 60:
                letra = "G"
            elif ficha >= 61 and ficha <= 75:
                letra = "O"

            if ficha not in self.cantadas:
                self.cantadas.append(ficha)
                return ficha, letra

bingo = Bingo([])

bingo.cantar_ficha()


