# Laboratorio 1 Graficas por computadoras (SR1: Point)

from render import *
from utilities import *

objetoRender = None

def glInit(width, height):
	glCreateWindow(width,height)

def glCreateWindow(width, height):
	global objetoRender
	objetoRender = Render(width, height)

def glViewport(x,y, width, height):

	global objetoRender

	objetoRender.vp_x = x
	objetoRender.vp_y = y
	objetoRender.vp_width = width
	objetoRender.vp_height = height

	# Dibujando el VP: ForLoop posterior
	for ancho in range(x, width+x):
		for alto in range(y, height+y):
			objetoRender.point(ancho,alto)

def glClear():
	objetoRender.clear()

def glClearColor(r, g, b):
	objetoRender.clear_color = color(round(255*r), round(255*g), round(255*b))
	glClear()

def glVertex(x,y):
	# objetoRender.current_color = color(0,255,0)

	# objetoRender.point(objetoRender.vp_x , objetoRender.vp_y)

	# objetoRender.point(objetoRender.vp_x + round(objetoRender.vp_width/2) + round(x * (objetoRender.vp_width/2)), objetoRender.vp_y + y + round(objetoRender.vp_height/2))

	des_x = objetoRender.vp_x
	des_y = objetoRender.vp_y
	width = objetoRender.vp_width
	height = objetoRender.vp_height

	centro_x = round(des_x + (width/2))
	centro_y = round(des_y + (height/2))

	movimiento_x = centro_x + round(x * width/2) 
	movimiento_y = centro_y + round(y * height/2) 

	objetoRender.point(movimiento_x,movimiento_y)

	# objetoRender.point(objetoRender.vp_x + objetoRender.vp_width - 1, objetoRender.vp_y + objetoRender.vp_height - 1)


def glColor(r, g, b):
	objetoRender.current_color = color(round(255*r), round(255*g), round(255*b))

def glFinish():
	objetoRender.write('test.bmp')


