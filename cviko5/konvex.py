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

def nice_point((x,y), points):
	good_point = (points[0][0], points[0][1])
	ratio = abs(points[0][0]-x)/abs(points[0][1]-y)
	print abs(points[0][0]-x)
	print abs(points[0][1]-y)
	print ratio
	angle = math.tan(math.radians(0.75))
	print angle
	print points
	print (x,y)
	for point in points:
		#print point
		print abs(point[0]-x)/abs(point[1]-y)
		if abs(point[0]-x)/abs(point[1]-y) < ratio:
			ratio = abs(point[0]-x)/abs(point[1]-y)
			good_point = (point[0],point[1])
	print good_point
	return good_point

points = generate_points(5)
points.sort(key=lambda (x,y): x)

points = [(36, 244), (77, 344), (143, 257), (250, 164), (269, 347)]
points_on_edge = [points[0]]
current_point = points[0]
first_point = current_point
draw_p(points)
points.remove(first_point)
for i in range(0,4):
	new_point = nice_point(current_point, points[:])
	current_point = new_point
	points.remove(new_point)
	points_on_edge.append(new_point)
print points_on_edge
draw_it([(36, 244), (77, 344), (143, 257), (250, 164), (269, 347)], points_on_edge)
	















