# gui/batalla_frame.py
import customtkinter as ctk
from tkinter import messagebox
import random
import time


class BatallaFrame(ctk.CTkFrame):
    def __init__(self, parent, controller, juego):
        super().__init__(parent)
        self.controller = controller
        self.juego = juego

        ctk.CTkLabel(self, text="⚔️  SIMULAR BATALLA RPG  ⚔️", font=("Arial", 24, "bold")).pack(pady=20)

        self.p1_var = ctk.StringVar()
        self.p2_var = ctk.StringVar()

        ctk.CTkLabel(self, text="Selecciona el primer combatiente:").pack()
        self.p1_combo = ctk.CTkComboBox(self, variable=self.p1_var, width=300)
        self.p1_combo.pack(pady=5)

        ctk.CTkLabel(self, text="Selecciona el segundo combatiente:").pack()
        self.p2_combo = ctk.CTkComboBox(self, variable=self.p2_var, width=300)
        self.p2_combo.pack(pady=5)

        ctk.CTkButton(self, text="🔥 Iniciar Batalla 🔥", width=200, height=40, command=self.simular).pack(pady=15)

        # Marco para las barras de vida
        self.hp_frame = ctk.CTkFrame(self)
        self.hp_frame.pack(pady=10)

        # Etiquetas dinámicas con nombres
        self.hp1_label = ctk.CTkLabel(self.hp_frame, text="🗡️ Vida del Personaje 1")
        self.hp2_label = ctk.CTkLabel(self.hp_frame, text="🗡️ Vida del Personaje 2")
        self.hp1_label.grid(row=0, column=0, padx=15)
        self.hp2_label.grid(row=0, column=1, padx=15)

        self.hp1 = ctk.CTkProgressBar(self.hp_frame, width=300)
        self.hp1.grid(row=1, column=0, padx=15, pady=5)
        self.hp2 = ctk.CTkProgressBar(self.hp_frame, width=300)
        self.hp2.grid(row=1, column=1, padx=15, pady=5)

        self.text_box = ctk.CTkTextbox(self, width=780, height=320, font=("Consolas", 12))
        self.text_box.pack(pady=10)

    def simular(self):
        p1_name = self.p1_var.get()
        p2_name = self.p2_var.get()

        try:
            if len(self.juego.personajes) < 2:
                raise ValueError("Debe haber al menos dos personajes para combatir.")

            if not p1_name or not p2_name:
                raise ValueError("Debe seleccionar ambos personajes.")

            if p1_name == p2_name:
                raise ValueError("No puede seleccionar el mismo personaje dos veces.")

            p1 = next((p for p in self.juego.personajes if p.nombre == p1_name), None)
            p2 = next((p for p in self.juego.personajes if p.nombre == p2_name), None)

            if not p1 or not p2:
                raise ValueError("Uno de los personajes no existe.")

            # Restaurar vida máxima si alguno está muerto de antes
            p1.vida = p1.vida_max
            p2.vida = p2.vida_max

            # Actualizar etiquetas con nombres reales
            self.hp1_label.configure(text=f"🗡️ Vida de {p1.nombre}")
            self.hp2_label.configure(text=f"🗡️ Vida de {p2.nombre}")

            self.text_box.delete("1.0", "end")
            self.hp1.set(1)
            self.hp2.set(1)
            self.update()

            ataques = [
                "⚔️ asesta un golpe demoledor a",
                "🛡️ rompe la defensa de",
                "💥 desata un embate sobre",
                "🎯 golpea con precisión a",
                "🔥 abarca a su rival con un ataque",
                "💢 rompe la guardia de",
                "⚡ impacta con fuerza sobre",
                "⚔️ ataque relámpago dirigido a",
                "💀 golpea sin piedad a"
            ]

            turno = 1
            self.text_box.insert("end", f"🔥 ¡Comienza la batalla entre {p1.nombre} y {p2.nombre}! 🔥\n")

            while p1.esta_vivo() and p2.esta_vivo():
                self.text_box.insert("end", f"\n--- 🕐 Turno {turno} ---\n")

                # Turno 1
                frase = random.choice(ataques)
                self.text_box.insert("end", f"{p1.nombre} {frase} {p2.nombre} ⚔️\n")
                p1.atacar(p2)
                self.actualizar_vidas(p1, p2)
                self.update_text()
                if not p2.esta_vivo():
                    self.text_box.insert("end", f"💀 {p2.nombre} ha caído en combate.\n")
                    break

                # Turno 2
                frase = random.choice(ataques)
                self.text_box.insert("end", f"{p2.nombre} {frase} {p1.nombre} ⚡\n")
                p2.atacar(p1)
                self.actualizar_vidas(p1, p2)
                self.update_text()
                if not p1.esta_vivo():
                    self.text_box.insert("end", f"💀 {p1.nombre} ha sido derrotado.\n")
                    break

                turno += 1

            ganador = p1 if p1.esta_vivo() else p2
            self.text_box.insert("end", f"\n🏆 ¡{ganador.nombre.upper()} ({ganador.tipo}) SE CORONA CAMPEÓN! 🏆\n")
            self.text_box.insert("end", f"\n🔥 El campo de batalla queda en silencio... 🔥\n")

        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def actualizar_vidas(self, p1, p2):
        self.hp1.set(p1.vida / p1.vida_max if p1.vida_max else 0)
        self.hp2.set(p2.vida / p2.vida_max if p2.vida_max else 0)

    def update_text(self):
        self.text_box.see("end")
        self.update()
        time.sleep(0.4)

    def tkraise(self, aboveThis=None):
        super().tkraise(aboveThis)
        nombres = [p.nombre for p in self.juego.personajes]
        self.p1_combo.configure(values=nombres)
        self.p2_combo.configure(values=nombres)
