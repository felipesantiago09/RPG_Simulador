import customtkinter as ctk
from tkinter import messagebox

class CrearPersonajeFrame(ctk.CTkFrame):
    def __init__(self, parent, controller, juego):
        super().__init__(parent)
        self.controller = controller
        self.juego = juego

        ctk.CTkLabel(self, text="CREAR PERSONAJE", font=("Arial", 24, "bold")).pack(pady=30)

        self.nombre_entry = ctk.CTkEntry(self, placeholder_text="Nombre del personaje", width=300)
        self.nombre_entry.pack(pady=10)

        ctk.CTkLabel(self, text="Tipo de personaje:").pack(pady=5)
        self.tipo_var = ctk.StringVar()
        self.tipo_combobox = ctk.CTkComboBox(self, variable=self.tipo_var, width=300,
                                             values=["guerrero", "mago", "arquero", "demonio", "angel"])
        self.tipo_combobox.pack(pady=10)

        ctk.CTkButton(self, text="Crear Personaje", width=200, height=40, command=self.crear_personaje).pack(pady=20)

    def crear_personaje(self):
        nombre = self.nombre_entry.get().strip()
        tipo = self.tipo_var.get().strip().lower()

        try:
            if not nombre:
                raise ValueError("El nombre no puede estar vacío.")
            if not tipo:
                raise ValueError("Debe seleccionar un tipo de personaje.")

            self.juego.crear_personaje(nombre, tipo)
            messagebox.showinfo("Éxito", f"Personaje '{nombre}' creado correctamente.")
            self.nombre_entry.delete(0, "end")
            self.tipo_combobox.set("")

        except ValueError as e:
            messagebox.showerror("Error", str(e))
