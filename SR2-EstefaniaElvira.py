
# Estefania Elvira 20725
# Ejercicio 1 SR-points
# Fecha 13.07.22
from gl import Renderer,vector2, color

width = 960
height = 540

rend = Renderer(width, height)

#Rellenamos el Poligono 1
rend.glColor(0.5,1,0.75)
poligono1 = ((165, 380),(185, 360),(180, 330),(207, 345),(233, 330),(230, 360),
(250, 380),(220, 385),(205, 410),(193, 383))
rend.glFill(poligono1)
#Rellenamos el Poligono 2
rend.glColor(1,1,0.5)
poligono2 = ((321, 335),(288, 286),(339, 251),(374, 302))
rend.glFill(poligono2)
#Rellenamos el Poligono 3
rend.glColor(1,0.5,1)
poligono3 = ((377, 249),(411, 197),(436, 249))
rend.glFill(poligono3)
#Relleneamos el Poligono 4
rend.glColor(0.5,1,1)
poligono4 = ((413, 177),(448, 159),(502, 88),(553, 53),(535, 36),(676, 37),(660, 
52),(750, 145),(761, 179),(672, 192),(659, 214),(615, 214),(632, 230),(580, 230),
(597, 215),(552, 214),(517, 144),(466, 180))
rend.glFill(poligono4)
#Rellenamos el Poligono 5
rend.glColor(0,0,0)
poligono5 = ((682, 175),(708, 120),(735, 148),(739, 170))
rend.glFill(poligono5)
#Renderizamos los poligonos en un archivo llamado Poligono.bmp
rend.glFinish("Output.bmp")

