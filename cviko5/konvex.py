from __future__ import division
import math
from random import choice
from PIL import Image, ImageDraw


def draw_p(points):
	size = 500
	im = Image.new('L', (size,size),255)
	draw = ImageDraw.Draw(im) 
	for point in points:
		for x in range(point[0]-2,point[0]+2):
			for y in range(point[1]-2,point[1]+2):
				im.putpixel((x,y),0)
	im.save('konvexP.png','png')

def draw_it(points, edge):
	size = 500
	im = Image.new('L', (size,size),255)
	draw = ImageDraw.Draw(im) 
	for point in points:
		for x in range(point[0]-2,point[0]+2):
			for y in range(point[1]-2,point[1]+2):
				im.putpixel((x,y),0)

	for i in range(0,len(edge)-1):
		draw.line((edge[i][0],edge[i][1],edge[i+1][0],edge[i+1][1]),fill=0)
	im.save('konvex.png','png')
		
def generate_points(n):
	size = 400
	points = []
	for i in range(0,n):
		x = choice(range(size))
		y = choice(range(size))
		points.append((x,y))
	return points

def get_x((x,y)):
	return x

def generate_sorted_lines(points):
	lines = map(lambda x: tuple(x), combinations(points,2))
	lines.sort(key=get_length)
	return lines

#ked y bodu 2 je mensia ako y bodu 1: x/y
#ked ybodu 2 je vacsia ako y bodu 1: y/x
#math.degrees(math.atan(abs(point[1]-y)/abs(point[0]-x)))+90
 # 2D cross product of OA and OB vectors, i.e. z-component of their 3D cross product.
 # Returns a positive value, if OAB makes a counter-clockwise turn,
def cross(o, a, b):
	return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])
def nice_point((x,y), points):
	points.remove((x,y))
	good_point = points[0]
	c = cross((x,y), (x,y+10), good_point)
	#if (good_point[1] > y and good_point[0] > x) or (good_point[1] < y and good_point[0] < x):
	#	c = math.degrees(math.atan(abs(good_point[0]-x)/abs(good_point[1]-y)))
	#else:
	#	c = math.degrees(math.atan(abs(good_point[1]-y)/abs(good_point[0]-x)))+90
	print 'kokotpica'	
	#print (x,y)
	for point in points:
		print point
		print cross((x,y), (x,y+10), point)
		if cross((x,y), (x,y+10), point) < 0 and cross((x,y), (x,y+10), point) > c:
		#if (point[1] > y and point[0] > x) or (point[1] < y and point[0] < x):
		#	angle = math.degrees(math.atan(abs(point[0]-x)/abs(point[1]-y)))
		#else:
		#	angle = math.degrees(math.atan(abs(point[1]-y)/abs(point[0]-x)))+90
		#print angle
		#if angle < c:
			good_point = point
			c = cross((x,y), (x,y+10), point)
		#	c = angle

	print good_point
	return good_point

points = generate_points(10)
points.sort(key=lambda (x,y): x)

points = [(36, 244), (77, 344), (143, 257), (250, 164), (300, 400)]
td = points[:]
points_on_edge = [points[0]]
current_point = points[0]
#points.append(current_point)
#first_point = current_point
#points.remove(first_point)
#print points
draw_p(points)

for i in range(0,4):
	#points.remove(current_point)
	current_point = nice_point(current_point, points[:])
	points_on_edge.append(current_point)
	print points

print points_on_edge
draw_it(td, points_on_edge)
	















