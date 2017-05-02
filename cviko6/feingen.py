import matplotlib.pyplot as plt
import numpy as np

def draw_figure(r,show):
	if show:
		fine = 0.01
		x = 0.0
		xax = []
		yax = []
		while x <= 1.1:
			y = 4*x*(1-x)*r
			xax.append(x)
			yax.append(y)
			x+=fine


	pointsx = []
	pointsy = []

	gran = 100

	x = 0.01
	y = 4*x*(1-x)*r
	for i in range(gran):
		pointsx.append(x)
		pointsy.append(y)

		x = y
		pointsx.append(x)
		pointsy.append(y)
		y = 4*r*x*(1-x)
	
	if show:
		plt.figure(1)
		plt.axis([0.0,1.0,0.0,1.0])
		plt.plot(pointsx, pointsy)
		plt.plot(xax,yax)
		plt.plot([0.0,1.0],[0.0,1.0])
		plt.show()

		plt.figure(2)
		plt.plot(range(gran*2),pointsx)
		plt.show()
	return pointsy[100:]

def draw_feingen(x1,x2,y2):
	for r in np.linspace(x1,x2, 2000, endpoint=False):
		result = draw_figure(r,True)
		plt.plot([r for i in range(len(result))], result, marker=',',lw=0, linestyle='', color='black')
		plt.ylim = y2
	#plt.show()
	
	plt.savefig('./feingen/2.png')
	plt.close()

x1 = 0.65
x2 = 0.8
y1 = 0.4
y2 = 1000
#for xzoom in np.linspace(0.65,1.0, 100, endpoint=False):
draw_feingen(x1,x2,y2)

