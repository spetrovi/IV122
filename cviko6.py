from PIL import Image
from random import choice,randint
from cviko3T import forward, back, left, right, done, penup, pendown, Korytnacka
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
   def __init__(self, axiom, rules,angle,level):
      self.instructions = axiom
      self.rules = rules
      self.length = 10
      self.angle = angle
      self.g = Korytnacka(700)
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
	#print self.instructions
	eval('self.g.left(90)')
	i = 0
	for item in self.instructions:
		
		
		if item == 'F' or item == 'A' or item == 'B':
			i+=1
			item = 'self.g.forward(11)'
			self.g.save('./exp/'+str(i))
		if item == '+':
			item = 'self.g.right('+str(self.angle)+')'
		if item == '-':
			item = 'self.g.left('+str(self.angle)+')'
		if item == '[':
			item = 'self.g.push()'
		if item == ']':
			item = 'self.g.pop()'
		if item != 'X':
			eval(item)
		#eval(item)

   def display(self):
	self.g.display() 
   def save(self,name):
	self.g.save(name)


#to run L-system, iterate through list of intstructions with eval(instruction)
#g.display()

#l = Lsystem(['A'],[('F','F','F'),('A','F','[','-','A',']','+','A')],60,7)
#l = Lsystem(['F','-','-','F','-','-','F'],[('F','F','+','F','-','-','F','+','F')],60,3)#koch
#l = Lsystem(['A'],[('A','+','B','-','A','-','B','+'),('B','-','A','+','B','+','A','-')],60,5)#sier
#l = Lsystem(['X'],[('X','F','-','[','[','X',']','+','X',']','+','F','[','+','F','X',']','-','X'),('F','F','F')],25,5)
#l = Lsystem(['F'],[('F','F','[','+','F',']','F','[','-','F',']','[','F',']')],20,5)
l = Lsystem(['F'],[('F','F','F','-','[','-','F','+','F','+','F',']','+','[','+','F','-','F','-','F',']')],22.5,4)
#l = Lsystem(['F'],[('F','F','[','+','F',']','F','[','-','F',']','F')],25.7,4)
l.grow_it()
l.draw_it()
l.display()
#l.save('./cviko6/LPlant3')
#chaos_game(6)



