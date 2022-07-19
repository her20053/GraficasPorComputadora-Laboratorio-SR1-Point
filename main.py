from gl import *

glInit(width=80, height=80)
glViewport(x = 10, y = 10, width = 49, height =49)
glColor(r=0.839,g=0,b=0)

# for i in range(20):
# 	for j in range(20):
# 		glVertex(x=i, y=j)
# 		glVertex(x=-i, y=-j)


glVertex(x=0.90, y=0.5)

glFinish()
