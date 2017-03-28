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

	gran = 200

	x = 0.01
	y = 4*x*(1-x)*r
	for i in range(gran):
		pointsx.append(x)
		pointsy.append(y)

		x = y
		pointsx.append(x)
		pointsy.append(y)
	
		y = 4*x*(1-x)*r

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
draw_figure(1.5,True)
plt.figure(3)
for r in np.arange(0.8,4.0,0.001):
	result = draw_figure(r,False)
	plt.plot([r for i in range(len(result))], result, marker=',',lw=0, linestyle='', color='black')
plt.show()
plt.savefig('fiegen.png')


