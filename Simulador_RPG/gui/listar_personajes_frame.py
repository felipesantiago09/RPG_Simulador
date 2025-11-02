import customtkinter as ctk
from tkinter import messagebox

class ListarPersonajesFrame(ctk.CTkFrame):
    def __init__(self, parent, controller, juego):
        super().__init__(parent)
        self.controller = controller
        self.juego = juego

        ctk.CTkLabel(self, text="PERSONAJES REGISTRADOS", font=("Arial", 24, "bold")).pack(pady=30)

        self.text_box = ctk.CTkTextbox(self, width=700, height=400, font=("Consolas", 14))
        self.text_box.pack(pady=10)

        ctk.CTkButton(self, text="Actualizar lista", width=200, command=self.actualizar_lista).pack(pady=10)

    def actualizar_lista(self):
        self.text_box.delete("1.0", "end")

        if not self.juego.personajes:
            messagebox.showinfo("Información", "No hay personajes creados aún.")
            return

        for p in self.juego.personajes:
            info = (f"Nombre: {p.nombre}\n"
                    f"Tipo: {p.tipo}\n"
                    f"Vida: {p.vida}  |  Fuerza: {p.fuerza}  |  Defensa: {p.defensa}\n"
                    f"Poder Especial: {p.poder_especial}\n"
                    "-------------------------------------------\n")
            self.text_box.insert("end", info)

