from models.personaje import Personaje

class Demonio(Personaje):
    def __init__(self, nombre):
        super().__init__(nombre, "Demonio", vida=130, fuerza=18, defensa=12, poder_especial="Absorción de vida")

    def atacar(self, enemigo):
        danio = (self.fuerza * 1.1) - enemigo.defensa
        if danio < 0:
            danio = 0
        enemigo.vida -= danio
        self.vida += danio * 0.3
        print(f"{self.nombre} absorbe la energía de {enemigo.nombre} y causa {danio} de daño, recuperando algo de vida.")

