# Graph

most betest data structure, conceived by Euler

all data structures we saw up this far are kind o graphs


## Terminology

- cycle: when you start at Node(x), follow the link, and end back at Node(x)
- acyclic: a graph that contains no cycles
- connected: when every node has a path to another node
- directed: when there is a direction to the connections. Think Twitter
- undirected: !direct. Think Facebook
- weighted: the edges have a weight associated with them. Think Maps
- dag: directed, acycled graph

- node: a point or vertex on the graph
- edge: the connection betxit two nodes


## Big O

O(V * E) where V is vertex, and E is edge


## Representation

- adj list - O()
- adj matrix - O(V²)

Adjacent List
- the idx maps to the node
- elements is another list, which is a list of edges containing where it points to and the weight


Adjacent Matrix

- more memory heavy
- node connection are mapped into a 2-matrix where the nodes are row-column, and the value is the weight


## Search

all tree are graph, so we can do DFS and BFS

[BFS Matrix](./kata-machine/src/day1/BFSGraphMatrix.ts)
[DFS List](./kata-machine/src/day1/DFSGraphList.ts) O(V+E)


## Dijkstra Shortest Path

We will use BFS with a previous array
Shortest path is the path from source to sync with min(sum(weights))

restrictions:
- non-negative weights to the edges

[Dijikstra](./kata-machine/src/day1/DijkstraList.ts) => Run Time: O(V² + E), counting loops won't work here

To improve the running time, use a minHeap -> O(logV(V+E))
