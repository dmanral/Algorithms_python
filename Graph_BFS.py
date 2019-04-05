#BFS is a graph traversal algorithmself.
#O(V+E) where V = # of vertecies and E = # of edges
#Each vertex has 3 attributes:
            #Discovery status: Color
                #Gray:  Undiscovered
                #Black: Discovered
                #Blue:  Visited
            #Distance from source: d
            #Predecessor vertex: pi

class Vertex:
    def __init__(self, n):
        self.name = n
        self.neighbors = list()

        self.distance = 9999 #just a high number
        self.color = 'black' #unvisited

    def add_neigbor(self, v): #v=letter name of vertex
        if v not in self.neighbors:
            self.neighbors.append(v)
            self.neighbors.sort()

class Graph:
    vertices = {}

    def add_vertex(self, vertex):
        if isinstance(vertex, Vertex) and vertex.name not in self.vertices:
            self.vertices[vertex.name] = vertex
            return True
        else:
            return False

    def add_edge(self, u, v): #u and v are vertices
        if u in self.vertices and v in self.vertices:
            for key, value in self.vertices.items():
                if key == u:
                    value.add_neigbor(v)
                if key == v:
                    value.add_neigbor(u)
            return True
        else:
            return False

    def print_graph(self):
        for key in sorted(list(self.vertices.keys())):
            print(key + str(self.vertices[key].neighbors) + " " + str(self.vertices[key].distance))

    def bfs(self, vert):
        q = list()              #Queue
        vert.distance = 0       #Starting vertex distance is always 0.
        vert.color = 'red'      #Starting vertex color is red because we are starting there, hence, its visited.

        for v in vert.neighbors:    #Visit neighbors
            self.vertices[v].distance = vert.distance + 1   #Set distance to 1.
            q.append(v)     #Add neighbors to queue.

        while len(q) > 0:
            u = q.pop(0)
            node_u = self.vertices[u] #u is just a name, therefore, we need vertex object
            node_u.color = 'red'

            for v in node_u.neighbors:
                node_v = self.vertices[v]
                if node_v.color == 'black': #if neighbor has not been visited, hence, black.
                    q.append(v)
                    if node_v.distance > node_u.distance + 1:
                        node_v.distance = node_u.distance + 1

def main():
    g = Graph()
    a = Vertex('A')

    g.add_vertex(a)
    g.add_vertex(Vertex('B'))
    for i in range(ord('A'), ord('K')):
        g.add_vertex(Vertex(chr(i)))

    edges = ['AB', 'AE', 'BF', 'CG', 'DE', 'DH', 'EH', 'FG', 'FI', 'FJ', 'GJ', 'HI']
    for edge in edges:
        g.add_edge(edge[:1], edge[1:])

    g.bfs(a)
    g.print_graph()

main()
