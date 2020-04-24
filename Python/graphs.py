import numpy as np 



# random_int = np.random.randint(10, 100)
# random_dgraph = Graph.Erdos_Renyi(n = random_int, m = random_int, directed=True, loops=False)
# random_udgraph = Graph.Erdos_Renyi(n = random_int, m = random_int, directed=False, loops=False)

adjaceny_matrix = [[0, 4, 1, 9], [3, 0, 6, 11], [4, 1, 0, 2], [6, 5, -4, 0]]
adjaceny_list = {
    '1' : ['2','6'],
    '2' : ['4', '5'],
    '3' : ['4'],
    '4' : [],
    '5' : ['6', '3', '5'],
    '6' : []
}
visited = []
queue = []
#DFS: O(V+E) time complexity
def dfs(visited, graph, node):
    if node not in visited:
        print (node),
        visited.append(node)
        for adjacent in graph[node]:
            dfs(visited, graph, adjacent)
dfs(visited, adjaceny_list, '1')

#BFS: O(V+E) time complexity
def bfs(visited, graph, node):
    visited.append(node)
    queue.append(node)

    while queue:
        x = queue.pop(0)
        print (x, end = " "),
        
        for adjacent in graph[x]:
            if adjacent not in visited:
                visited.append(adjacent)
                queue.append(adjacent)

bfs(visited, adjaceny_list, '1')

#Dijktras 

#Bellman-Ford 