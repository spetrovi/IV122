from PIL import Image
from random import choice,randint
from cviko3T import Korytnacka
import math



def chaos_game(n):
	size = 301
	c = -1
	im = Image.new('L',(size,size),255)
	points = [(int(math.cos(2*math.pi/n*x)*(size/2))+(size/2),int(math.sin(2*math.pi/n*x)*(size/2))+(size/2)) for x in xrange(0,n)]
	point = (randint(0,300),randint(0,300))
	for i in range(2000):
		abc_point = choice(points)
		point = ((point[0] + abc_point[0])/5, (point[1] + abc_point[1])/5)
		if i > 100:
			im.putpixel(point,0)
		if i % 100 == 0:
			c+=1
			#im.save('./chaos/'+str(c)+'.png','png')
	im.show()


class Lsystem:
   def __init__(self, axiom, rules,angle,level,start_position,start_angle,length):
      self.instructions = axiom
      self.rules = rules
      self.length = length
      self.angle = angle
      self.start_angle = start_angle
      self.g = Korytnacka(700,start_position)
      self.level = level
      self.variables = self.identify_variables()

   def item_in_variables(self, item):
	_is = -1
	for i in range(0,len(self.variables)):
		if item == self.variables[i]:
			_is = i
	return _is

#rewrite with lambda abstractions
   def identify_variables(self):
	variables = []
	for item in self.rules:
		variables.append(item[0])
	return variables

   def rewrite(self):
	new_instructions = []	
	for item in self.instructions:
		position = self.item_in_variables(item)
		if position == -1:
			new_instructions.append(item)
		else:
			new_instructions += self.rules[position][1:]
	self.instructions = list(new_instructions)

	return self.instructions

   def grow_it(self):
	for i in range(0,self.level):
		self.rewrite()

   def draw_it(self):
	eval('self.g.left('+str(self.start_angle)+')')
	i = 0
	for item in self.instructions:
		if item == 'F' or item == 'A' or item == 'B'  or item == 'O' or item == 'P' or item == 'N' or item == 'M':
			i+=1
			item = 'self.g.forward('+str(self.length)+')'
			#self.g.save('./exp/'+str(i))
		if item == '+':
			item = 'self.g.right('+str(self.angle)+')'
		if item == '-':
			item = 'self.g.left('+str(self.angle)+')'
		if item == '[':
			item = 'self.g.push()'
		if item == ']':
			item = 'self.g.pop()'
		if item != 'X' and item != 'Y' and item != '':

			eval(item)
		#eval(item)

   def evaluate_string(self):
	self.instructions = self.instructions.split(' ')
	new_rules = []
	for item in self.rules:
		new_rules += [item.split(' ')]
	self.rules = list(new_rules)
	
   def display(self):
	self.g.display() 
   def save(self,name):
	self.g.save(name)


#g.display()

#l = Lsystem('A',['F F F','A F [ - A ] + A'],45,7,(350,600),90,5)
#l = Lsystem('F - - F - - F', ['F F + F - - F + F'],60,4,(150,450),0,5)#koch
#l = Lsystem('A',['A + B - A - B +', 'B - A + B + A -'],60,6,(500,450),180,7)#sier
#l = Lsystem('X',['X F - [ [ X ] + X ] + F [ + F X ] - X','F F F'],25,6,(350,660),90,4) #algae
#l = Lsystem('F',['F F [ + F ] F [ - F ] [ F ]'],25.7,5,(350,660),90,10) #plant
#l = Lsystem('F',['F F F - [ - F + F + F ] + [ + F - F - F ]'],20,4,(430,660),90,11)#plant2
#l = Lsystem('F',['F F [ + F ] F [ - F ] F'],25.7,4,(350,660),90,8) #plant3
#l = Lsystem('F + F + F + F',['F F F + F + F + F + F F'],90,4,(100,100),0,6)#box
#l = Lsystem('X F',['X X + Y F + + Y F - F X - - F X F X - Y F +', 'Y - F X + Y F Y F + + Y F + F X - - F X - Y', 'F F'],60,4,(150,250),90,7)#hex
#l = Lsystem('F + F + F + F',['F F F + F + F + F + F + F - F'],90,4,(450,150),0,3)#ring
#l = Lsystem('F - F - F - F',['F F - F + F + F - F'],90,4,(100,600),0,6)#box 2
#l = Lsystem('F + F + F + F',['F F F + F + + F + F'],90,5,(100,100),0,2)#crystal
#l = Lsystem('[ N ] + + [ N ] + + [ N ] + + [ N ] + + [ N ]',['M O A + + P A - - - N A [ - O A - - - M A ] + +','N + O A - - P A [ - - M A - - N A ] +','O - M A + + N A [ + + + O A + + P A ] -','P - - O A + + + + M A [ + P A + + + + N A ] - - N A'],36,6,(350,350),0,9)#penrose tiling
#l = Lsystem('X',['X + Y F - X F X - F Y +','Y - X F + Y F Y + F X -','F F'],90,7,(30,30),0,5)#hilbert
#l = Lsystem('X',['X F [ + X ] F [ - X ] + X ','F F F'],20,6,(350,660),90,5) #plant4
#l = Lsystem('X',['X F [ + X ] [ - X ] F X','F F F'],25.7,6,(350,660),90,5) #plant5
l = Lsystem('F',['F F [ + F ] F [ - F ] [ F ]'],20,5,(350,660),90,10) #plant6
l.evaluate_string()
l.grow_it()
l.draw_it()
l.display()
l.save('./cviko6/plant')
#chaos_game(6)



