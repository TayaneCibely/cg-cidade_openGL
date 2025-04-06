from OpenGL.GLUT import *
from renderer import draw_scene, init_scene
from logic import handle_keyboard
from config import window_config

from renderer import setup_lighting


def timer(value):
    glutPostRedisplay()
    glutTimerFunc(16, timer, 0)

def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(window_config["width"], window_config["height"])
    glutCreateWindow("MiniCidade - Simulador".encode("ascii", "ignore"))
    setup_lighting()
    init_scene()
    glutDisplayFunc(draw_scene)
    glutKeyboardFunc(handle_keyboard)
    glutTimerFunc(0, timer, 0)
    glutMainLoop()

if __name__ == "__main__":
    main()