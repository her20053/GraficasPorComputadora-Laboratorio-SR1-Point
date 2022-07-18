from gl import *

glInit(width=80, height=80)
glViewport(x = 10, y = 10, width = 50, height =50)
glColor(r=0.839,g=0.756,b=0.156)

# for i in range(20):
# 	for j in range(20):
# 		glVertex(x=i, y=j)
# 		glVertex(x=-i, y=-j)
glVertex(x=1, y=1)

glFinish()
