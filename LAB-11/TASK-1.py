'''Implemented a graph using adjacency list representation.
   The implementation is quite different from the one in the pdf.
    But logically its working fine.
   I tried to take care of the case when the vertexes values are not same as their indexes.
   JazakAllah !
'''
class GraphNode:
    def __init__(self, vertex=0, next_node=None):
        self.vertex = vertex
        self.next = next_node
        self.index = None

    def __str__(self):
        s = (f'{self.vertex}: ')
        if not self.next: return s
        s += ','.join([f' {each.vertex}' for each in reversed(self.next)])
        return s


class Graph:
    MAX = 10
    def __init__(self):
        self.headnodes = [None] * self.MAX
        self.n = 0
        self.visited = ([False] * self.MAX)

    def initialize_visited(self):
        self.visited = [False] * self.MAX

    def addVertex(self, vertex):
        ver = GraphNode(vertex)
        if self.n <= self.MAX:
            for i in range(self.MAX):
                if self.headnodes[i] is None:
                    self.headnodes[i] = ver
                    ver.index = i
                    break
            self.n += 1
        else:
            print("Graph is full")


    def removeVertex(self, vertex):
        if not self.vertexExists(vertex):
            print("Vertex not found")
            return
        for i in range(self.MAX):
            if self.headnodes[i] is not None:
                if self.headnodes[i].vertex == vertex:
                    self.headnodes[i] = None
                    self.n -= 1
                    break
        return

    def addEdge(self, vertex1, vertex2):
        if not self.vertexExists(vertex1) or not self.vertexExists(vertex2):
            print("Vertex not found")
            return
        idx1 = self.headnodes[vertex1].index
        idx2 = self.headnodes[vertex2].index
        if not self.headnodes[idx1].next: self.headnodes[idx1].next = [];
        self.headnodes[idx1].next.append(self.headnodes[idx2])
        return



    def removeEdge(self, vertex1, vertex2):
        if not self.vertexExists(vertex1) or not self.vertexExists(vertex2):
            print("Vertex not found")
            return
        idx1 = self.headnodes[vertex1].index
        idx2 = self.headnodes[vertex2].index
        if self.headnodes[idx1].next is None: return;
        self.headnodes[idx1].next.remove(self.headnodes[idx2])
        return

    def vertexExists(self, vertex):
        for node in self.headnodes:
            if node is not None and node.vertex == vertex:
                return True
        return False

    def printGraph(self):
        for each in self.headnodes:
            if each:
                print(each)
        print()

    def _dfs(self, node):
        if not node: return
        print(node.vertex, end=" ")
        self.visited[node.index] = True
        if node.next is not None:
            for each in reversed(node.next):
                if not self.visited[each.index]:
                    self._dfs(each)
    def dfs(self, vertex):
        if not self.vertexExists(vertex):
            print("Vertex not found")
            return
        node = None
        for i in range(self.MAX):
            if self.headnodes[i] is not None and self.headnodes[i].vertex == vertex:
                node = self.headnodes[i]
                break
        self._dfs(node)
        print()


    def bfs(self, vertex):
        if not self.vertexExists(vertex):
            print("Vertex not found")
            return
        node = None
        for i in range(self.MAX):
            if self.headnodes[i] is not None and self.headnodes[i].vertex == vertex:
                node = self.headnodes[i]
                break
        queue = []
        queue.append(node)
        while queue:
            cur = queue.pop(0)
            print(cur.vertex, end=" ")
            if cur.next is not None:
                for each in reversed(cur.next):
                    if not self.visited[each.index]:
                        queue.append(each)
                        self.visited[each.index] = True
                self.visited[cur.index] = True


if __name__ == '__main__':
    g = Graph()
    # Add vertices
    for i in range(6):
        g.addVertex(i)
    # Add edges
    g.addEdge(0, 1)
    g.addEdge(0, 3)
    g.addEdge(1, 2)
    g.addEdge(1, 3)
    g.addEdge(1, 5)
    g.addEdge(3, 4)
    g.addEdge(4, 2)
    g.addEdge(4, 5)
    g.addEdge(5, 1)
    # Print the graph
    g.printGraph()
    # Perform DFS and BFS traversals
    print("DFS starting from vertex 0:")
    g.dfs(0)
    g.initialize_visited()
    print("BFS starting from vertex 0:")
    g.bfs(0)