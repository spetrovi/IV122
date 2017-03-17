from PIL import Image, ImageDraw 
import math

def full_circle(size,r):
	im = Image.new('L', (size,size))
	for x in range(size):
		for y in range(size):
			if (x-size/2)**2 + (y-size/2)**2 <= r**2:
				im.putpixel((x,y), 0)
			else:
				im.putpixel((x,y), 255)
	im.save('full_circle.png','png')

def circle(size,r,brush):
	im = Image.new('L', (size,size))
	for x in range(size):
		for y in range(size):
			if (x-size/2)**2 + (y-size/2)**2 < r**2 and (x-size/2)**2 + (y-size/2)**2 > (r-brush)**2:
				im.putpixel((x,y), 0)
			else:
				im.putpixel((x,y), 255)
	im.save('circle.png','png')

#t e 0,2pi
#x = a+rcost
#y = b+rsint
def circle_param(size,r,brush):
	im = Image.new('L', (size,size),255)
	s2 = int(size/2)
	a=s2
	b=s2
	t = 0.0
	while t <= math.pi*2:
		x = int(a+r*math.cos(t))
		y = int(b+r*math.sin(t))
		im.putpixel((x,y), 0)
		t += 0.001
	
	im.save('circle_param.png','png')

def draw_square(pixels, pos, size):
	for x in range(pos[0]-size/2, pos[0]+size/2):
		for y in range(pos[1]-size/2, pos[1]+size/2):
			pixels[x,y] = 0
	

def spiral(size,r,brush):
	im = Image.new('L', (size,size),255)
	pixels = im.load()
	a = int(size/2)
	b = int(size/2)
	t = 0
	nr = 0
	while nr < r:
		x = int(a+(nr)*math.cos(t))
		y = int(b+(nr)*math.sin(t))
		draw_square(pixels,(x,y),brush)
		
		nr += 0.002
		t += 0.001
	im.save('spiral.png','png')

def ellipse_equation(size,r,a,b):
	im = Image.new('L', (size,size))
	x0 = size/2
	y0 = size/2
	for x in range(size):
		for y in range(size):
			if ((x-x0)/a)**2 + ((y-y0)/b)**2 <= r**2:
				im.putpixel((x,y), 0)
			else:
				im.putpixel((x,y), 255)
	im.save('ellipse_equation.png','png')

#y <= -sqrt(3)x+a(sqrt(3)/2)
#y = kx +l
#0 = k*a/2 + a*sqrt(3)/2
#k = -sqrt3
#mnohouholnik, pospajame ciary bodov co su zasebou
def triangle(size,a):
	im = Image.new('L', (size,size), 255)
	x0 = 250
	y0 = 50
	y1 = y0+a
	for x in range(size):
		for y in range(size):
			if y >= -math.sqrt(3)*(x-x0) + math.sqrt(2)/3+y0 and y >= math.sqrt(3)*(x-x0)+math.sqrt(2)/3+y0 and y < y1:
				im.putpixel((x,y),0)
				

	im.save('triangle.png','png')

def pruhy(size,n):
	im = Image.new('L', (size,size))
	for x in range(size):
		for y in range(size):
			z = math.sin(n * 2 * math.pi * x/size)
			color = int(255 * (z + 1) / 2)
			im.putpixel((x,y), color)
	im.save('pruhy.png','png')

def change_color(color):
	if color == 255:
		return 0
	else:
		return 255




def belongs_to(point, line):
	xA = line[0][0]
	yA = line[0][1]
	xB = line[1][0]
	yB = line[1][1]
	xC = point[0]
	yC = point[1]
	#if point == line[0] or point == line[1]: return True
	if (xA < xC < xB and xA < xB) or (yA < yC <yB and yA < yB) or (xB < xC <xA and xB < xA) or (yB < yC <yA and yB < yA):
		return True
	return False
def find_cross_points(line1, line2):
	xA = line1[0][0]
	yA = line1[0][1]
	xB = line1[1][0]
	yB = line1[1][1]
	xC = line2[0][0]
	yC = line2[0][1]
	xD = line2[1][0]
	yD = line2[1][1]
	if ((xA-xB)*(yC-yD)-(yA-yB)*(xC-xD)) == 0 or ((xA-xB)*(yC-yD)-(yA-yB)*(xC-xD)) == 0: return (None)
	xP = ((xA*yB-yA*xB)*(xC-xD)-(xA-xB)*(xC*yD-yC*xD))/((xA-xB)*(yC-yD)-(yA-yB)*(xC-xD))
	yP = ((xA*yB-yA*xB)*(yC-yD)-(yA-yB)*(xC*yD-yC*xD))/((xA-xB)*(yC-yD)-(yA-yB)*(xC-xD))
	if belongs_to((xP,yP),line1) and belongs_to((xP,yP),line2): 
		return (xP,yP)

def polygon(size, points):
	im = Image.new('L',(size,size))
	lines = []
	for i in range(0,len(points)-1):
		lines.append((points[i], points[i+1]))
	lines.append((points[i+1],points[0]))
	for y in range(size):
		color = 255
		cross_points = []
		for line in lines:
			cross_points.append(find_cross_points(line, ((0,y),(size,y))))
		cross_points = filter(lambda x: x!=None, cross_points)
		if len(cross_points) % 2 == 1:#ak je neparny pocet cross points, algoritmus zrejme vynechal nejaky vrchol
			cross_points += points
		for x in range(size):
			if (x,y) in cross_points:
				color = change_color(color)
			im.putpixel((x,y),color)
	im.save('polygon.png','png')
	
def chess(size,size_of_square):
	im = Image.new('L',(size,size))
	color = 0
	previous_inside_test = 1
	previous_inside_test2 = 1
	previous_inside_test3 = 1
	for x in range(size):
		if x % size_of_square == 0:
			color = change_color(color)
		for y in range(size): 
			if y % size_of_square == 0:
				color = change_color(color)
			if (x-size/2)**2 + (y-size/2)**2 < 100**2 and previous_inside_test == 0:
				previous_inside_test = 1
				color = change_color(color)
			if (x-size/2)**2 + (y-size/2)**2 > 100**2 and previous_inside_test == 1:
				previous_inside_test = 0				
				color = change_color(color)

			if (x-size/2)**2 + (y-size/2)**2 < 200**2 and previous_inside_test2 == 0:
				previous_inside_test2 = 1
				color = change_color(color)
			if (x-size/2)**2 + (y-size/2)**2 > 200**2 and previous_inside_test2 == 1:
				previous_inside_test2 = 0				
				color = change_color(color)

			if (x-size/2)**2 + (y-size/2)**2 < 50**2 and previous_inside_test3 == 0:
				previous_inside_test3 = 1
				color = change_color(color)
			if (x-size/2)**2 + (y-size/2)**2 > 50**2 and previous_inside_test3 == 1:
				previous_inside_test3 = 0				
				color = change_color(color)


			im.putpixel((x,y),color)
		

	
	im.save('chess.png','png')
			
#full_circle(150,50)
#circle(150,50,5)
#spiral(500,100,3)
#ellipse_equation(500,20,5,3)
#triangle(300,250)
polygon(200,[(10, 10),(180, 20),(160, 150),(100, 50),(20, 180)])
#polygon(200,[(50, 50),(50, 100),(100, 100),(100,50)])
#pruhy(150,5)
#chess(500,18)







