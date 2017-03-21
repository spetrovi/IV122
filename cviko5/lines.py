import sys, math
from random import randint
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

def make_line(x,y,size,length):
	x1 = -1
        y1 = -1
	while (x1 > size) or (x1 < 0) or (y1 < 0) or (y1 > size):
		angle=randint(0,360)
		x1 = x + int(math.cos(math.radians(angle)) * length)
        	y1 = y + int(math.sin(math.radians(angle)) * length)
	return (x,y,x1,y1)
		
def generate_lines(n):
	size = 500
	length = 300
	lines = []
	for i in range(0,n):
		x = randint(1,size)
		y = randint(1,size)
		line = make_line(x,y,size,length)
		lines.append(line)
	return lines

def belongs_to((xC, yC), (xA, yA, xB, yB)):
	if (xA < xC <xB and xA < xB) or (yA < yC <yB and yA < yB) or (xB < xC <xA and xB < xA) or (yB < yC <yA and yB < yA):
		return True
	return False

def find_cross_points((xA,yA,xB,yB), (xC,yC,xD,yD)):
	if ((xA-xB)*(yC-yD)-(yA-yB)*(xC-xD)) == 0 or ((xA-xB)*(yC-yD)-(yA-yB)*(xC-xD)) == 0: return None 
	xP = ((xA*yB-yA*xB)*(xC-xD)-(xA-xB)*(xC*yD-yC*xD))/((xA-xB)*(yC-yD)-(yA-yB)*(xC-xD))
	yP = ((xA*yB-yA*xB)*(yC-yD)-(yA-yB)*(xC*yD-yC*xD))/((xA-xB)*(yC-yD)-(yA-yB)*(xC-xD))
	if belongs_to((xP,yP), (xA,yA,xB,yB)) and belongs_to((xP,yP),(xC,yC,xD,yD)): return (xP,yP)
	

def find_all_cross_points(lines):
	pairs = combinations(lines,2)
	all_cross_points = []
	for item in pairs: all_cross_points.append(find_cross_points(item[0],item[1]))
	return filter(lambda x: x != None, all_cross_points)


def draw_it(lines,cross_points):
	size = 500
	im = Image.new('L', (size,size),255)
	draw = ImageDraw.Draw(im) 
	for line in lines: draw.line(line,fill=0)
	for point in cross_points:
		for x in range(point[0]-2,point[0]+2):
			for y in range(point[1]-2,point[1]+2):
				im.putpixel((x,y),0)
	im.show()
	im.save('lines.png','png')


lines = generate_lines(10)
all_cross_points = find_all_cross_points(lines)
draw_it(lines, all_cross_points)















