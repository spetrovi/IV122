from random import choice
from priodict import priorityDictionary



def Dijkstra(G,start,end=None):
	"""
	Find shortest paths from the start vertex to all
	vertices nearer than or equal to the end.

	The input graph G is assumed to have the following
	representation: A vertex can be any object that can
	be used as an index into a dictionary.  G is a
	dictionary, indexed by vertices.  For any vertex v,
	G[v] is itself a dictionary, indexed by the neighbors
	of v.  For any edge v->w, G[v][w] is the length of
	the edge.  This is related to the representation in
	<http://www.python.org/doc/essays/graphs.html>
	where Guido van Rossum suggests representing graphs
	as dictionaries mapping vertices to lists of neighbors,
	however dictionaries of edges have many advantages
	over lists: they can store extra information (here,
	the lengths), they support fast existence tests,
	and they allow easy modification of the graph by edge
	insertion and removal.  Such modifications are not
	needed here but are important in other graph algorithms.
	Since dictionaries obey iterator protocol, a graph
	represented as described here could be handed without
	modification to an algorithm using Guido's representation.

	Of course, G and G[v] need not be Python dict objects;
	they can be any other object that obeys dict protocol,
	for instance a wrapper in which vertices are URLs
	and a call to G[v] loads the web page and finds its links.
	
	The output is a pair (D,P) where D[v] is the distance
	from start to v and P[v] is the predecessor of v along
	the shortest path from s to v.
	
	Dijkstra's algorithm is only guaranteed to work correctly
	when all edge lengths are positive. This code does not
	verify this property for all edges (only the edges seen
 	before the end vertex is reached), but will correctly
	compute shortest paths even for some graphs with negative
	edges, and will raise an exception if it discovers that
	a negative edge has caused it to make a mistake.
	"""

	D = {}	# dictionary of final distances
	P = {}	# dictionary of predecessors
	Q = priorityDictionary()   # est.dist. of non-final vert.
	Q[start] = 0
	
	for v in Q:
		D[v] = Q[v]
		if v == end: break
		#print G
		for w in G[v]:
			vwLength = D[v] + G[v][w]
			if w in D:
				if vwLength < D[w]:
					raise ValueError, \
  "Dijkstra: found better path to already-final vertex"
			elif w not in Q or vwLength < Q[w]:
				Q[w] = vwLength
				P[w] = v
	
	return (D,P)
			
def shortestPath(G,start,end):
	"""
	Find a single shortest path from the given start vertex
	to the given end vertex.
	The input has the same conventions as Dijkstra().
	The output is a list of the vertices in order along
	the shortest path.
	"""
	D,P = Dijkstra(G,start,end)
	Path = []
	"""	
	while 1:
		Path.append(end)
		if end == start: break
		end = P[end]
	Path.reverse()
	return Path
	"""
	while 1:
		Path.append(end)
		if end == start: break
		end = P[end]
	Path.reverse()
	return Path

def shortestPath2(G,start,end):
	"""
	Find a single shortest path from the given start vertex
	to the given end vertex.
	The input has the same conventions as Dijkstra().
	The output is a list of the vertices in order along
	the shortest path.
	"""
	D,P = Dijkstra(G,start,end)
	Path = []
	"""	
	while 1:
		Path.append(end)
		if end == start: break
		end = P[end]
	Path.reverse()
	return Path
	"""
	while 1:
		Path.append(end)
		if end == start: break
		end = P[end]
	Path.reverse()
	while (Path[len(Path)-1][0],Path[len(Path)-1][1]) == (Path[len(Path)-2][0],Path[len(Path)-2][1]):
	  Path = Path[:-1]
	return Path





class numMaze:
   def __init__(self,matrix):
      self.size = len(matrix)
      self.x = 0
      self.y = 0
      self.matrix = matrix
      self.graph = self.make_graph()
      
   def go_to(self, position):
	self.x = position[0]
	self.y = position[1]

   def possible_moves(self,x,y):
	number = self.matrix[x][y]
	positions = [(x+number,y),(x-number,y),(x,y+number),(x,y-number)]	
	positions = filter(lambda x: x[0]>-1 and x[0]<self.size and x[1]>-1 and x[1]<self.size, positions)
	return positions

   def bogo_solve(self):
	while self.x!=self.size-1 or self.y!=self.size-1:
		try:
			self.go_to(choice(self.possible_moves(self.x,self.y)))
		except IndexError:
			print 'stuck'
			return
		print self.x, self.y

   def make_graph(self):
	graph = {}
	for i in range(0,self.size):
		for j in range(0,self.size):
			node = (i,j)
			moves = self.possible_moves(i,j)
			newDict = {}
			for move in moves:
				newDict.update({move:1})
			graph[node] = newDict
	return graph

   def solve(self):	
	return shortestPath(self.graph,(0,0),(self.size-1,self.size-1))
	
   def is_unique(self):	
	P = self.solve()
	length = len(P)
	print P
	for i in range(0,length-1):
		del self.graph[P[i]][P[i+1]]
	try:
		P = shortestPath(self.graph,(0,0),(self.size-1,self.size-1))
	except KeyError:
		print 'This solution is the only path'
		return 1
	if length == len(P):
		print 'This solution is not the only shortest path'
		return 0
	print 'This solution is the only shortest path'
	return 1


level6n = [[3,2,4,4,3,1],
	  [3,4,2,1,5,3],
 	  [1,1,4,5,2,2],
 	  [5,3,3,5,1,4],
 	  [2,4,5,4,2,2],
 	  [5,1,4,3,3,1]]
level0 = [[1,1,1],
	 [1,1,1],
	 [1,1,1]]
level6s = [[4,3,3,2,5,2],
	  [4,2,3,3,3,4],
 	  [4,4,5,5,5,4],
 	  [1,3,3,4,2,3],
 	  [2,2,4,2,3,4],
 	  [5,3,5,4,3,1]]
level7i = [[4,2,2,4,5,4,4],
	   [4,6,1,4,1,5,3],
 	   [2,3,3,4,2,5,3],
 	   [3,2,3,5,1,4,3],
 	   [6,4,1,5,5,1,6],
 	   [2,1,3,1,4,3,6],
	   [3,3,2,6,2,6,1]]
level6q = [[2,3,5,5,1,1],
	  [2,1,1,4,4,2],
 	  [5,3,2,2,4,4],
 	  [3,3,5,4,5,3],
 	  [2,4,3,1,3,1],
 	  [3,5,2,4,3,1]]

maze = numMaze(level0)
print maze.solve()
#maze.is_unique()



