def undirected(vertixes, edges_list):
    adjacency_list = {i:[] for i in range(vertixes)}
    for each in edges_list:
        adjacency_list[each[0]].append(each[1])
        adjacency_list[each[1]].append(each[0])

    return adjacency_list

def directed(vertixes, edges_list):
    adjacency_list = {i:[] for i in range(vertixes)}
    for each in edges_list:
        adjacency_list[each[0]].append(each[1])
    return adjacency_list

def display(dictionary):
    for i, j in dictionary.items():
        print(i,end =' -> ')
        print(' '.join(map(str,j))) if j != [] else print('x')


if __name__ == '__main__':
    vertixes = 9
    edges = 8
    edges_list1 = [(2, 0),(0, 3),(5, 2),(4, 6),(4, 0),(1, 3),(2, 1),(6, 1)]
    adjacency_list = undirected(vertixes, edges_list1)
    vertices2 = 8
    edges2 = 11
    edge_list2 = [(0, 3),(5, 7), (7, 5),(4, 6), (4, 2), (2, 5),(1, 5),(1, 6), (5, 6), (6, 5), (4, 7)]
    adjacency_list2 = directed(vertices2, edge_list2)
    print('UNDIRECTED GRAPH ADJACENCY LIST:')
    display(adjacency_list)
    print('-'*30)
    print('DIRECTED GRAPH ADJACENCY LIST:')
    display(adjacency_list2)

    # For testing 
    type = input('Enter D for directed graph and U for undirected graph: ')
    v = int(input('Enter number of vertexes:'))
    e = int(input('Enter number of edges:'))
    print('Start entering vertixes which have edges between them.\n P.S~(Enter the one directed toward other first in directed graph case')
    lst = []
    for i in [0]*e:
        lst.append(list(map(int,input().split())))
    if type.lower() == 'd':
        adj_list = directed(v,lst)
    else:
        adj_list = undirected(v, lst)
    display(adj_list)






