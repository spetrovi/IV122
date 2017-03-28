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

chaos_game(6)



