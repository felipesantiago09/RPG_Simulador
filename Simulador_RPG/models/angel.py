from models.personaje import Personaje

class Angel(Personaje):
    def __init__(self, nombre):
        super().__init__(nombre, "Ángel", vida=110, fuerza=15, defensa=10, poder_especial="Curación celestial")

    def atacar(self, enemigo):
        danio = self.fuerza - enemigo.defensa
        if danio < 0:
            danio = 0
        enemigo.vida -= danio
        self.vida += 5
        print(f"{self.nombre} ataca causando {danio} de daño y se cura ligeramente (+5 vida).")
