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
def triangle(size,a):
	im = Image.new('L', (size,size), 255)
	x0 = 0
	y0 = 0
	y1 = y0+a
	y2 = y1
	x1 = x0-(a/2)
	x2 = x0+(a/2)
	print x1, x2
	for x in range(size):
		for y in range(size):
			if y <= size+x and x >= size-y and x < 300 and y < 400:
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
triangle(500,100)
#pruhy(150,5)
#chess(500,18)








