from PIL import Image, ImageDraw 

def change_color(color):
	if color == 255: return 0
	return 255

def belongs_to(point, line):
	xA = line[0][0]
	yA = line[0][1]
	xB = line[1][0]
	yB = line[1][1]
	xC = point[0]
	yC = point[1]
	if (xA < xC < xB and xA < xB) or (yA < yC <yB and yA < yB) or (xB < xC <xA and xB < xA) or (yB < yC <yA and yB < yA):
		return True
	return False

def find_cross_points(line1, line2):
	xA = line1[0][0]
	yA = line1[0][1]
	xB = line1[1][0]
	yB = line1[1][1]
	xC = line2[0][0]
	yC = line2[0][1]
	xD = line2[1][0]
	yD = line2[1][1]
	if ((xA-xB)*(yC-yD)-(yA-yB)*(xC-xD)) == 0 or ((xA-xB)*(yC-yD)-(yA-yB)*(xC-xD)) == 0: return (None)
	xP = ((xA*yB-yA*xB)*(xC-xD)-(xA-xB)*(xC*yD-yC*xD))/((xA-xB)*(yC-yD)-(yA-yB)*(xC-xD))
	yP = ((xA*yB-yA*xB)*(yC-yD)-(yA-yB)*(xC*yD-yC*xD))/((xA-xB)*(yC-yD)-(yA-yB)*(xC-xD))
	if belongs_to((xP,yP),line1) and belongs_to((xP,yP),line2): 
		return (xP,yP)

def polygon(size, points):
	im = Image.new('L',(size,size))
	lines = []
	for i in range(0,len(points)-1):
		lines.append((points[i], points[i+1]))
	lines.append((points[i+1],points[0]))
	for y in range(size):
		color = 255
		cross_points = []
		for line in lines:
			cross_points.append(find_cross_points(line, ((0,y),(size,y))))#kde riadok pretina polygon
		cross_points = filter(lambda x: x!=None, cross_points)
		if len(cross_points) % 2 == 1:#ak je neparny pocet cross points, algoritmus zrejme vynechal nejaky vrchol
			cross_points += points
		for x in range(size):
			if (x,y) in cross_points:
				color = change_color(color)
			im.putpixel((x,y),color)
	im.save('polygon2.png','png')
	

polygon(200,[(10, 10),(180, 20),(160, 150),(100, 50),(20, 180)])
polygon(200,[(10, 10),(180, 20),(160, 45),(190, 55),(160, 65),(160, 150),(130, 70),(100, 50),(20, 180)])
#polygon(200,[(50, 50),(50, 100),(100, 100),(100,50)])








