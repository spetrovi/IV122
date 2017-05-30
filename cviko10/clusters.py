import matplotlib.pyplot as plt
import math, random
import numpy as np
def color(i):
	colors = ['red', 'blue', 'yellow', 'green', 'brown', 'magenta', 'pink']
	return colors[i]

def show_clusters(assigned, k, original, size, noise):
	fig, ax = plt.subplots()
	for (xc,yc, i), p_list in sorted(assigned.items()):
		x = map(lambda x: x[0], p_list)
		y = map(lambda x: x[1], p_list)

		ax.scatter(x, y, color = color(i))
		ax.scatter(xc,yc, color = 'black', marker='v')

	ax.set_xlim(0-noise,size+noise)
	ax.set_ylim(0-noise,size+noise)

	for (x,y, i) in original:
		ax.scatter(x,y, color='black', marker='x')
	fig.set_size_inches(4, 3)
	plt.savefig('clusters/cluster_'+str(k)+'.png', bbox_inches = 'tight')
	plt.close()


def distance((x1,y1),(x2,y2)):
	return math.sqrt((x2-x1)**2+(y2-y1)**2)

def assign((x,y), centers):
	assigned = {}
	for center in centers:
		assigned[center] = []

	for i in range(len(x)):
		distances = []
		for (xc, yc, color) in centers:
			distances.append(distance((x[i],y[i]),(xc,yc)))
		assigned[centers[distances.index(min(distances))]].append((x[i],y[i]))
	return assigned

def update_centers(assigned):
	updated_centers = []

	for (xc, yc, i), p_list in assigned.items():
		if p_list:
 			x = int(np.mean(map(lambda x: x[0],p_list)))
			y = int(np.mean(map(lambda x: x[1],p_list)))
			updated_centers.append((x, y, i))
		else:updated_centers.append((xc, yc, i))
	updated_centers.sort()
	return updated_centers

def generate_clusters(k, option, noise, npoints=100, size=100):
	if option == 'circle':
		points = [(int(math.cos(2*math.pi/k*x)*(size/2))+(size/2),int(math.sin(2*math.pi/k*x)*(size/2))+(size/2), x) for x in xrange(0,k)]
	if option == 'random':
		points = [(random.randint(0,size), random.randint(0,size), i) for i in range(k)]	
	print points	
	resx = []
	resy = []
	for i in range(npoints):
		orig = random.choice(points)
		resx.append(orig[0]+random.randint(-noise,noise))
		resy.append(orig[1]+random.randint(-noise,noise))
	return (resx, resy), points

		
def clusters((x,y), original, k, noise, size=100,):
	centers = [(random.randint(0,size), random.randint(0,size), i) for i in range(k)]
#	centers = [(size/2+random.randint(0,20), size/2+random.randint(0,20)) for i in range(k)]
	print centers
	centers_old = None
	i = 0
	while centers_old != centers:
		centers_old = centers
		assigned = assign((x,y), centers)	
		show_clusters(assigned, i, original, size, noise)
		centers = update_centers(assigned)
		i += 1
	return i

def exps((k1,k2), noise, name)
	fig, ax = plt.subplots()
	for k in range(1,10):
		vals = []
		for i in range(100):
			points, original_points = generate_clusters(k, 'random', noise)
			vals.append(clusters(points, original_points, k, noise))
		ax.bar(k, np.mean(vals))
	ax.set_xlabel('Number of points')
	ax.set_ylabel('Iterations')
	plt.savefig(name+'_noise'+str(noise)+'.png')
	plt.close()



k = 5
noise = 20
points, original_points = generate_clusters(k, 'circle', noise)
clusters(points, original_points, k, noise)



