import tkinter as tk
import pygame
from tkinter import messagebox

pygame.mixer.init()

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Taller Interfaz")
ventana.geometry("700x300")
ventana.resizable(False, False)

# -------- Frames organizados --------
frame1 = tk.Frame(ventana, bg="black", height=80)
frame1.pack(side="top", fill="x")

frame2 = tk.Frame(ventana, bg="grey")
frame2.pack(side="bottom", expand=True, fill="both")
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

def mostrarventana4():
    ventana3.withdraw()
    ventana4.deiconify()

def regresarventana4():
    ventana4.withdraw()
    ventana3.deiconify()

# -------- Ventana secundaria 1: Animación --------
ventana1 = tk.Toplevel(bg="lightblue")
ventana1.title("Animación")
ventana1.geometry("500x300")
ventana1.resizable(False, False)
ventana1.withdraw()

canvas = tk.Canvas(ventana1, bg="lightblue", width=500, height=250)
canvas.pack()

bola1 = canvas.create_oval(50, 50, 100, 100, fill="purple")
bola2 = canvas.create_oval(200, 150, 250, 200, fill="blue")

dx1, dy1 = 3, 2
dx2, dy2 = -2, -3

def mover():
    global dx1, dy1, dx2, dy2
    canvas.move(bola1, dx1, dy1)
    canvas.move(bola2, dx2, dy2)
    x1, y1, x2, y2 = canvas.coords(bola1)
    a1, b1, a2, b2 = canvas.coords(bola2)

    if x1 <= 0 or x2 >= 500: dx1 = -dx1
    if y1 <= 0 or y2 >= 250: dy1 = -dy1
    if a1 <= 0 or a2 >= 500: dx2 = -dx2
    if b1 <= 0 or b2 >= 250: dy2 = -dy2

    if not (x2 < a1 or x1 > a2 or y2 < b1 or y1 > b2):
        dx1, dy1, dx2, dy2 = -dx1, -dy1, -dx2, -dy2

    ventana1.after(30, mover)

mover()

tk.Button(ventana1, text="Regresar", bg="white", command=regresarventana1).pack(pady=10)

# -------- Ventana secundaria 2: Análisis numérico --------
ventana2 = tk.Toplevel(bg="lightblue")
ventana2.title("Análisis numérico")
ventana2.geometry("500x300")
ventana2.resizable(False, False)
ventana2.withdraw()

def recursividad(n, a=1, pares=None):
    if pares is None:
        pares = []
    if a > n:
        return pares
    if n % a == 0:
        pares.append((a, n // a))
    return recursividad(n, a + 1, pares)

def calcular():
    try:
        n = int(entry_num.get())
        pares = recursividad(n)
        resultado.set("Pares: " + ", ".join([f"({a},{b})" for a, b in pares]))
    except ValueError:
        messagebox.showerror("Error", "Ingrese un número entero válido")

tk.Label(ventana2, text="Ingrese un número entero:", bg="lightblue").pack(pady=10)
entry_num = tk.Entry(ventana2)
entry_num.pack()
resultado = tk.StringVar()
tk.Label(ventana2, textvariable=resultado, bg="lightblue").pack(pady=10)
tk.Button(ventana2, text="Calcular", command=calcular).pack(pady=5)
tk.Button(ventana2, text="Regresar", command=regresarventana2).pack(pady=5)

# -------- Ventana secundaria 3: Ficha Personal --------
ventana3 = tk.Toplevel(bg="lightblue")
ventana3.title("Ficha Personal")
ventana3.geometry("800x600")
ventana3.resizable(False, False)
ventana3.withdraw()

info = (
    "Nombre: Valeria Prado Valerín\n"
    "Carnet: 2025064517\n"
    "Edad: 18\n\n"
    "Biografía:\n"
    "Soy estudiante de Ingeniería en Computadores en el TEC.\n"
    "Me gusta bailar, dibujar y la música. Soy de Cartago.\n\n"
    "Grupo favorito: Barderos\n"
    "Género musical: Trap"
)
tk.Label(ventana3, text=info, justify="left", bg="lightblue").pack(pady=20)

# -------- Ventana secundaria 4: Imágenes y música --------
ventana4 = tk.Toplevel(bg="lightblue")
ventana4.title("Imágenes y música")
ventana4.geometry("1000x700")   # más grande
ventana4.resizable(False, False)
ventana4.withdraw()

tk.Label(ventana4, text="Cartago y Barderos", bg="lightblue", font=("Arial", 14, "bold")).pack(pady=10)

# --- Botones para música ---
def reproducir_musica():
    try:
        pygame.mixer.music.load("barderos.mp3.mp3")  # nombre correcto del archivo
        pygame.mixer.music.play(-1)  # loop infinito
    except Exception as e:
        messagebox.showerror("Error", f"No se pudo reproducir la música: {e}")

def detener_musica():
    pygame.mixer.music.stop()

tk.Button(ventana4, text="▶ Reproducir música", command=reproducir_musica).pack(pady=5)
tk.Button(ventana4, text="⏹ Detener música", command=detener_musica).pack(pady=5)

# --- Carga de imágenes ---
imagenes = []
try:
    img1 = tk.PhotoImage(file="vale.png")
    imagenes.append(img1)
    tk.Label(ventana3, image=img1, bg="lightblue").pack(pady=5, padx=10)

    # Se eliminó la imagen de bienvenidos

    img2 = tk.PhotoImage(file="cartago.png")
    img3 = tk.PhotoImage(file="barderos.png")
    imagenes.extend([img2, img3])
except Exception as e:
    print("Error cargando imágenes:", e)

lbl_img = tk.Label(ventana4, bg="lightblue")
lbl_img.pack(pady=10)

estado_img = {"actual": 0}

def alternar_imagen():
    if estado_img["actual"] == 0:
        lbl_img.config(image=imagenes[2])  # barderos
        estado_img["actual"] = 1
    else:
        lbl_img.config(image=imagenes[1])  # cartago
        estado_img["actual"] = 0

tk.Button(ventana4, text="Descubre más", command=alternar_imagen).pack(pady=10)
tk.Button(ventana4, text="Regresar", command=regresarventana4).pack(pady=10)

tk.Button(ventana3, text="Regresar", command=regresarventana3).pack(pady=10)
tk.Button(ventana3, text="Más información", command=mostrarventana4).pack(pady=10)

# -------- Botones en el menú principal --------
boton1 = tk.Button(frame1, text="Análisis de números", fg="black", command=mostrarventana2)
boton2 = tk.Button(frame1, text="Ficha personal", fg="black", command=mostrarventana3)
boton3 = tk.Button(frame1, text="Animación", fg="black", command=mostrarventana1)

boton1.pack(side="left", expand=True, fill="both", padx=5, pady=5)
boton2.pack(side="left", expand=True, fill="both", padx=5, pady=5)
boton3.pack(side="left", expand=True, fill="both", padx=5, pady=5)

# -------- Función para cerrar ventana principal --------
def cerrarventana():
    ventana.destroy()

canva1 = tk.Canvas(frame2, bg="lightgrey", width=400, height=200)
canva1.pack(pady=20)

tk.Button(canva1, text="Adiós", bg="white", command=cerrarventana).place(x=355, y=180)

ventana.mainloop()

