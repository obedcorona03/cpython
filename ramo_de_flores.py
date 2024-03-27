import tkinter as tk
import random

# Función para dibujar una flor en una posición dada
def draw_flower(canvas, x, y):
    canvas.create_oval(x-10, y-10, x+10, y+10, fill='orange', outline='')
    petals = [(x+5, y-5), (x+5, y+5), (x, y), (x-5, y+5), (x-5, y-5)]
    canvas.create_polygon(petals, fill='yellow', outline='')

# Función de animación para mover las flores
def animate(canvas):
    canvas.delete('all')
    for _ in range(5):  # Dibujar cinco flores en posiciones aleatorias
        x = random.randint(0, 400)
        y = random.randint(0, 400)
        draw_flower(canvas, x, y)
    canvas.after(200, animate, canvas)

# Configurar la ventana
root = tk.Tk()
root.title("Ramo de Flores Animado")

# Crear el lienzo (canvas)
canvas = tk.Canvas(root, width=400, height=400, bg='white')
canvas.pack()

# Ejecutar la animación
animate(canvas)

# Mostrar la ventana
root.mainloop()
