from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def draw_cube(x, y, z, size, color):
    glPushMatrix()
    glTranslatef(x, y, z)
    glColor3fv(color)
    glutSolidCube(size)
    glPopMatrix()

def draw_building_with_windows(x, y, z, size, color, window_color):
    draw_cube(x, y, z, size, color)
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
    draw_cube(x, y, z, 1.0, (1, 1, 0))
    draw_cube(x, y + 0.35, z, 0.5, (0.3, 0.3, 0.8))

def draw_tree(x, y, z):
    # Tronco
    glPushMatrix()
    glTranslatef(x, y, z)
    glColor3f(0.55, 0.27, 0.07)
    glScalef(0.2, 0.6, 0.2)
    glutSolidCube(1)
    glPopMatrix()

    # Copa
    glPushMatrix()
    glTranslatef(x, y + 0.6, z)
    glColor3f(0.0, 0.5, 0.0)
    glutSolidSphere(0.5, 20, 20)
    glPopMatrix()

def draw_house(x, y, z):
    # Base
    draw_cube(x, y, z, 1.0, (0.9, 0.7, 0.5))

    # Telhado
    glPushMatrix()
    glTranslatef(x, y + 0.75, z)
    glRotatef(-90, 1, 0, 0)
    glColor3f(0.6, 0.1, 0.1)
    glutSolidCone(0.8, 0.6, 4, 4)
    glPopMatrix()

def draw_cone(x, y, z):
    glPushMatrix()
    glTranslatef(x, y, z)
    glRotatef(-90, 1, 0, 0)
    glColor3f(1.0, 0.5, 0.0)
    glutSolidCone(0.2, 0.4, 10, 2)
    glPopMatrix()

def draw_traffic_light(x, y, z, is_green):
    # Poste
    glPushMatrix()
    glTranslatef(x, y, z)
    glColor3f(0.2, 0.2, 0.2)
    glScalef(0.1, 2.0, 0.1)
    glutSolidCube(1)
    glPopMatrix()

    # Caixa do semáforo
    draw_cube(x, y + 1.1, z + 0.25, 0.3, (0.3, 0.3, 0.3))

    # Luz vermelha (acima)
    draw_cube(x, y + 1.25, z + 0.35, 0.15, (1, 0, 0) if not is_green else (0.2, 0.2, 0.2))

    # Luz verde (abaixo)
    draw_cube(x, y + 0.95, z + 0.35, 0.15, (0, 1, 0) if is_green else (0.2, 0.2, 0.2))