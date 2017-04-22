import math
from PIL import Image, ImageDraw

def row_multi(row1,row2):
	return sum(map(lambda x,y: x*y, row1,row2))

def matrix_multi(matrix, matrix2):
	print matrix
	print matrix2
	result = []
	columns = []
	for i in range(len(matrix2[0])):
		columns.append(map(lambda x: x[i], matrix2))
	for row in matrix:
		new_row = []
		for col in columns:
			new_row.append(row_multi(row,col))
		result.append(new_row)
	print result
	return result

def translate(x,y):
	return [[1,0,x],[0,1,-y],[0,0,1]]
def scale(x,y):
	return [[x,0,0],[0,y,0],[0,0,1]]
def rotate(angle):
#	angle = -angle
	return [[math.cos(math.radians(angle)), -math.sin(math.radians(angle)),0],[math.sin(math.radians(angle)),math.cos(math.radians(angle)),0],[0,0,1]]
def shear(k):
	return [[1,-k,0],[0,1,0],[0,0,1]]
def square(a):
	a = a/2
	return [[-a,-a,-a,a],[-a,-a,a,-a],[a,-a,a,a],[-a,a,a,a]]
def combine(ops):
	return reduce(lambda x,y: matrix_multi(x,y), list(reversed(ops)), [[1,0,0],[0,1,0],[0,0,1]])

def demo(it, transform, obj):
	size = 500
	im = Image.new('RGB', (size,size), (255,255,255))
	draw = ImageDraw.Draw(im)
	map(lambda (x1,x2,y1,y2): draw.line((x1+size/2,x2+size/2,y1+size/2,y2+size/2),fill=0),obj)
	for i in range(it):
		for i,line in enumerate(obj):
			point1 = matrix_multi(transform,[[line[0]],[line[1]],[1]])
			point2 = matrix_multi(transform,[[line[2]],[line[3]],[1]])
			obj[i] = [point1[0][0],point1[1][0],point2[0][0],point2[1][0]]
		map(lambda (x1,x2,y1,y2): draw.line((x1+size/2,x2+size/2,y1+size/2,y2+size/2),fill=0),obj)
	im.save('demo3.png','png')

#demo(25, combine([shear(1.3), rotate(10), scale(0.9,0.9), translate(20, 20)]), square(50))
#nahrad obrazok zmensenymi kopiami
obj = square(200)

c1 = combine([scale(0.5,0.5),rotate(90), translate(0,0.5)])
c2 = combine([scale(0.5,0.5),rotate(90), translate(-0.3,-0.25)])
c3 = combine([scale(0.5,0.5),rotate(90), translate(-0.3,0.25)])

cs = [c1,c2,c3]
size = 500
im = Image.new('RGB', (size,size), (255,255,255))
draw = ImageDraw.Draw(im)

for transform in cs:
	for i,line in enumerate(obj):
		point1 = matrix_multi(transform,[[line[0]],[line[1]],[1]])
		point2 = matrix_multi(transform,[[line[2]],[line[3]],[1]])
		obj[i] = [point1[0][0],point1[1][0],point2[0][0],point2[1][0]]
	map(lambda (x1,x2,y1,y2): draw.line((x1+size/2,x2+size/2,y1+size/2,y2+size/2),fill=0),obj)
im.save('frak.png','png')





