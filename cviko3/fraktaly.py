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
      self.pen = True
      self.stack = []
      self.counter = 0
      self.draw_process = False

   def forward(self,length):
    new_x = float(self.x + math.cos(math.radians(self.angle)) * length)
    new_y = float(self.y + math.sin(math.radians(self.angle)) * length)
    if self.pen:    
	self.draw.line((self.x, self.y, new_x, new_y), fill = 0)
    self.x = new_x
    self.y = new_y
    if self.draw_process:
	self.counter += 1
    	self.save('sier'+str(self.counter))
    
   def back(self,length):
    new_x = float(self.x - math.cos(math.radians(self.angle)) * length)
    new_y = float(self.y - math.sin(math.radians(self.angle)) * length)
    if self.pen:
    	self.draw.line((self.x, self.y, new_x, new_y), fill = 255)
    self.x = new_x
    self.y = new_y
    if self.draw_process:
	self.counter += 1
    	self.save('sier'+str(self.counter))
    
    
   def left(self,angle):
      self.angle -= angle
   def right(self,angle):
      self.angle += angle
    
   def draw_all(self):
	self.draw_process = True

   def penup(self):
	self.pen = False
   
   def pendown(self):
	self.pen = True

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



def tree(g,length, min_length=1):
    g.forward(length)
    if length > min_length:
        g.left(45)
        tree(g,0.6*length, min_length)
        g.right(90)
        tree(g,0.6*length, min_length)
        g.left(45)
    g.back(length)


def kochside(g,length, levels):
    if levels == 0:
        g.forward(length)
        return
    length /= 3.0
    kochside(g,length, levels-1)
    g.left(60)
    kochside(g,length, levels-1)
    g.right(120)
    kochside(g,length, levels-1)
    g.left(60)
    kochside(g,length, levels-1)

def kochflake(level):
	g = Korytnacka(500,(50,150))
	for i in range(3):
        	kochside(g,450, level)
        	g.right(120)
	g.display()
	g.save('kochflake')

def sierpinsky(level):
	g = Korytnacka(500,(30,450))
	#g.draw_process = True
	sier(g, 450, level)
        g.save('sierpinsky')

def sier(g, side, level):
    if level == 1:
	g.pendown()
        for i in range(0,3):
            g.forward(side)
            g.left(120)
	g.penup()

    else:
	side /= 2
	g.penup()
        sier(g, side, level-1)
        g.forward(side)
        sier(g, side, level-1)
	g.back(side)
	g.left(60)
        g.forward(side)
        g.right(60)
        sier(g, side, level-1)
	g.left(60)
	g.back(side)
	g.right(60)

def pent_side(g,length,level):
	if level == 0:
        	g.forward(length/5)
        	return
	length /= 5
	pent_side(g,length,level-1)
	g.right(72)
	pent_side(g,length,level-1)

	g.left(36)
	pent_side(g,length,level-1)
	g.penup()
	g.left(180)
	pent_side(g,length,level-1)
	g.right(180)
	g.pendown()
	
	#department of redundancy department
	g.right(144-36)
	pent_side(g,length,level-1)
	g.penup()
	g.left(180)
	pent_side(g,length,level-1)
	g.right(180)
	g.pendown()
	g.left(144-36)
	
	g.left(144-36)
	pent_side(g,length,level-1)
	g.right(72)
	pent_side(g,length,level-1)

def pentaflake(level):
	g = Korytnacka(500,(150,100))
	for i in range(5):
		pent_side(g,8000,level)
		g.right(72)
	g.display()
	g.save('pentaflake')
	g.show()

def draw_tree(level):
	g = Korytnacka(500,(250,400))
	g.left(90)
	tree(g,level)
	g.display()
	g.save('tree')

#pentaflake(2)
#kochflake(4)
#sierpinsky(8)
#draw_tree(150)








































