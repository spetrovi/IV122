#umocnovanie na zlomok
#a^n mod k
#vypocet pi
#odmocniny-polenie intervalu sqrt(5)==> 2,2^2; 2.3^2...
from PIL import Image, ImageDraw
from kombinatorika import combinations

def draw_square(pos, size, square):
	colors = [(255,0,0), (0,0,255), (0,255,0), (0,255,255), (255,0,255), (125,0,125), (255,125,125), (0,125,125), (50,125,0)]
	for x in range(pos[0]-size/2, pos[0]+size/2):
		for y in range(pos[1]-size/2, pos[1]+size/2):
			pixels[x,y] = colors[square%9]

def slow_rows(n):
	result = []
	for i in range(0,n+1):
		row = []
		for j in range(0,i+1):
			row.append(len(combinations(range(i),j)))
		result.append(row)
	return result

def quick_rows(n):
	result = []
	prev_row = []
	for i in range(1,n):
		row = []
		for j in range(0,i):
			if j == 0 or j == i-1:
				row.append(1)
			else:
				row.append(prev_row[j]+prev_row[j-1])
		prev_row = row[:]
		result.append(row)
		#print result
	return result
sqrsize = 10
size = 1000
x = size/2
y = sqrsize/2
im = Image.new('RGB', (size, size), 'white')

pixels = im.load()

n = 100
num_list = quick_rows(n)
print num_list
for row in num_list:
	y+=sqrsize
	x = size/2-sqrsize/2*len(row)
	for square in row:
		draw_square((x,y), sqrsize, square)
		x+=sqrsize

im.save('mod9.png','png')
