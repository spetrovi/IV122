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
		draw.line((edge[i][0],edge[i][1],edge[i+1][0],edge[i+1][1]),fill = 0)
	draw.line((edge[i+1][0],edge[i+1][1],edge[0][0],edge[0][1]), fill = 0)
	im.save('konvex.png','png')
		
def generate_points(n):
	size = 400
	points = []
	for i in range(0,n):
		x = choice(range(100,size))
		y = choice(range(100,size))
		points.append((x,y))
	return points

def get_x((x,y)):
	return x

#(C is on left of line from A to B)
def left((xA,yA),(x1,y1),(x2,y2)):
	v1 = (x2-x1, y2-y1)   # Vector 1
	v2 = (x2-xA, y2-yA)   # Vector 1
	xp = v1[0]*v2[1] - v1[1]*v2[0]  # Cross product
	if xp > 0:
    		return True
	return False

points = generate_points(100)
points.sort(key=lambda (x,y): x)

td = points[:]
point_on_hull = points[0]
endpoint = points[1]
points_on_edge = []

while endpoint != points[0]:
	points_on_edge.append(point_on_hull)
	endpoint = points[0]
	for point in points[1:]:
		if endpoint == point_on_hull or left(point, point_on_hull, endpoint):
			endpoint = point
	point_on_hull = endpoint
print points_on_edge
draw_it(td, points_on_edge)
	















