from random import choice 
import numpy as np

#print 'Sequence 2'
f = open('random2.txt','r')
s2 = f.read().split(' ')[:-1]
f.close()
s2 = map(lambda x: int(x), s2)
#print np.histogram(s2, bins=6)

print 'Sequence1'
f = open('random1.txt','r')
s1 = f.read().split(' ')[:-1]
s1 = map(lambda x: int(x), s1)
f.close()

stats = [[] for i in range(6)]


for i, num in enumerate(s1[:-1]):
	stats[num-1].append(s1[i+1])

for stat in stats:
	print np.histogram(stat, bins=[1,2,3,4,5,6,7])


#5 ma prilis vela sesiek
#6 ma prilis vela sesiek
#7 ma prilis vela sesiek

