import random
class Personaje:
    def __init__(self, nombre, tipo, vida, fuerza, defensa, poder_especial):
        self.nombre = nombre
        self.tipo = tipo
        self.vida_max = vida
        self.vida = vida
        self.fuerza = fuerza
        self.defensa = defensa
        self.poder_especial = poder_especial

    def atacar(self, enemigo):
        danio = int((self.fuerza - enemigo.defensa) / 2)
        danio += random.randint(-2, 2)
        if danio < 0:
            danio = 0
        enemigo.vida -= danio
        if enemigo.vida < 0:
            enemigo.vida = 0
        print(
            f"{self.nombre} ataca a {enemigo.nombre} y causa {danio} de daño. Vida restante de {enemigo.nombre}: {enemigo.vida}")

    def esta_vivo(self):
        return self.vida > 0


    def __str__(self):
        return f"{self.tipo} {self.nombre} - Vida: {self.vida}/{self.vida_max}, Fuerza: {self.fuerza}, Defensa: {self.defensa}"

