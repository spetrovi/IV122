import matplotlib.pyplot as plt

f = open('linreg.txt','r')
data = map(lambda x: (float(x.split(' ')[0]), float(x.split(' ')[1])),f.read().split('\n')[:-1])
f.close()

x = map(lambda x: x[0], data)
y = map(lambda y: y[1],data)

lowPx = min(x)
highPx = max(x)

lowPy = min(y)
highPy = max(y)

print str(highPx-lowPx)+'x + '+str(highPy-lowPy)


fig, ax = plt.subplots()
ax.scatter(x,y)

ax.plot([lowPx,highPx],[lowPy,highPy], color='red')
plt.show()


