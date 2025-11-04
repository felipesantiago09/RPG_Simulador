from models.personaje import Personaje
import random

class Arquero(Personaje):
    def __init__(self, nombre):
        super().__init__(nombre, "Arquero", vida=100, fuerza=20, defensa=8, poder_especial="Flecha precisa")

    def atacar(self, enemigo):
        acierto = random.random()
        if acierto < 0.3:
            print(f"{self.nombre} falló el tiro.")
            return
        danio = (self.fuerza * 1.1) - enemigo.defensa
        if danio < 0:
            danio = 0
        enemigo.vida -= danio
        print(f"{self.nombre} dispara una flecha precisa causando {danio} de daño.")
