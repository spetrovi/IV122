import numpy as np
import matplotlib.pyplot as plt
from PIL import Image, ImageDraw 
import math

def julius((x1,x2),(y1,y2),const,name):
	size = 600

	im = Image.new('RGB', (size, size))

	x = np.linspace(x1,x2, size, endpoint=False)
	y = np.linspace(y1,y2, size, endpoint=False)

	for cx, i in enumerate(x):
		for cy, j in enumerate(y):
			z = complex(i,j)
#			c = complex(-0.13,0.75)
			c = complex(-0.13,const)
			v = []
			for k in range(0,30):
				z = z**2+c
				v.append(math.sqrt(z.real**2+z.imag**2)*100)
				if abs(z) > 2: break;
			if abs(z) < 2:			#is mandel
				im.putpixel((cx,cy),(0,0,0)) 
			else: 				#is not mandel

		#kolko iteracii trvalo, nez postupnost opustila 2
				im.putpixel((cx,cy),(k**2,k**2,k**2))

	im.save('jul2/'+str(name)+'.png','png')

x = (-2,2)
y = (-2,2)

for i,j in enumerate(np.linspace(0.0,2,150,endpoint=False)):
	julius(x,y,j,i)
#for i in range(100):
	




