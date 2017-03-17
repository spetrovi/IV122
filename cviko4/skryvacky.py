from PIL import Image, ImageDraw 
import math


def skryvacka1():
  im = Image.open('skryvacka1.png')
  im = im.convert('RGB')
  for i in range(0,499):
    for j in range(0,137):
      pixel = im.getpixel((i,j))
      if pixel[2] == 0:
	im.putpixel((i,j),(255,255,255))
  im.show()
  im.save('orel.png','png')

def skryvacka2():
    im = Image.open('skryvacka2.png')
    im = im.convert('RGB')
    prev_pixel = (0,0,0)

    threashold = 2
    for j in range(0,137):
        for i in range(0,489):
            pixel = im.getpixel((i,j))
            if abs(pixel[0]-prev_pixel[0]) > threashold or abs(pixel[1]-prev_pixel[1]) > threashold or abs(pixel[2]-prev_pixel[2]) > threashold:
                im.putpixel((i,j),(0,0,0))
            prev_pixel = pixel
    im.show()
    im.save('koza.png','png')


def skryvacka3():
    im = Image.open('skryvacka3.png')
    im = im.convert('RGB')
    width = 507
    height = 188
    matrix = Image.new('RGB',(width,height),(255,255,255))
    
    for x in range(0,width):
        if x % 2 == 0: color = (0,0,0)
        else: color = (255,255,255)
        for y in range(0,height):
                if color == (255,255,255): color = (0,0,0)
                else: color = (255,255,255)
	    	print x, y, color
	    	matrix.putpixel((x,y),color)

    matrix.save('m.png','png')
    new_im = Image.new('RGB',(width,height))
    for i in range(0,width):
        for j in range(0,height):
            pixel1 = im.getpixel((i,j))
            pixel2 = matrix.getpixel((i,j))
            if pixel1 == pixel2:
                new_im.putpixel((i,j),(0,0,0))
            else:
                new_im.putpixel((i,j),(255,255,255))
    new_im.save('slon.png','png')

skryvacka1()
skryvacka2()
skryvacka3()











