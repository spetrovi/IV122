from PIL import Image, ImageDraw 
import matplotlib.pyplot as plt
import numpy as np

def img1(size):
  s2 = size/2
  im = Image.new('RGB', (size, size), (255,255,255))
  draw = ImageDraw.Draw(im) 
  for i in range(0,(s2/10)+1):
    x = i*10
    draw.line((x,s2, s2,s2-x), fill=0)
    draw.line((x,s2, s2,s2+x), fill=0)
    draw.line((size-x,s2, s2,s2-x), fill=0)
    draw.line((size-x,s2, s2,s2+x), fill=0)
  #im.show()
  im.save('./cviko1/siet.png','png')

def colors():
  img = Image.new( 'RGB', (255,255), "black")
  pixels = img.load() 
  for i in range(img.size[0]):
    for j in range(img.size[1]):
      pixels[i,j] = (i, 0, j) #smerom doprava scervenieva, smerom dole zmodrieva
  #img.show()
  img.save('./cviko1/colors.png','png')

def collatz(n):
  number_of_steps = 0
  while n !=1:
    number_of_steps += 1
    if n % 2 == 0:
      n = n / 2
    else:
      n = 3*n+1
  return number_of_steps

def collatz_plot(n):
  name = n
  x = 0
  list_x = []
  list_y = []
  while n !=1:
    x += 1
    list_x.append(x)
    list_y.append(n)
    if n % 2 == 0:
      n = n / 2
    else:
      n = 3*n+1
  plt.plot(list_x, list_y)
  plt.savefig('./collatz/img_'+str(name)+'.png', bbox_inches='tight')
  if (name == 100) or (name == 150) or (name==200) or (name == 250) or (name == 300) or (name==350):
    plt.close()
  #plt.show()

def collatz_steps(n):
  list_x = []
  list_y = []
  for i in range (1,n):
    list_x.append(i)
    list_y.append(collatz(i))
  plt.plot(list_x, list_y,'ro')
  plt.savefig('./collatz/collatz_steps.png', bbox_inches='tight')
  #plt.show()

def is_prime(n):
    for i in range(2,int(n ** 0.5)+1):
        if n % i==0:
            return False

    return True
  
  
def color_pixel(count,k):
  if is_prime(count):
    return (0,0,0)
  else:
    return (255,255,255)
"""
  if count % k == 0:
    return(0,0,0)
  else:
    return(255,255,255)
"""
def ulam_spiral(k):
  size = 1000
  x = size/2 - 1#select
  y = size/2 - 1#       central pixel
  im = Image.new('RGB', (size, size), 'white')
  pixels = im.load()
  count = -1
  iteration = 0
  while iteration +1 < size:
    iteration += 1
    for i in range(1,iteration):
      if iteration % 2 == 1:
	x += 1
      else:
	x -= 1
      count += 1 
      pixels[x,y] = color_pixel(count,k)
    for i in range(1,iteration):
      if iteration % 2 == 1:
	y += 1
      else:
	y -= 1
      count += 1
      pixels[x,y] = color_pixel(count,k)
  im.save('./ulam/primes.png','png')
  #im.show()
  
  
def nsd(a,b):
  if b == 0:
    return a
  else:
    return nsd(b, a % b)
#netusim, co ste myslel vyrazom Napiste program generujuci obrazok vizualizujuci najvacsie spolocne delitele, tak som spravil toto
def nsd_range(seed):
  list_x = []
  list_y = []
  for i in range(1,seed):
    list_x.append(i)
    list_y.append(nsd(seed,i))
  plt.plot(list_x, list_y,'ro')
  plt.show()
  
  
#nsd_range(8000)
#img1(800)
colors()
#ulam_spiral(100)
#for i in range(2,400):
#  collatz_plot(i)
#collatz_steps(8000)
#for i in range(2,400):
    #ulam_spiral(i)
