import sys,math
from PIL import Image, ImageDraw

class Korytnacka:
   def __init__(self, size,start_position):
      self.size = size
      self.x = start_position[0]
      self.y = start_position[1]
      self.im = Image.new('RGB', (size, size), (255,255,255))
      self.draw = ImageDraw.Draw(self.im) 
      self.angle = 0
      self.pen = 1
      self.stack = []

   def forward(self,length):

    new_x = self.x + math.cos(math.radians(self.angle)) * length
    new_y = self.y + math.sin(math.radians(self.angle)) * length
    if self.pen == 1:    
	self.draw.line((self.x,self.y, new_x,new_y),fill=0)
    self.x = new_x
    self.y = new_y
    
   def back(self,length):
    new_x = self.x - math.cos(math.radians(self.angle)) * length
    new_y = self.y - math.sin(math.radians(self.angle)) * length
    if self.pen == 1:
    	self.draw.line((self.x,self.y, new_x,new_y),fill=0)
    self.x = new_x
    self.y = new_y
    
    
   def left(self,angle):
      self.angle -= angle
   def right(self,angle):
      self.angle += angle
    

   def penup(self):
	self.pen = 0
   
   def pendown(self):
	self.pen = 1

   def display(self):
    self.im.show()

   def push(self):
	self.stack.append((self.x, self.y, self.angle))

   def pop(self):
	 tupple = self.stack.pop()
	 self.x = tupple[0]
  	 self.y = tupple[1]
	 self.angle = tupple[2]
   
   def save(self,name):
	self.im.save(name+'.png','png')


#pentagram dvoma sposobmi
#dalsie- mozes si vybrat
#sekvencia nahodnych pohybov 100 krat opakovat-zaujimave obrazky

def pentagram_relativne(size, position, side):
		inside_angle = 180-(360/5)
		pentagram_angle = (180 - inside_angle)/2 #rovnoramenny trojuholnik. Sucet uhlov trojuholnika je 180
		long_side = int(2*(side*math.cos(math.radians(pentagram_angle))))
		g = Korytnacka(size, position)
		g.right(180+72)
		for i in range(0,5):
			g.right(180-pentagram_angle)
			g.forward(side)
			g.right(180-pentagram_angle)
			g.forward(long_side)
		g.save('pentagram_relativne')

def pentagram_absolutne(size, ratio):
		im = Image.new('RGB', (size, size), (255,255,255))
		draw = ImageDraw.Draw(im) 

		x1, y1 = 250, 250
		
		points = [(int(math.cos(2*math.pi/5*x)*ratio)+x1,int(math.sin(2*math.pi/5*x)*ratio)+y1) for x in xrange(0,5)]
		points2 = points[:]
		for point in points:
			for point2 in points2:
				draw.line((point[0], point[1], point2[0],point2[1]), fill = 0)
			points2.pop(0)
		im.save('pentagram_absolutne.png','png')

def draw_square(g, side):
	for i in range(0,4):
		g.forward(side)
		g.right(90)


def spiral(size, position, side, constant):
	g = Korytnacka(size, position)
	draw_square(g, side)
	angle = math.degrees(math.acos((side - constant*side)/(constant*side)))
	for i in range(1, 35):	
		g.forward(side-side*constant)
		side = side * constant
		g.right(90-angle)
		draw_square(g, side)
	g.save('spirala')

def grid(size, ratio, fineness):
	im = Image.new('RGB', (size, size), (255,255,255))
	draw = ImageDraw.Draw(im) 
	x1, y1 = 250, 50
	x2, y2 = x1-ratio-fineness, y1+ratio+fineness
	for i in range(0, 2*ratio/fineness+1):
		v = ratio - i*fineness

		length = math.sqrt((ratio**2)-v**2)
		y1 = y1+fineness
		draw.line((x1-length, y1, x1+length, y1), fill = 0)
	
		x2 = x2+fineness
		draw.line((x2, y2-length, x2, y2+length), fill = 0)
	im.save('grid.png','png')

def triangles(size, side, fineness):
	im = Image.new('RGB', (size, size), (255,255,255))
	draw = ImageDraw.Draw(im)
	x1, y1, x2, x3, y2 = 250, 250, 250, 250, 250
	#pomocou pytagorovej vety vypocitam stranu trojuholnika podla vysky
	hside = 0
	while 2*hside < side:
		y1 -= 2*fineness
		y2 += fineness
		v = y2 - y1
		hside = v/math.atan(60)
		x2 = x1 - hside
		x3 = x1 + hside 
		draw.line((x1, y1, x2, y2), fill = 0)
		draw.line((x1, y1, x3, y2), fill = 0)
		draw.line((x3, y2, x2, y2), fill = 0)
	im.save('triangles.png','png')


def penrose(size, fineness):
		side = (size/10) - fineness
		position = (250, 250)
		inside_angle = 360/fineness
		g = Korytnacka(size, position)
		g.right(180+72)
		for i in range(0, fineness):
			for j in range(0,fineness):
				g.right(inside_angle)
				g.forward(side)
			g.right(inside_angle)
		g.save('penrose')
	

penrose(500, 18)
#triangles(500, 400, 5)
#pomocou pytagorovej vety sa spocita dlzka tetivy
#grid(500, 200, 10)
#side > new_side > sqrt(2*(side/2)^2)<---pytagorova veta
#Pre lubovolnu kostantu z intervalu (side, sqrt(2*(side/2)^2)) sa pomocou acos() dopocita potrebny uhol
spiral(500, (25,25), 450, 0.88)
#pentagram_relativne(500, (250, 100), 200)
#pentagram_absolutne(500, 200)




































