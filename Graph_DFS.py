# Could be directed or undirected
# Discovery and finish time
# Finish time is usually 2*number of vertices, for example, 10 vertices =  10*2 = 20 finish time
# Sorted by increasing discovery time
# Can also be sorted by decreasing finish time, for example, 20, 19, 18...etc

class Vertex:
    def __init__(self, n):          #constructor
        self.name = n
        self.neighbors = list()

        self.discovery = 0
        self.finish = 0
        self.color = 'black'        #Undiscovered/unvisited

    def add_neighbor(self, v):
        nset= set(self.neighbors)
        if v not in nset:
            self.neighbors.append(v)        #add to neighbors
            self.neighbors.sort()            #Tim sort

class Graph:
    vertices = {}               #dictionary
    time = 0

    def add_vertex(self,vertex):    #receivees a vertex
        if isinstance(vertex, Vertex) and vertex.name not in self.vertices: #make sure what we pass in is a vertex
            self.vertices[vertex.name] = vertex
            return True
        else:
            return False

    def add_edge(self, u, v):
        if u in self.vertices and v in self.vertices:
            for key, value in self.vertices.items():
                if key == u:                    #find u
                    value.add_neighbor(v)       #add v as a neighbor to it
                if key == v:                    #find v
                    value.add_neighbor(u)       #add u as a neighbor to it
            return True
        else:
            return False

    def print_graph(self):
        for key in sorted(list(self.vertices.keys())):
            print(key + str(self.vertices[key].neighbors) + "  " + str(self.vertices[key].discovery) + "/" + str(self.vertices[key].finish))

    def _dfs(self, vertex):
        global time
        vertex.color = 'red'            #already discovered
        vertex.discovery = time
        time += 1

        for v in vertex.neighbors:
            if self.vertices[v].color == 'black':   #black = hasnt been visited yet
                self._dfs(self.vertices[v])
        vertex.color = 'blue'                       #finished
        vertex.finish = time
        time += 1

    def dfs(self, vertex):
        global time
        time = 1
        self._dfs(vertex)

def main():
    g = Graph()

    #different way of adding vertices
    a = Vertex('A')
    g.add_vertex(a)
    g.add_vertex(Vertex('B'))

    #adding whole series of vertices
    for i in range(ord('A'), ord('K')):
        g.add_vertex(Vertex(chr(i)))

    edges = ['AB', 'AE', 'BF', 'CG', 'DE', 'DH', 'EH', 'FG', 'FI', 'FJ', 'GJ', 'HI']
    for edge in edges:
        g.add_edge(edge[:1], edge[1:])

    g.dfs(a)
    g.print_graph()


main()
