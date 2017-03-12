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

def 5star():
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


g = Korytnacka(500, (250,250))



for i in range(0,1000):
	g.left(angle)
	g.forward(forward)
	g.right(angle2+i*10)
	g.back(forward*kvocient2)
	g.right(angle2+i*10)
	g.forward(forward)
g.save('test/hokus2)

#21 92 5.73388719272 0.0
#17 17 81.8640773224 81.8640773224
#2 167 3.90874363068 27.3612054148
#10 19 2.604722665 10.41889066
#10 45 23.0952076297 207.856868667
#14 42 3.628828434 18.14414217
#17 52 4.38557557084 21.9278778542 15
#31, 14, 16
#11, 71, 12, 5
#10 172 65 2
#podobne cisla, rozdielne vysledky
#2 104 70 7
#2 101 66 8
#5 171 41 * vytvara retaz
"""

  547  mv hokus13_50_95.png toin/
  548  mv hokus2_175_68.png toin/
  561  mv hokus79_86_93_23.png ./toin/hokus2_79_86_93_23.png
  562  mv hokus25_67_7_9.png ./toin/hokus2_25_67_7_9.png
  576  mv hokus2_11_71_12_5.png toin/
  587  mv hokus2_10_172_65_2.png 
  588  mv hokus2_10_172_65_2.png toin/
  632  mv hokus3_2_101_66_8.png toin/
  633  mv hokus3_2_104_70_7.png toin/
  649  mv hokus4_7_175_70_2.png toin/
"""




























