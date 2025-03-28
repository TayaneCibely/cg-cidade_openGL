from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.raw.GLUT import glutSwapBuffers

from config import state
from logic import update_car_position
from objects import draw_cube, draw_building_with_windows, draw_car

def init_scene():
    glClearColor(0.5, 0.8, 1.0, 1.0)
    glEnable(GL_DEPTH_TEST)

    # Definir o modo de projeção
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45, 800/600, 1, 100)

    glMatrixMode(GL_MODELVIEW)

def draw_scene():
    update_car_position()

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    gluLookAt(0, 5, 15, 0, 0, 0, 0, 1, 0)

    # Rua
    glColor3f(0.2, 0.2, 0.2)
    glBegin(GL_QUADS)
    glVertex3f(-5, -1, 5)
    glVertex3f(5, -1, 5)
    glVertex3f(5, -1, -5)
    glVertex3f(-5, -1, -5)
    glEnd()

    # Prédios
    draw_building_with_windows(-4, 0, 4, 2, (0.7, 0.2, 0.2), (1, 1, 1))
    draw_building_with_windows(4, 0, -4, 2, (0.2, 0.2, 0.7), (1, 1, 0.5))


# Semáforo
    draw_cube(0, 1, 4.5, 0.3, (0.3, 0.3, 0.3))
    draw_cube(0, 1.5, 4.5, 0.2, (1, 0, 0) if state["traffic_light"] == 0 else (0, 1, 0))

    # Carro
    draw_car(state["car_position"], -0.5, 0)

    glutSwapBuffers()