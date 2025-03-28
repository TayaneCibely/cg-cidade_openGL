from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.raw.GLUT import glutSwapBuffers, glutSolidSphere

from config import state
from logic import update_car_position, update_clouds
from objects import (
    draw_cube,
    draw_building_with_windows,
    draw_car,
    draw_tree,
    draw_house,
    draw_cone,
    draw_traffic_light
)

def init_scene():
    glClearColor(0.5, 0.8, 1.0, 1.0)
    glEnable(GL_DEPTH_TEST)

    # Ativar transparência
    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45, 800 / 600, 1, 100)

    glMatrixMode(GL_MODELVIEW)

def draw_scene():
    update_car_position()
    update_clouds()

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    gluLookAt(0, 5, 15, 0, 0, 0, 0, 1, 0)

    # Estrada (longitudinal no eixo X)
    glColor3f(0.1, 0.1, 0.1)
    glBegin(GL_QUADS)
    glVertex3f(-6, -1, -1)
    glVertex3f(6, -1, -1)
    glVertex3f(6, -1, 1)
    glVertex3f(-6, -1, 1)
    glEnd()

    # Faixa branca central (tracejada)
    glColor3f(1, 1, 1)
    for x in range(-5, 6, 2):
        glBegin(GL_QUADS)
        glVertex3f(x - 0.2, -0.99, -0.05)
        glVertex3f(x + 0.2, -0.99, -0.05)
        glVertex3f(x + 0.2, -0.99, 0.05)
        glVertex3f(x - 0.2, -0.99, 0.05)
        glEnd()

    # Grama lateral
    glColor3f(0.2, 0.6, 0.2)
    glBegin(GL_QUADS)
    glVertex3f(-6, -1.01, -5)
    glVertex3f(6, -1.01, -5)
    glVertex3f(6, -1.01, -1)
    glVertex3f(-6, -1.01, -1)

    glVertex3f(-6, -1.01, 1)
    glVertex3f(6, -1.01, 1)
    glVertex3f(6, -1.01, 5)
    glVertex3f(-6, -1.01, 5)
    glEnd()

    # Prédios
    draw_building_with_windows(-4, 0, 4, 2, (0.7, 0.2, 0.2), (1, 1, 1))
    draw_building_with_windows(4, 0, -4, 2, (0.2, 0.2, 0.7), (1, 1, 0.5))

    # Casas menores
    draw_house(-2, -0.25, -3.5)
    draw_house(3, -0.25, 3.5)

    # Árvores
    draw_tree(-5.5, 0, 2)
    draw_tree(5.5, 0, -2)
    draw_tree(5, 0, 4)

    # Cones de trânsito
    draw_cone(-1.5, -1, 0.8)
    draw_cone(-1.0, -1, 0.8)
    draw_cone(-0.5, -1, 0.8)

    # Semáforo
    draw_traffic_light(0, -1, 1.3, state["traffic_light"] == 1)

    # Carro
    draw_car(state["car_position"], -0.5, 0)

    # Sol
    glPushMatrix()
    glTranslatef(5, 7, -10)
    glColor3f(1.0, 1.0, 0.0)
    glutSolidSphere(1.0, 20, 20)
    glPopMatrix()

    # Nuvens animadas
    def draw_cloud(x, y, z):
        glPushMatrix()
        glColor4f(1.0, 1.0, 1.0, 0.9)
        glTranslatef(x, y, z)
        glutSolidSphere(0.5, 15, 15)
        glTranslatef(0.6, 0.1, 0)
        glutSolidSphere(0.4, 15, 15)
        glTranslatef(-1.0, 0.1, 0)
        glutSolidSphere(0.4, 15, 15)
        glPopMatrix()

    draw_cloud(-4 + state["cloud_offset"], 6.5, -8)
    draw_cloud(2 + state["cloud_offset"], 7, -9)

    glutSwapBuffers()