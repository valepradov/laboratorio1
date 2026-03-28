import tkinter as tk
import pygame
import time

pygame.mixer.init()

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Taller Interfaz")
ventana.geometry("500x300")
ventana.resizable(width=False, height=False)

# Frame negro (menú principal)
frame1 = tk.Frame(ventana, bg="black")
frame1.pack(expand=True, fill="both")

# Frame gris (contenido)
frame2 = tk.Frame(ventana, bg="grey")
frame2.pack(expand=True, fill="both")
frame2.config(cursor="heart")

# --- Funciones para mostrar/ocultar ventanas ---
def mostrarventana1():
    ventana.withdraw()
    ventana1.deiconify()

def regresarventana1():
    ventana1.withdraw()
    ventana.deiconify()

def mostrarventana2():
    ventana.withdraw()
    ventana2.deiconify()

def regresarventana2():
    ventana2.withdraw()
    ventana.deiconify()

def mostrarventana3():
    ventana.withdraw()
    ventana3.deiconify()

def regresarventana3():
    ventana3.withdraw()
    ventana.deiconify()

# -------- Ventana secundaria 1: Animación
ventana1 = tk.Toplevel()
ventana1.title("Animación")
ventana1.geometry("500x300")
ventana1.resizable(width=False, height=False)
ventana1.withdraw()

tk.Label(ventana1, text="Aquí irá la animación").pack(pady=20)
botonB = tk.Button(ventana1, text="Regresar", command=regresarventana1)
botonB.pack(pady=20)

# -------- Ventana secundaria 2: Análisis numérico --------
ventana2 = tk.Toplevel()
ventana2.title("Análisis numérico")
ventana2.geometry("500x300")
ventana2.resizable(width=False, height=False)
ventana2.withdraw()

tk.Label(ventana2, text="Aquí irá el análisis de números").pack(pady=20)
botonA = tk.Button(ventana2, text="Regresar", command=regresarventana2)
botonA.pack(pady=20)

# -------- Ventana secundaria 3: Ficha Personal --------
ventana3 = tk.Toplevel()
ventana3.title("Ficha Personal")
ventana3.geometry("500x300")
ventana3.resizable(width=False, height=False)
ventana3.withdraw()

info = (
    "Nombre: Valeria Prado Valerín\n"
    "Carnet: 2025064517\n"
    "Edad: 18\n\n"
    "Biografía:\n"
    "Soy una estudiante de Ingeniería en Computadores en el TEC.\n"
    "Me gusta bailar, dibujar y la música. Soy una persona muy artística.\n\n"
    "Grupo favorito: Barderos\n"
    "Género musical: Trap"
)
tk.Label(ventana3, text=info, justify="left").pack(pady=20)

# Imagen (asegúrate de tener vale.png en la misma carpeta)
try:
    img = tk.PhotoImage(file="vale.png")
    lbl_img = tk.Label(ventana3, image=img)
    lbl_img.pack(pady=10)
except:
    tk.Label(ventana3, text="No se encontró la imagen vale.png").pack(pady=10)

botonF = tk.Button(ventana3, text="Regresar", command=regresarventana3)
botonF.pack(pady=20)

# -------- Botones en el menú principal --------
boton1 = tk.Button(frame1, text="Análisis de números", fg="black", command=mostrarventana2)
boton2 = tk.Button(frame1, text="Ficha personal", fg="black", command=mostrarventana3)
boton3 = tk.Button(frame1, text="Animación", fg="black", command=mostrarventana1)

boton1.place(relx=.05, rely=.05, relwidth=.25, relheight=.9)
boton2.place(relx=.35, rely=.05, relwidth=.25, relheight=.9)
boton3.place(relx=.65, rely=.05, relwidth=.25, relheight=.9)

# -------- Función para cerrar ventana principal --------
def cerrarventana():
    print("cerrarventana")
    ventana.destroy()

# Canvas dentro del frame gris
canva1 = tk.Canvas(frame2, bg="lightgrey", width=400, height=200)
canva1.pack(pady=20)

# Botón para cerrar
boton4 = tk.Button(canva1, text="Adiós", bg="white", command=cerrarventana)
boton4.place(x=355, y=180)

ventana.mainloop()
