# 🧙‍♂️ Simulador RPG - Juego con Interfaz Gráfica

## 📖 Descripción General
El **Simulador RPG** es una aplicación desarrollada en **Python** que permite crear, gestionar y hacer combatir personajes de un videojuego de rol (RPG).  
Cada personaje pertenece a una clase (Guerrero, Mago, Arquero, Demonio o Ángel), con atributos y habilidades únicas que reflejan los principios de la **Programación Orientada a Objetos (POO)**, tales como herencia, polimorfismo, encapsulamiento y abstracción.

La interfaz gráfica fue implementada con **CustomTkinter**, ofreciendo un diseño moderno, intuitivo y atractivo.  
El usuario puede crear personajes, visualizar sus estadísticas y simular batallas con animaciones simples, emojis y barras de vida.

---

## ⚙️ Características Principales
- Creación de personajes con distintos tipos y atributos.  
- Visualización de todos los personajes registrados.  
- Simulación de combates automáticos por turnos.  
- Interfaz gráfica moderna y responsiva con `customtkinter`.  
- Persistencia de datos con archivo `JSON` para guardar y cargar personajes automáticamente.  
- Uso de polimorfismo para ataques y habilidades especiales.  

---

## 🧩 Instalación y Ejecución
1. Clona este repositorio:
   ```bash
   git clone https://github.com/felipesantiago09/RPG_Simulador.git
   ```
2. Accede al directorio del proyecto:
   ```bash
   cd RPG_Simulador
   ```
3. Instala la librería necesaria:
   ```bash
   pip install customtkinter
   ```
4. Ejecuta la aplicación:
   ```bash
   python main.py
   ```

---

## 🗂️ Estructura del Proyecto
```
RPG_Simulador/
│
├── gui/                         # Interfaz gráfica (CustomTkinter)
│   ├── crear_personaje_frame.py
│   ├── listar_personajes_frame.py
│   └── batalla_frame.py
│
├── models/                      # Clases base y subclases de personajes
│   ├── personaje.py
│   ├── guerrero.py
│   ├── mago.py
│   ├── arquero.py
│   ├── demonio.py
│   └── angel.py
│
├── utils/                       # Lógica del juego y persistencia
│   ├── juego.py
│   └── __init__.py
│
├── personajes.json              # Archivo de guardado automático
├── main.py                      # Archivo principal que inicia la app
└── README.md
```

---

##  Librerías Utilizadas
- **CustomTkinter** → Para la interfaz gráfica moderna.  
- **json (nativa de Python)** → Para guardar y cargar personajes creados.  


