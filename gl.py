# Estefania Elvira 20725
# Ejercicio 1 SR-points
# Fecha 13.07.22


import struct
from collections import namedtuple

def char(c):
    #1 byte
    return struct.pack('=c', c.encode('ascii'))

def word(w):
    #2 bytes
    return struct.pack('=h', w)

def dword(d):
    #4 bytes
    return struct.pack('=l', d)

def color(r, g, b):
    return bytes([int(b * 255),
                  int(g * 255),
                  int(r * 255)] )

##variables
cNegro = color(0, 0, 0)
cBlanco = color(1, 1, 1)
vector2 = namedtuple('Point2', ['x', 'y'])

class Renderer(object):
   
	#Constructor
	def __init__(self, width, height):

		# Crea un nuevo Renderer de color negro
		self.clearColor = cNegro
		self.clearColor = cBlanco
		self.glCreateWindow(width, height)

	# Crea la ventana
	def glCreateWindow(self, width, height):
		self.width = width
		self.height = height
		# Crea una ventana dibujando en todos los pixeles
		self.glClear()
		# El viewPort tendrá las mismas dimensiones que la ventana
		self.glViewPort(0, 0, width, height)

	# Crea el viewport
	def glViewPort(self, x, y, width, height):
		self.vpX = x
		self.vpY = y
		self.vpWidth = width
		self.vpHeight = height

	# Determina que color quiero para el fondo
	def glClearColor(self, r, g, b):
		# Color que le quiero asignar a los pixeles de fondo
		# Tedrá 3 Bytes
		self.clearColor = color(r, g, b)

	def glClear(self):
		# Recorre todo el ancho y altura y a cada una le asigna el color de 
		# limpieza que es negro
		self.pixels = [[ self.clearColor for y in range(self.height)] for x in range(self.width) ]

	# Color del dibujo
	def glColor(self, r, g, b):
		self.currColor = color(r,g,b)

	# Dibuja un punto en el ViewPort
	def glVertex(self, x, y, color = None):
		x = (x + 1) * (self.vpWidth / 2) + self.vpX
		y = (y + 1) * (self.vpHeight / 2) + self.vpY
		
		if x < self.vpX or x >= self.vpX + self.vpWidth or y < self.vpY or y >= self.vpY + self.vpHeight:
			return
		
		# Para que acepte solo enteros
		if (0 < x < self.width) and (0 < y < self.height):
			self.pixels[int(x)][int(y)] = color or self.currColor

	# Dibujar un punto en coordenadas norm
	def glPoint(self, x, y, color = None): # Pide color y si se le da lo coloca y si no coloca el dafault
		if x < self.vpX or x >= self.vpX + self.vpWidth or y < self.vpY or y >= self.vpY + self.vpHeight:
			return
		
		# Para que acepte solo enteros
		if (0 < x < self.width) and (0 < y < self.height):
			self.pixels[int(x)][int(y)] = color or self.currColor

	# Crea líneas
	def glLine(self, v0, v1, color = None):
		x0 = v0.x
		x1 = v1.x
		y0 = v0.y
		y1 = v1.y

		# Pendiente
		dx = abs(x1 - x0)
		dy = abs(y1 - y0)

		# Para determinar si está muy inclinado
		steep = dy > dx # Hay más desplazamiento en dy que en dx

		# Cambia de eje si está muy inclinado, o sea, más de 1 de pendiente (arriba)
		if steep: 
			x0, y0 = y0, x0
			x1, y1 = y1, x1

		# Se está dibujando de derecha a izquierda, se tiene que dibujar de izquierda a derecha
		if x0 > x1:
			x0, x1 = x1, x0
			y0, y1 = y1, y0

		# Pendiente
		dx = abs(x1 - x0)
		dy = abs(y1 - y0)

		# Determina en cual de los dos pixeles cae cada vez que vaya cambiando de posición la línea
		offset = 0

		# Verá si ya se apsó del límite para pasarse a otro pixel y dibujarlo
		limit = 0.5

		# Para que el denominador no se 0
		try:
			m =  dy / dx
		except ZeroDivisionError:
			pass
		else:
			y = y0
			# Range no incluye el último número, entonces se le suma 1
			for x in range(x0, x1 + 1):
				if steep:
					self.glPoint(y, x, color)
				else:
					self.glPoint(x, y, color)
				# Calcula el siguiente valor de y
				offset += m
				if offset >= limit:
					# Y va creciendo y límite también para que se vaya dibujando bien todo
					y += 1
					limit += 1

	# def glFill(self, polygon):
# 		for y in range(self.height):
#  for x in range(self.width): 
#  i = 0
#  j = len(polygon) - 1
#  result = False
#  #Se realiza un ciclo que revisa si el punto siempre se 
# encuentra entre los limites de los vertices planteados
#  for i in range(len(polygon)):
#  #Si el poligono se encuentra dentro de los limites 
# la variable resultado esta dentro de los limites obtiene un valor True 
#  if (polygon[i][1] < y and polygon[j][1] >= y) or 
# (polygon[j][1] < y and polygon[i][1] >= y):
#  if polygon[i][0] + (y - polygon[i][1]) / 
# (polygon[j][1] - polygon[i][1]) * (polygon[j][0] - polygon[i][0]) < x:
#  result = not result
#  j = i
#  #Si el resultado es True entonces se pinta el punto 
#  if result == True:
#  self.glPoint((float(x)/(float(self.width)/2))-1,
# (float(y)/(float(self.height)/2))-1,self.vertexColor)
#  else:
#  pass



 
	def glFinish(self, filename):
				file = open(filename, 'wb')
				#file header 14
				file.write(bytes('B'.encode('ascii')))
				file.write(bytes('M'.encode('ascii')))
				file.write(dword(54 + self.width * self.height * 3))
				file.write(dword(0))
				file.write(dword(54))
				
				file.write(dword(40))
				file.write(dword(self.width))
				file.write(dword(self.height))
				file.write(word(1))
				file.write(word(24))
				file.write(dword(0))
				file.write(dword(self.width * self.height * 3))
				file.write(dword(0))
				file.write(dword(0))
				file.write(dword(0))
				file.write(dword(0))
				for x in range(self.height):
					for y in range(self.width):
						file.write(self.pixels[x][y])
				file.close()