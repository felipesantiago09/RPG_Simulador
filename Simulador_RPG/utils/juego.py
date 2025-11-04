import json
from models.guerrero import Guerrero
from models.mago import Mago
from models.arquero import Arquero
from models.demonio import Demonio
from models.angel import Angel

class Juego:
    def __init__(self):
        self.personajes = []
        self.cargar_personajes()

    def crear_personaje(self, nombre, tipo):
        tipos = {
            "guerrero": Guerrero,
            "mago": Mago,
            "arquero": Arquero,
            "demonio": Demonio,
            "angel": Angel
        }

        tipo = tipo.strip().lower()



        for p in self.personajes:
            if p.nombre == nombre:
                raise ValueError("Ya existe un personaje con ese nombre.")


        if tipo not in tipos:
            raise ValueError("Tipo de personaje no válido.")


        personaje = tipos[tipo](nombre)
        self.personajes.append(personaje)
        self.guardar_personajes()

    def guardar_personajes(self):

        datos = []
        for p in self.personajes:
            datos.append({
                "nombre": p.nombre,
                "tipo": p.tipo,
                "vida": p.vida,
                "fuerza": p.fuerza,
                "defensa": p.defensa,
                "poder_especial": p.poder_especial
            })

        with open("personajes.json", "w", encoding="utf-8") as f:
            json.dump(datos, f, indent=4, ensure_ascii=False)

    def cargar_personajes(self):
        """Carga los personajes desde el archivo JSON"""
        try:
            with open("personajes.json", "r", encoding="utf-8") as f:
                datos = json.load(f)
                self.personajes = []

                for d in datos:
                    tipo = d["tipo"].lower()
                    if tipo == "guerrero":
                        p = Guerrero(d["nombre"])
                    elif tipo == "mago":
                        p = Mago(d["nombre"])
                    elif tipo == "arquero":
                        p = Arquero(d["nombre"])
                    elif tipo == "demonio":
                        p = Demonio(d["nombre"])
                    elif tipo == "angel":
                        p = Angel(d["nombre"])
                    else:
                        print(f"Tipo de personaje desconocido: {tipo}. Se omitió este registro.")

                    # Restaurar los valores guardados
                    p.vida = d["vida"]
                    p.fuerza = d["fuerza"]
                    p.defensa = d["defensa"]
                    p.poder_especial = d["poder_especial"]

                    self.personajes.append(p)

        except FileNotFoundError:
            self.personajes = []
