from collections import deque

def bfs(graph, start_vertex):
    visited = [False] * len(graph)  # List to track visited vertices
    queue = deque([start_vertex])   # Queue for BFS, starting with the start_vertex
    visited[start_vertex] = True    # Mark the starting vertex as visited
    reachable_nodes = []            # List to store reachable nodes in BFS order

    while queue:
        vertex = queue.popleft()  # Dequeue a vertex from the queue
        reachable_nodes.append(vertex + 1)  # Append the current vertex (1-based index)
        
        # Check adjacent vertices
        for i, connected in enumerate(graph[vertex]):
            if connected == 1 and not visited[i]:  # If there's an edge and it's unvisited
                queue.append(i)      # Enqueue the connected vertex
                visited[i] = True    # Mark it as visited

    return reachable_nodes

def main():
    # Taking the number of vertices
    n = int(input("Enter the number of vertices: "))
    
    # Taking adjacency matrix input
    print("Enter graph data in matrix form:")
    graph = []
    for _ in range(n):
        row = list(map(int, input().split()))
        graph.append(row)
    
    # Taking the starting vertex
    start_vertex = int(input("Enter the starting vertex: ")) - 1
    
    # Performing BFS and getting the reachable nodes
    reachable_nodes = bfs(graph, start_vertex)
    
    # Displaying the result
    print("The nodes which are reachable are:")
    print(" ".join(map(str, reachable_nodes)))

# Execute the main function
main()
