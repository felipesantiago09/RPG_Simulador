import random

class Batalla:
    def __init__(self, personaje1, personaje2):
        self.p1 = personaje1
        self.p2 = personaje2

    def iniciar(self):
        print(f"\n🗡️ Batalla entre {self.p1._nombre} ({self.p1._tipo}) y {self.p2._nombre} ({self.p2._tipo})")

        atacante = self.p1
        defensor = self.p2

        while self.p1.esta_vivo() and self.p2.esta_vivo():
            # 30% de probabilidad de usar habilidad especial
            if random.random() < 0.3:
                atacante.habilidad_especial(defensor)
            else:
                atacante.atacar(defensor)

            if not defensor.esta_vivo():
                print(f"\n🏆 {atacante._nombre} ha derrotado a {defensor._nombre}!\n")
                break

            # Cambiar de turno
            atacante, defensor = defensor, atacante
