from PIL import Image, ImageDraw 
import math

def full_circle(size,r):
	im = Image.new('L', (size,size))
	for x in range(size):
		for y in range(size):
			if (x-size/2)**2 + (y-size/2)**2 == r**2:
				im.putpixel((x,y), 0)
			else:
				im.putpixel((x,y), 255)
	im.show()

def circle(size,r,brush):
	im = Image.new('L', (size,size))
	for x in range(size):
		for y in range(size):
			if (x-size/2)**2 + (y-size/2)**2 < r**2 and (x-size/2)**2 + (y-size/2)**2 > (r-brush)**2:
				im.putpixel((x,y), 0)
			else:
				im.putpixel((x,y), 255)
	im.show()

def spiral(size,r,brush):
	im = Image.new('L', (size,size),255)
	s2 = size/2
	x0=s2
	y0=s2
	for angle in range(0,360):
		x = x0 +int(math.cos(math.radians(angle)) * angle)
		y = y0 + int(math.sin(math.radians(angle)) * angle)
		im.putpixel((x,y),0)
	im.show()

"""
	angle = 0.0
	radius = 0.0
	while radius < r:
		im.putpixel((int(x+radius*math.sin(angle)),int(y+radius*math.cos(angle))),0)
		radius += 0.1
		angle += math.pi*10
"""
	

def pruhy(size,n):
	im = Image.new('L', (size,size))
	for x in range(size):
		for y in range(size):
			z = math.sin(n * 2 * math.pi * x/size)
			color = int(255 * (z + 1) / 2)
			im.putpixel((x,y), color)
	im.show()

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
		

	
	im.show()
			
#full_circle(150,50)
#circle(150,50,5)
spiral(1000,50,5)
#pruhy(150,5)
#chess(500,18)








