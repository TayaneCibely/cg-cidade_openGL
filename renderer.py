import pygame
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.raw.GLUT import glutSwapBuffers, glutSolidSphere
from OpenGL.GLUT import glutSolidCone
from math import sin
from config import state
from logic import update_car_position, update_clouds
from objects import *

def generate_terrain_mesh():
    mesh = []
    for i in range(-400, 400):
        x = i / 100
        z = 0.8 * sin(0.8 * x)
        mesh.append((x, z))
    return mesh

def get_terrain_height(x):
    mesh = generate_terrain_mesh()
    for i in range(len(mesh)-1):
        x0, z0 = mesh[i]
        x1, z1 = mesh[i+1]
        if x0 <= x <= x1:
            ratio = (x - x0)/(x1 - x0)
            return z0 + ratio*(z1 - z0)
    return 0.0

def draw_house_with_texture(x, y, z, texture_id):
    # Base da casa com textura
    glBindTexture(GL_TEXTURE_2D, texture_id)
    glPushMatrix()
    glTranslatef(x, y, z)
    glColor3f(1, 1, 1)
    
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
    glColor3f(0.6, 0.1, 0.1)
    glutSolidCone(0.8, 0.6, 4, 4)
    glPopMatrix()

def load_texture(image_path):
    image = pygame.image.load(image_path)
    image = pygame.transform.flip(image, False, True)
    width, height = image.get_rect().size
    texture_data = pygame.image.tostring(image, "RGBA", 1)

    texture_id = glGenTextures(1)
    glBindTexture(GL_TEXTURE_2D, texture_id)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)

    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, width, height, 0, GL_RGBA, GL_UNSIGNED_BYTE, texture_data)
    return texture_id

def init_scene():
    glClearColor(0.5, 0.8, 1.0, 1.0)
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(70, 800/600, 0.1, 1000)
    glMatrixMode(GL_MODELVIEW)

def draw_scene():
    update_car_position()
    update_clouds()
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    gluLookAt(0, 5, 12, 0, 0, 0, 0, 2, 0)

    # Carregar texturas
    grass_texture_id = load_texture("textures/grama.png")
    asphalt_texture_id = load_texture("textures/asfalto.png")
    brick_texture_id = load_texture("textures/tijolos.png")

    # Terreno com textura
    glEnable(GL_TEXTURE_2D)
    glBindTexture(GL_TEXTURE_2D, grass_texture_id)
    glBegin(GL_QUAD_STRIP)
    for i in range(-650, 650):
        x = i / 100
        z = get_terrain_height(x)
        tex_coord = x * 0.2
        glTexCoord2f(tex_coord, 0); glVertex3f(x, -1.01, z - 6)
        glTexCoord2f(tex_coord, 1); glVertex3f(x, -1.01, z + 6)
    glEnd()
    glDisable(GL_TEXTURE_2D)

    # Estrada com textura e superfície curva
    road_width = 1.5
    glEnable(GL_TEXTURE_2D)
    glBindTexture(GL_TEXTURE_2D, asphalt_texture_id)
    glBegin(GL_QUAD_STRIP)
    for i in range(-650, 650):
        x = i / 100
        z = get_terrain_height(x)
        tex_coord = x * 0.1  
        glTexCoord2f(tex_coord, 0); glVertex3f(x, -1, z - road_width/2)
        glTexCoord2f(tex_coord, 1); glVertex3f(x, -1, z + road_width/2)
    glEnd()
    glDisable(GL_TEXTURE_2D)

    # Faixas da estrada 
    glColor3f(1, 1, 1) 
    glLineWidth(3.0)   

    # Configurações da faixa tracejada
    stripe_length = 0.3
    gap_length = 0.3
    
    for i in range(-650, 650, int((stripe_length + gap_length) * 100)):
        x_start = i / 100
        x_end = (i + stripe_length * 100) / 100
        
        # Calcula os pontos acompanhando a curvatura
        z_start = get_terrain_height(x_start)
        z_end = get_terrain_height(x_end)
        
        # Desenha cada traço da faixa
        glBegin(GL_QUADS)
        glVertex3f(x_start, -0.98, z_start - 0.08)  
        glVertex3f(x_end, -0.98, z_end - 0.08)      
        glVertex3f(x_end, -0.98, z_end + 0.08)       
        glVertex3f(x_start, -0.98, z_start + 0.08)   
        glEnd()

            
    # Prédios
    draw_building_with_windows(-4, 0, 4, 2, (0.7, 0.2, 0.2), (1, 1, 1))
    draw_building_with_windows(4, 0, -4, 2, (0.2, 0.2, 0.7), (1, 1, 0.5))

    # Casas com textura
    glEnable(GL_TEXTURE_2D)
    draw_house_with_texture(-2, -0.25, -3.5, brick_texture_id)
    draw_house_with_texture(3, -0.25, 3.5, brick_texture_id)
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

    # Carro (ajustado para a superfície curva)
    car_z = get_terrain_height(state["car_position"])
    draw_car(state["car_position"], -0.5, car_z)

    # Sol
    glPushMatrix()
    glTranslatef(5, 7, -10)
    glColor3f(1.0, 1.0, 0.0)
    glutSolidSphere(1.0, 20, 20)
    glPopMatrix()

    # Nuvens
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