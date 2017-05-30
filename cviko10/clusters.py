import matplotlib.pyplot as plt
import math, random
import numpy as np
def color(i):
	colors = ['red','blue','yellow', 'green','brown']
	return colors[i]

def show_clusters(assigned, k):
	fig, ax = plt.subplots()
	i = 0
	for (xc,yc), p_list in assigned.items():
		x = map(lambda x: x[0], p_list)
		y = map(lambda x: x[1], p_list)
		ax.scatter(x, y, color = color(i))
		ax.scatter(xc,yc, color = 'black')		
		i += 1

	ax.set_ylim(-20,120)
	ax.set_xlim(-20,120)
#	plt.show()
	plt.savefig('cluster_'+str(k)+'.png')
	plt.close()


def distance((x1,y1),(x2,y2)):
	return math.sqrt((x2-x1)**2+(y2-y1)**2)

def assign((x,y), centers):
	assigned = {}
	for (xc, yc) in centers:
		print(xc, yc)
		assigned[(xc,yc)] = []

	for i in range(len(x)):
		distances = []
		for (xc, yc) in centers:
			distances.append(distance((x[i],y[i]),(xc,yc)))
		assigned[centers[distances.index(min(distances))]].append((x[i],y[i]))
	return assigned

def update_centers(assigned):
	updated_centers = []
	for center, p_list in assigned.items():
		x = int(np.mean(map(lambda x: x[0],p_list)))
		y = int(np.mean(map(lambda x: x[1],p_list)))
		updated_centers.append((x, y))
	return updated_centers

def clusters((x,y), k, size=100):
	centers = [(random.randint(0,size), random.randint(0,size)) for i in range(k)]
	centers_old = None
	i = 0
	while centers_old != centers:
		centers_old = centers	
		assigned = assign((x,y), centers)	
		show_clusters(assigned, i)
		centers = update_centers(assigned)
		i += 1





def generate_clusters(k, npoints=100, size=100, noise=10):
	points = [(int(math.cos(2*math.pi/k*x)*(size/2))+(size/2),int(math.sin(2*math.pi/k*x)*(size/2))+(size/2)) for x in xrange(0,k)]
	resx = []
	resy = []
	for i in range(npoints):
		orig = random.choice(points)
		resx.append(orig[0]+random.randint(-noise,noise))
		resy.append(orig[1]+random.randint(-noise,noise))
	return (resx, resy)

		




k = 5
clusters(generate_clusters(k),k)




