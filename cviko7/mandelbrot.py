import numpy as np
import matplotlib.pyplot as plt
from PIL import Image, ImageDraw 
import math

size = 600

im = Image.new('RGB', (size, size))

x = (-0.0,0.5)
y = (-0.9,-0.4)

x = np.linspace(x[0],x[1], size, endpoint=False)
y = np.linspace(y[0],y[1], size, endpoint=False)

for cx, i in enumerate(x):
	for cy, j in enumerate(y):
		c = complex(i,j)
		z = 0
		v = []
		for k in range(0,30):
			z = z**2+c
			v.append(math.sqrt(z.real**2+z.imag**2)*100)
			if abs(z) > 2: break;
		if abs(z) < 2:			#is mandel
			im.putpixel((cx,cy),(0,0,0)) 
		else: 				#is not mandel
			b = int(sum(v)/len(v))# priemerna vzdialenost od nuly

#kolko iteracii trvalo, nez postupnost opustila 2
			im.putpixel((cx,cy),(k**2,k**2,k**2))

# do ktoreho kvadrantu sa postuponst dostala
#			if z.real > 0 and z.imag > 0: im.putpixel((cx,cy),(255,0,0)) 
#			if z.real > 0 and z.imag < 0: im.putpixel((cx,cy),(255,0,255)) 
#			if z.real < 0 and z.imag > 0: im.putpixel((cx,cy),(0,0,255)) 
#			if z.real < 0 and z.imag < 0: im.putpixel((cx,cy),(0,255,0))

im.save('mandel.png','png')


