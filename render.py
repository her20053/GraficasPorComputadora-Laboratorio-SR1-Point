# Importando libreria para manejo de bytes
from utilities import *

# Importando libreria para manejo de colores
from colors import *

class Render(object):

	# Metodo ejecutado al inicializar la clase:
    def __init__(self, width, height):
		
		# Estableciendo el ancho y el largo del framebuffer
        self.width = width  
        self.height = height    
        
		# Estableciendo el desface del Viewport en el framebuffer
        self.vp_x = 0
        self.vp_y = 0

		# Estableciendo el ancho y el largo del Viewport
        self.vp_width = 0
        self.vp_height = 0

        # Estableciendo el color por defecto con el que pintara el Render en caso de no ser cambiado
        self.current_color = WHITE 

		# Estableciendo el color con el que se realizara cualquier clear() en caso de no ser cambiado
        self.clear_color = GRIS 

		# Limpiando el framebuffer para llenarlo con el color del clear()
        self.clear()

	# Metodo encargado de limpiar el framebuffer 
    def clear(self):

		# Utilizando list comprehension se llenan todos los pixeles usando width y height
        self.framebuffer = [
            [self.clear_color for x in range(self.width)]
            for y in range(self.height)
        ]

	# Metodo utilizado para dibujar el framebuffer en un archivo bmp
    def write(self, filename):
        f = open(filename, 'bw')

        # pixel header
        f.write(char('B'))
        f.write(char('M'))
        f.write(dword(14 + 40 + self.width * self.height * 3))
        f.write(word(0))
        f.write(word(0))
        f.write(dword(14 + 40))

        # info header
        f.write(dword(40))
        f.write(dword(self.width))
        f.write(dword(self.height))
        f.write(word(1))
        f.write(word(24))
        f.write(dword(0))
        f.write(dword(self.width * self.height * 3))
        f.write(dword(0))
        f.write(dword(0))
        f.write(dword(0))
        f.write(dword(0))

        # pixel data
        for x in range(self.height):
            for y in range(self.width):
                f.write(self.framebuffer[y][x])

        f.close()

	# Metodo utilizado para establecer un punto especifico en el framebuffer
    def point(self, x, y):
        self.framebuffer[x][y] = self.current_color