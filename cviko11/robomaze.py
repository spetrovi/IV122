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






class robotMaze:
   def __init__(self,matrix):
      self.sizeY = len(matrix)
      self.sizeX = len(matrix[0])
      self.matrix = matrix
      self.graph = self.make_graph()
   def possible_moves(self,node):
     if node[2] == 'west':
      moves = [(node[0],node[1],'north'),(node[0],node[1],'south')]
      if  node[1]-1 > -1 and self.matrix[node[0]][node[1]-1] == '.':
	moves.append((node[0],node[1]-1,'west'))
	return moves
      else: return moves

     if node[2] == 'east':
	moves = [(node[0],node[1],'north'),(node[0],node[1],'south')]
	if node[1]+1 < self.sizeX and self.matrix[node[0]][node[1]+1] == '.':
	  moves.append((node[0],node[1]+1,'east'))
	  return moves
	else: return moves
    
     if node[2] == 'north':
	moves = [(node[0],node[1],'east'),(node[0],node[1],'west')]
	if node[0]-1 > -1 and self.matrix[node[0]-1][node[1]] == '.':
	  moves.append((node[0]-1,node[1],'north'))
	  return moves
	else: return moves
     
     if node[2] == 'south':
	moves = [(node[0],node[1],'east'),(node[0],node[1],'west')]
	if node[0]+1 < self.sizeY and self.matrix[node[0]+1][node[1]] == '.':
	  moves.append((node[0]+1,node[1],'south'))
	  return moves
	else: return moves

   def make_graph(self):
     graph = {}
     for i in range(0,self.sizeY):
       for j in range(0,self.sizeX):
	 if self.matrix[i][j] != '#':
	   
	  moves = self.possible_moves((i,j,'west'))
	  newDict = {}
	  for move in moves:
	      newDict.update({move:1})
	  graph[(i,j,'west')] = newDict
	  
	  moves = self.possible_moves((i,j,'east'))
	  newDict = {}
	  for move in moves:
	      newDict.update({move:1})
	  graph[(i,j,'east')] = newDict
	  
	  moves = self.possible_moves((i,j,'north'))
	  newDict = {}
	  for move in moves:
	      newDict.update({move:1})
	  graph[(i,j,'north')] = newDict
	  
	  moves = self.possible_moves((i,j,'south'))
	  newDict = {}
	  for move in moves:
	      newDict.update({move:1})
	  graph[(i,j,'south')] = newDict
     return graph  

   def solve(self,end):	
	return shortestPath2(self.graph,(0,0,'east'),end)



level1= [['.','.','.','.','.','.','.'],
	 ['.','.','#','#','#','#','.'],
	 ['#','.','.','#','#','#','.'],
	 ['#','#','.','.','#','#','.'],
	 ['#','#','#','.','.','#','.'],
	 ['#','#','#','#','.','.','.']]

level0= [['.','.'],
	 ['.','.'],
	 ['.','.']]




maze2 = robotMaze(level1)
print maze2.solve((5,5,'east'))


