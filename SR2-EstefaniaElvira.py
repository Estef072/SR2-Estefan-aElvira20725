
# Estefania Elvira 20725
# Ejercicio 1 SR-points
# Fecha 13.07.22
from gl import Renderer,vector2, color
import random

width = 960
height = 540


rend = Renderer(width, height)
rend.glColor(0.3, 0.4, 0.6)

poligono1 = [vector2(165, 380), vector2(185, 360),vector2(180, 330),vector2(207, 345), vector2(233, 330), vector2(230, 360), vector2(250, 380), vector2(220, 385), vector2(205, 410), vector2(193, 383)]
poligono1 = [(165, 380), (185, 360), (180, 330), (207, 345), (233, 330), (230, 360), (250, 380), (220, 385), (205, 410), (193, 383)]

poligono2 = [(321, 335), (288, 286), (339, 251), (374, 302)]
poligono3 = [(377, 249), (411, 197), (436, 249)]
poligono4 = [(413, 177), (448, 159), (502, 88), (553, 53), (535, 36), (676, 37), (660, 52),
            (750, 145), (761, 179), (672, 192), (659, 214), (615, 214), (632, 230), (580, 230),
            (597, 215), (552, 214), (517, 144), (466, 180)]

poligono5 = [(682, 175), (708, 120), (735, 148), (739, 170),(745,190),(750,201)]

figuras = [poligono1, poligono2, poligono3, poligono4, poligono5]


for i in figuras:
    rend.glFill(i, color(random.random(), random.random(), random.random()))
    if i == poligono5:
        rend.glFill(i, color(1, 1, 1))




rend.glFinish("result.bmp")