import sys,math
from PIL import Image, ImageDraw
from random import randint

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

def star():
	g = Korytnacka(500, (250,250))

	angle = 10
	angle2 = 170
	kvocient = 50
	kvocient2 = 2

	forward = math.sin(math.radians(angle))*kvocient
	for i in range(0,1000):
		g.left(angle)
		g.forward(forward)
		g.right(angle2+i*10)
		g.back(forward*kvocient2)
		g.right(angle2+i*10)
		g.forward(forward)
	g.save('test/hokus_'+str(angle)+'_'+str(angle2)+'_'+str(kvocient)+'_'+str(kvocient2))

def loghokus():
	g = Korytnacka(500, (250,250))

	a = randint(0,10)
	forward = math.log10(a)
	angle = randint(0,90)
	print a, angle
	for i in range(0,1000):
		g.left(angle)
		g.forward(math.log10(forward**i))
	g.save('test/loghokus_'+str(a)+'_'+str(angle))



g = Korytnacka(500, (250,250))

a = randint(0,10)
forward = a
angle = randint(0,90)
print a, angle
for i in range(0,1000):
	g.left(math.tan(math.radians(angle+10*i)))
	g.forward(forward)
g.save('test/radhokus_'+str(a)+'_'+str(angle))






















