import numpy as np
import matplotlib.pyplot as plt

def _reduce(fun, _list):
	tail = _list[0]
	for next in _list[1:]:
		tail = fun(tail, next)
	return tail



x, y = np.ogrid[-2:1:500j, -1.5:1.5:500j]
_iter = 100
c = x + y*1j


z = reduce(lambda x, y: x**2 + c, [1] * _iter, c)

plt.figure(figsize=(10, 10))
plt.imshow(np.abs(z))
plt.show()

	

