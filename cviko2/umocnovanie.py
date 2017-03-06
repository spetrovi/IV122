#umocnovanie na zlomok
#a^n mod k
#vypocet pi
#odmocniny-polenie intervalu sqrt(5)==> 2,2^2; 2.3^2...

def my_modulo (a, b):
	return a-(a/b)

#euklidov algoritmus
def my_gcd(a, b):
	while b:
		a = b
		b = my_modulo(a, b)
	return a

def fr(n):
	pw = int(''.join(str(n).split('.')))
	sq = int(str(n).split('.')[1])
	sq = power(10,len(str(sq)))
	g = my_gcd(pw,sq)
	return pw/g, sq/g


def power(x, power):
	res = 1
	for i in range(0, power):
		res = res*x
	return res

def better_power(x,pow):
	if pow % 1 == 0:
		return power(x,pow)
	else:
		pw, sq = fr(pow)
		return sqrt_I(power(x,pw), sq, 0.1)
		

def sqrt_II(x, root, accuracy):
	newx = float(x)/2
	for i in range(0,20):
		new_power = power(newx, root)
		if new_power < x+accuracy and new_power > x-accuracy:
			break
		newx -= 0.1
	return newx

def sqrt_I(x, root, accuracy):
	a = 0
	b = x
	while True:
		result = float(a+b)/2
		new_power = power(result, root)	
		if new_power < x+accuracy and new_power > x-accuracy:
			return result
		if new_power > x:
			b = result
		else:
			a = result

print better_power(4,2.2)

