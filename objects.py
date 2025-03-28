from OpenGL.GL import *
from OpenGL.GLUT import *

def draw_cube(x, y, z, size, color):
    glPushMatrix()
    glTranslatef(x, y, z)
    glColor3fv(color)
    glutSolidCube(size)
    glPopMatrix()

def draw_building_with_windows(x, y, z, size, color, window_color):
    # Prédio principal
    draw_cube(x, y, z, size, color)

    # Desenhar janelas como cubinhos menores na frente
    spacing = 0.3
    window_size = 0.2
    start_x = x - 0.4
    start_y = y + 0.5
    for i in range(3):
        for j in range(2):
            wx = start_x + i * spacing
            wy = start_y - j * spacing
            draw_cube(wx, wy, z + size / 2 + 0.01, window_size, window_color)

def draw_car(x, y, z):
    # Base do carro
    draw_cube(x, y, z, 1.0, (1, 1, 0))
    # Cabine
    draw_cube(x, y + 0.35, z, 0.5, (0.3, 0.3, 0.8))
