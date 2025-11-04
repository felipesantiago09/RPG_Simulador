from models.personaje import Personaje

class Mago(Personaje):
    def __init__(self, nombre):
        super().__init__(nombre, "Mago", vida=80, fuerza=15, defensa=5, poder_especial="Hechizo de fuego")

    def atacar(self, enemigo):
        danio = (self.fuerza * 1.5) - enemigo.defensa
        if danio < 0:
            danio = 0
        enemigo.vida -= danio
        print(f"{self.nombre} lanza un hechizo de fuego y causa {danio} de daño.")

