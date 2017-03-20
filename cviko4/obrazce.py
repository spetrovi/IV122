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

#n je pocet pruhov
def pruhy(size, n):
	im = Image.new('L', (size,size))
	for x in range(size):
		for y in range(size):
			z = math.sin(n*math.pi*x/size)+1
			color = int(255*z/2)
			im.putpixel((x,y), color)
	im.save('pruhy.png','png')


def kruhy(size, n):
	im = Image.new('L', (size,size),255)
	s2 = int(size/2)
	a=s2
	b=s2
	for r in range(size):
		t = 0.0
		z = math.sin((r*n)*math.pi/size)+1
		color = int(255*z/2)
		while t <= math.pi*2:
			x = int(a+r*math.cos(t))
			y = int(b+r*math.sin(t))
			if x < size-1 and y < size-1 and x > -1 and y > -1:
				im.putpixel((x,y), color)
			t += 0.001
	im.save('kruhy.png','png')

def change_color(color):
	if color == 255: return 0
	return 255

def chess(size, size_of_square, radius):
	im = Image.new('L',(size,size))
	color = 0
	outside = [True for x in range(len(radius))]
	for x in range(size):
		if x % size_of_square == 0:
			color = change_color(color)
		for y in range(size): 
			if y % size_of_square == 0:
				color = change_color(color)
			for i, r in enumerate(radius):
				if (x-size/2)**2 + (y-size/2)**2 > r**2 and not outside[i]:
					outside[i] = True
					color = change_color(color)
				if (x-size/2)**2 + (y-size/2)**2 < r**2 and outside[i]:
					outside[i] = False				
					color = change_color(color)
			im.putpixel((x,y),color)
	im.save('chess.png','png')
			
#full_circle(150,50)
#circle(150,50,5)
#spiral(500,100,3)
#ellipse_equation(500,20,5,3)
#triangle(300,250)
#pruhy(150,10)
kruhy(300, 20)
#chess(500, 18, [100, 50, 200, 150, 10, 250])








