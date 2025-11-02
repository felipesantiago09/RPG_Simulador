from models.personaje import Personaje

class Guerrero(Personaje):
    def __init__(self, nombre):
        super().__init__(nombre, "Guerrero", vida=120, fuerza=25, defensa=10, poder_especial="Golpe poderoso")

    def atacar(self, enemigo):
        danio = (self.fuerza * 1.2) - enemigo.defensa
        if danio < 0:
            danio = 0
        enemigo.vida -= danio
        print(f"{self.nombre} realiza un golpe poderoso causando {danio} de daño.")
