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

	# Dibujando el VP: ForLoop previo
	# for j in range(x,width):
	# 	for k in range(y,height):
	# 		objetoRender.point(j,k)

	# Dibujando el VP: ForLoop posterior
	for ancho in range(x, width+x):
		for alto in range(y, height+y):
			objetoRender.point(ancho,alto)

def glClear():
	objetoRender.clear()

def glClearColor(r, g, b):
	objetoRender.clear_color = color(r, g, b)
	glClear()

def glVertex(x,y):
	# objetoRender.current_color = color(0,255,0)

	objetoRender.point(objetoRender.vp_x , objetoRender.vp_y)

	objetoRender.point(objetoRender.vp_x + x + round(objetoRender.vp_width/2), objetoRender.vp_y + y + round(objetoRender.vp_height/2))

	objetoRender.point(objetoRender.vp_x + objetoRender.vp_width - 1, objetoRender.vp_y + objetoRender.vp_height - 1)


def glColor(r, g, b):
	objetoRender.current_color = color(r, g, b)

def glFinish():
	objetoRender.write('test.bmp')


