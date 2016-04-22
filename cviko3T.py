import sys,math
from PIL import Image, ImageDraw

class Korytnacka:
   

   def __init__(self, size):
      self.size = size
      self.x = 400
      self.y = 630
      self.im = Image.new('RGB', (size, size), (255,255,255))
      self.draw = ImageDraw.Draw(self.im) 
      self.angle = 0
      self.pen = 1
      self.stack = []

   def forward(self,length):

    new_x = self.x + int(math.cos(math.radians(self.angle)) * length)
    new_y = self.y + int(math.sin(math.radians(self.angle)) * length)
    if self.pen == 1:    
	self.draw.line((self.x,self.y, new_x,new_y),fill=0)
    self.x = new_x
    self.y = new_y
    
   def back(self,length):
    new_x = self.x - int(math.cos(math.radians(self.angle)) * length)
    new_y = self.y - int(math.sin(math.radians(self.angle)) * length)
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

def forward(k):
  return g.forward(k)

def left(k):
  return g.left(k)

def right(k):
  return g.right(k)

def back(k):
  return g.back(k)

def penup():
  return g.penup()

def pendown():
  return g.pendown()

def done():
  return g.done()

def push():
  return g.push()

def pop():
  return g.pop()

def tree(length, min_length=1):
    forward(length)
    if length > min_length:
        left(45)
        tree(0.6*length, min_length)
        right(90)
        tree(0.6*length, min_length)
        left(45)
    back(length)


def kochside(length, levels):
    if levels == 0:
        forward(length)
        return
    length /= 3.0
    kochside(length, levels-1)
    left(60)
    kochside(length, levels-1)
    right(120)
    kochside(length, levels-1)
    left(60)
    kochside(length, levels-1)

def kochflake(level):
	for i in range(3):
        	kochside(100*level, level)
        	right(120)

def sier(length, level):
    if level == 1:
        for i in range(3):
            forward(length)
            left(120)
    else:
        sier(length/2, level-1)
        forward(length/2)
        sier(length/2, level-1)
        back(length/2)
        left(60)
        forward(length/2)
        right(60)
        sier(length/2, level-1)
        left(60)
        back(length/2)
        right(60)


def pent_side(length,level):
	if level == 0:
        	forward(length/5)
        	return
	length /= 5
	pent_side(length,level-1)
	right(72)
	pent_side(length,level-1)

	left(36)
	pent_side(length,level-1)
	penup()
	left(180)
	pent_side(length,level-1)
	right(180)
	pendown()
	
	#department of redundancy department
	right(144-36)
	pent_side(length,level-1)
	penup()
	left(180)
	pent_side(length,level-1)
	right(180)
	pendown()
	left(144-36)
	
	left(144-36)
	pent_side(length,level-1)
	right(72)
	pent_side(length,level-1)

def pentaflake(level):
	for i in range(5):
		pent_side(1000,level)
		right(72)

	

#turtle.speed(0)
#left(90)
#tree(50)

#penup()
#back(200)
#pendown()
#pentaflake(3)
#kochflake(4)
#g = Korytnacka(500)

#g.display()
#turtle.exitonclick()





































