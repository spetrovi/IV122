import math
from random import choice
from PIL import Image, ImageDraw

def draw_it(points, edge):
	size = 500
	im = Image.new('L', (size,size),255)
	draw = ImageDraw.Draw(im) 
	for point in points:
		for x in range(point[0]-2,point[0]+2):
			for y in range(point[1]-2,point[1]+2):
				im.putpixel((x,y),0)
	for i in range(0,len(edge)-1):
		draw.line((edge[i][0],edge[i][1],edge[i+i][0],edge[i+1][1]),fill=0)
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
	ratio = 0
	good_point = None
	points.remove((x,y))
	for point in points:
		print 'kokotpica'
		print good_point
		print point
		print abs(float((point[0]-x))/float((point[1]-y)))
		print ratio
		print abs(float((point[0]-x))/float((point[1]-y))) > ratio
		if abs(float((point[0]-x))/float((point[1]-y))) > ratio:
			ratio = abs(float((point[0]-x))/float((point[1]-y)))
			print 'was true'
			print point
			good_point = (point[0],point[1])
			print good_point
	print 'so return'
	print good_point
	return good_point

points = generate_points(5)
points.sort(key=lambda (x,y): x)

points_on_edge = []
current_point = points[0]
first_point = current_point
new_point = None


while new_point != first_point:
	new_point = nice_point(current_point, points)
	print new_point
	current_point = new_point
	points_on_edge.append(new_point)
draw_it(points, points_on_edge)
	















