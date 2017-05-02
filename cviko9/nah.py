from random import choice 
import numpy as np

f = open('random2.txt','r')
s2 = f.read().split(' ')[:-1]
f.close()
print s2
print np.histogram(map(lambda x: int(x),s2), bins=6)
#2 malo dvojek vela petiek


