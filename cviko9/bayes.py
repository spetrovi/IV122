import random
import numpy as np

#hypotezy, P=poctiva, N=nepocntiva
#V=padlo K sestiek
#Vyber poctivej(1-(1/x)) 
#Vyber nepoctive(1/x)
#Pravdepodovnost k sestiek, 1/6^k (1/6*1/6...*1/6, k krat)
#Pravdepodobnost, ze je kocka poctiva
def bayes_calc(n,k):
	PN = 1.0/n
	PP = 1.0-PN
	PVP = 1.0/6**k
	PVN = 1.0
	return (PVP*PP)/(PVP*PP+PVN*PN)
	
def bayes(n,k):
	box = [True for x in range(1,n)]+[False]
	random.shuffle(box)
	dice = random.choice(box)	
	if dice:
		stat = [random.randint(1,6) for x in range(k)]
	if not dice:
		stat = [6 for x in range(k)]
	if stat == [6 for x in range(k)]:
		return True, dice
	else: return False, dice


n = 1000
k = 5

nice = 0
rigged = 0
for x in range(10000):
	success, dice = bayes(n,k)
	if success and dice:
		nice += 1
	if success and not dice:
		rigged += 1

print float(nice)/rigged
print bayes_calc(n,k)
