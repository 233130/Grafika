import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

#definicja pozycji wierzchołków
wierzcholki = (
    (1, -1, -1),
    (1, 1, -1),
    (-1, 1, -1),
    (-1, -1, -1),
    (1, -1, 1),
    (1, 1, 1),
    (-1, -1, 1),
    (-1, 1, 1)
)

#definicja z których punktów składają się wierzchołki
powierzchnie = (
    (0, 1, 2, 3),   #red
    (3, 2, 7, 6),   #blue
    (1, 5, 7, 2),   #green
    (6, 7, 5, 4),   #red
    (4, 5, 1, 0),   #blue
    (4, 0, 3, 6)    #green
)

#definicja zmiennych kolorów i światła
RedSurface = (1.0, 0.0, 0.0, 1.0)
GreenSurface = (0.0, 1.0, 0.0, 1.0)
BlueSurface = (0.0, 0.0, 1.0, 1.0)
LightAmbient = (0.1, 0.1, 0.1, 0.1)
LightDiffuse = (0.7, 0.7, 0.7, 0.7)
LightSpecular = (0.0, 0.0, 0.0, 0.1)
LightPosition = (5.0, 5.0, 5.0, 0.0)

kolory = (RedSurface, GreenSurface, BlueSurface)

#funkcja rysująca kostkę
def kostka():
    glBegin(GL_QUADS)
    x = 0
    for side in powierzchnie:
        glMaterialfv(GL_FRONT_AND_BACK, GL_AMBIENT, kolory[x % 3])
        for v in side:
            glVertex3fv(wierzcholki[v])
        x += 1
    glEnd()


##main
pygame.init()
display = (800, 600)
pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

# gluPerspective(45, , 0.1, 50.0)
gluPerspective(45, (display[0] / display[1]), 1, 10.0);
glTranslate(0.0, 0.0, -5)

#ustawianie światła
glLightfv(GL_LIGHT0, GL_POSITION, LightPosition)
glLightfv(GL_LIGHT0, GL_DIFFUSE, LightDiffuse)
glLightfv(GL_LIGHT0,GL_AMBIENT, LightAmbient)
glLightfv(GL_LIGHT0, GL_SPECULAR, LightSpecular)
glDrawBuffer(GL_BACK)
glEnable(GL_LIGHTING)
glEnable(GL_DEPTH_TEST)
glEnable(GL_LIGHT0)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    glRotatef(1, 3, 1, 1)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    kostka()
    pygame.display.flip()
    pygame.time.wait(10)
