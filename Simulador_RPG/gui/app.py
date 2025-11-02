import customtkinter as ctk
from utils.juego import Juego
from gui.crear_personaje_frame import CrearPersonajeFrame
from gui.listar_personajes_frame import ListarPersonajesFrame
from gui.batalla_frame import BatallaFrame

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")
        self.title("Simulador RPG")
        self.geometry("900x600")


        self.juego = Juego()
        self.juego.cargar_personajes()

        # Frame de contenedor principal
        self.container = ctk.CTkFrame(self)
        self.container.pack(fill="both", expand=True)

        self.frames = {}

        for F in (CrearPersonajeFrame, ListarPersonajesFrame, BatallaFrame):
            frame = F(self.container, self, self.juego)
            self.frames[F.__name__] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        # Menú superior moderno
        self.menu = ctk.CTkFrame(self, height=50, corner_radius=0)
        self.menu.pack(side="top", fill="x")

        ctk.CTkButton(self.menu, text="Crear Personaje", width=200, command=lambda: self.mostrar_frame("CrearPersonajeFrame")).pack(side="left", padx=10, pady=10)
        ctk.CTkButton(self.menu, text="Ver Personajes", width=200, command=lambda: self.mostrar_frame("ListarPersonajesFrame")).pack(side="left", padx=10, pady=10)
        ctk.CTkButton(self.menu, text="Combatir", width=200, command=lambda: self.mostrar_frame("BatallaFrame")).pack(side="left", padx=10, pady=10)

        self.mostrar_frame("CrearPersonajeFrame")

    def mostrar_frame(self, nombre):
        frame = self.frames[nombre]
        frame.tkraise()

    def run(self):
        self.mainloop()
