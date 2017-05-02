import matplotlib.pyplot as plt
import math, random
def color(i):
	colors = ['red','blue','yellow', 'green','black']
	return colors[i]

def distance((x1,y1),(x2,y2)):
	return math.sqrt((x2-x1)**2+(y2-y1)**2)

def assign((x,y), centers):
	for i in range(len(x)):
		distances = []
		for center in centers:
			distances.append(distance((x[i],y[i]),(center[0],center[1])))
		print distances
			
def clusters((x,y), k, size=100):
	centers = [(random.randint(0,size), random.randint(0,size)) for i in range(k)]
	assign((x,y), centers)
	#for i in range(10):
		
	fig, ax = plt.subplots()
	ax.scatter(x,y)
	ax.set_ylim(-20,120)
	ax.set_xlim(-20,120)

	plt.show()




def generate_clusters(k, npoints=100, size=100, noise=10):
	points = [(int(math.cos(2*math.pi/k*x)*(size/2))+(size/2),int(math.sin(2*math.pi/k*x)*(size/2))+(size/2)) for x in xrange(0,k)]
	resx = []
	resy = []
	for i in range(npoints):
		orig = random.choice(points)
		resx.append(orig[0]+random.randint(-noise,noise))
		resy.append(orig[1]+random.randint(-noise,noise))
	return (resx, resy)
		




k=5
clusters(generate_clusters(k),k)




