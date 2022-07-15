from utilities import *

from colors import *

class Render(object):
    def __init__(self, width, height):
		
        self.width = width  
        self.height = height    
        
        self.vp_x = 0
        self.vp_y = 0

        self.vp_width = 0
        self.vp_height = 0

        
        self.current_color = WHITE 

        self.clear_color = BLUE 

        self.clear()

    def clear(self):
        self.framebuffer = [
            [self.clear_color for x in range(self.width)]
            for y in range(self.height)
        ]

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

    def point(self, x, y):
        self.framebuffer[x][y] = self.current_color