import pygame
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.raw.GLUT import glutSwapBuffers, glutSolidSphere
from OpenGL.GLUT import glutSolidCone

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

def draw_house_with_texture(x, y, z, texture_id):
    # Base da casa com textura
    glBindTexture(GL_TEXTURE_2D, texture_id)  # Garantir que a textura está ativa
    glPushMatrix()
    glTranslatef(x, y, z)
    glColor3f(1, 1, 1)  # Garantir que a textura seja aplicada sem cor
    
    # Frente da casa
    glBegin(GL_QUADS)
    glTexCoord2f(0, 0); glVertex3f(-0.5, -0.5,  0.5)
    glTexCoord2f(1, 0); glVertex3f( 0.5, -0.5,  0.5)
    glTexCoord2f(1, 1); glVertex3f( 0.5,  0.5,  0.5)
    glTexCoord2f(0, 1); glVertex3f(-0.5,  0.5,  0.5)
    glEnd()

    # Trás da casa
    glBegin(GL_QUADS)
    glTexCoord2f(0, 0); glVertex3f(-0.5, -0.5, -0.5)
    glTexCoord2f(1, 0); glVertex3f( 0.5, -0.5, -0.5)
    glTexCoord2f(1, 1); glVertex3f( 0.5,  0.5, -0.5)
    glTexCoord2f(0, 1); glVertex3f(-0.5,  0.5, -0.5)
    glEnd()

    # Lados da casa
    glBegin(GL_QUADS)
    glTexCoord2f(0, 0); glVertex3f(-0.5, -0.5,  0.5)
    glTexCoord2f(1, 0); glVertex3f(-0.5, -0.5, -0.5)
    glTexCoord2f(1, 1); glVertex3f(-0.5,  0.5, -0.5)
    glTexCoord2f(0, 1); glVertex3f(-0.5,  0.5,  0.5)

    glTexCoord2f(0, 0); glVertex3f( 0.5, -0.5,  0.5)
    glTexCoord2f(1, 0); glVertex3f( 0.5, -0.5, -0.5)
    glTexCoord2f(1, 1); glVertex3f( 0.5,  0.5, -0.5)
    glTexCoord2f(0, 1); glVertex3f( 0.5,  0.5,  0.5)
    glEnd()

    glPopMatrix()

    # Telhado (sem textura)
    glPushMatrix()
    glTranslatef(x, y + 0.50, z)
    glRotatef(-110, 1, 0, 0)
    glColor3f(0.6, 0.1, 0.1)  # Cor do telhado
    glutSolidCone(0.8, 0.6, 4, 4)  # Desenha o telhado
    glPopMatrix()

    # Telhado (sem textura)
    
    glPushMatrix()
    glTranslatef(x, y + 0.50, z)
    glRotatef(-110, 1, 0, 0)
    glColor3f(0.6, 0.1, 0.1)  # Cor do telhado
    glutSolidCone(0.8, 0.6, 4, 4)  # Desenha o telhado
    glPopMatrix()

def load_texture(image_path):
    # Carregar a imagem usando Pygame
    image = pygame.image.load(image_path)
    image = pygame.transform.flip(image, False, True)  # Corrige a orientação da imagem

    # Obter os dados da imagem
    width, height = image.get_rect().size
    texture_data = pygame.image.tostring(image, "RGBA", 1)

  # Gerar e configurar a textura
    texture_id = glGenTextures(1)
    glBindTexture(GL_TEXTURE_2D, texture_id)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)

    # Carregar a textura para o OpenGL
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, width, height, 0, GL_RGBA, GL_UNSIGNED_BYTE, texture_data)

    return texture_id


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

    # Carregar a textura (agora fora da função de desenhar a casa)
    texture_id = load_texture("textures/tijolos.png")
      # Ativar a textura para a casa
    glEnable(GL_TEXTURE_2D)
    draw_house_with_texture(-2, -0.25, -3.5, texture_id)
    draw_house_with_texture(3, -0.25, 3.5, texture_id)
    glDisable(GL_TEXTURE_2D)
    

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