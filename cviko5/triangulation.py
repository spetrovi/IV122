import sys, math
from random import choice
from PIL import Image, ImageDraw
def combinations(lis, k):
	result = []
	if k == 0:
		return [[]]
	else:
		for i in range(len(lis)):
			some_result = combinations(lis[i+1:], k-1)
			for item in some_result:
				result.append([lis[i]]+item)
	return result

def belongs_to((xC, yC), ((xA, yA), (xB, yB))):
	if (xA < xC <xB and xA < xB) or (yA < yC <yB and yA < yB) or (xB < xC <xA and xB < xA) or (yB < yC <yA and yB < yA):
		return True
	return False

def find_cross_point(((xA,yA),(xB,yB)), ((xC,yC),(xD,yD))):
	if ((xA-xB)*(yC-yD)-(yA-yB)*(xC-xD)) == 0 or ((xA-xB)*(yC-yD)-(yA-yB)*(xC-xD)) == 0: return False
	xP = ((xA*yB-yA*xB)*(xC-xD)-(xA-xB)*(xC*yD-yC*xD))/((xA-xB)*(yC-yD)-(yA-yB)*(xC-xD))
	yP = ((xA*yB-yA*xB)*(yC-yD)-(yA-yB)*(xC*yD-yC*xD))/((xA-xB)*(yC-yD)-(yA-yB)*(xC-xD))
	if belongs_to((xP,yP), ((xA, yA),(xB, yB))) and belongs_to((xP,yP),((xC,yC),(xD,yD))): return True
	return False
	

def have_cross_points(lines):
	pairs = combinations(lines,2)
	for item in pairs: 
		if find_cross_point(item[0],item[1]): return True
	return False


def draw_it(lines):
	size = 500
	im = Image.new('L', (size,size),255)
	draw = ImageDraw.Draw(im) 
	for line in lines: draw.line(line,fill=0)
	im.save('triangulation.png','png')
		
def generate_points(n):
	size = 500
	points = []
	for i in range(0,n):
		x = choice(range(size))
		y = choice(range(size))
		points.append((x,y))
	return points

def get_length(((xA,yA),(xB,yB))):
	return math.sqrt((xA-xB)**2+(yA-yB)**2)

def generate_sorted_lines(points):
	lines = map(lambda x: tuple(x), combinations(points,2))
	lines.sort(key=get_length)
	return lines
	
points = generate_points(20)
lines = generate_sorted_lines(points)

good_lines = []
for line in lines:
	if not have_cross_points(good_lines+[line]):
		good_lines += [line]
draw_it(good_lines)















