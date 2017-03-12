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
    	self.draw.line((self.x,self.y, new_x,new_y),fill=255)
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

from random import randint
def r(angle):
	forward = (math.sin(math.radians(angle))*randint(10, 400))
	return forward
	 
g = Korytnacka(500, (250,250))

angle = randint(10,21)
kvocient = randint(13,17)
forward = math.sin(math.radians(angle))*kvocient
angle2 = randint(25,35)
back = forward*randint(1,3)
for i in range(0,1000):
	g.left(angle)
	g.forward(forward)
	g.right(angle2+i*10)
	g.back(back)
	g.right(angle2+i*10)
	g.forward(forward)
print angle, angle2, forward, back, kvocient
g.save('hokus')




#21 92 5.73388719272 0.0
#17 17 81.8640773224 81.8640773224
#2 167 3.90874363068 27.3612054148
#10 19 2.604722665 10.41889066
#10 45 23.0952076297 207.856868667
#14 42 3.628828434 18.14414217
#17 52 4.38557557084 21.9278778542 15






























