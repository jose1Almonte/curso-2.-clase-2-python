import random
import time
from Carton import Carton


class Bingo:
    def __init__(self, cartones: list[Carton]):
        self.cartones = cartones
        self.cantadas = []

    def cantar_ficha(self) -> list[Carton]:
        ficha,letra = self._sacar_ficha()
        print("Ficha:", letra+str(ficha))
        cartones_ganadores = self._rellenar_cartones(letra,ficha)

        return cartones_ganadores

    def mostrar_cartones_actuales(self):
        for carton in self.cartones:
            carton.show_card(True)

    def _rellenar_cartones(self, letra, ficha):
        ganadores = []
        for i in range(len(self.cartones)):
            self.cartones[i].marcar_carton(letra, ficha)
            if self.cartones[i].gano_carton_lleno()[0]:
                ganadores.append(self.cartones[i].id)
        return ganadores

    def _sacar_ficha(self):
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



ids = []
cartones = []
carton = Carton(ids)
carton2 = Carton(ids)
carton3 = Carton(ids)
carton4 = Carton(ids)
cartones.append(carton)
cartones.append(carton2)
cartones.append(carton3)
# cartones.append(carton3)
# cartones.append(carton4)

bingo = Bingo(cartones)

while True:

    bingo.mostrar_cartones_actuales()
    cartones_ganadores = bingo.cantar_ficha()
    input()

    if len(cartones_ganadores) > 0:
        
        for carton_ganador in cartones:
            carton_ganador: Carton
            if carton_ganador.id == cartones_ganadores[0]:
                carton_ganador.show_card(False)
                               
        break


