# Function to perform Depth First Search
def dfs(graph, visited, node):
    # Print the node and mark it as visited
    print(node, end=" ")
    visited[node] = True
    
    # Visit all the neighbors of the current node
    for neighbor, isConnected in enumerate(graph[node]):
        if isConnected == 1 and not visited[neighbor]:  # Check if there's a connection and if it's unvisited
            dfs(graph, visited, neighbor)

# Main function to handle input and initiate DFS
def main():
    # Taking number of nodes as input
    total = int(input("Enter the number of nodes in the graph: "))
    
    # Taking adjacency matrix input
    print("Enter the adjacency matrix of the graph:")
    graph = []
    for i in range(total):
        row = list(map(int, input().split()))
        graph.append(row)
    
    # Taking the starting node as input
    start_node = int(input("Enter the starting node for DFS: "))
    
    # Initialize visited array to keep track of visited nodes
    visited = [False] * total
    
    # Output DFS traversal
    print(f"DFS traversal starting from node {start_node}: ", end="")
    dfs(graph, visited, start_node)
    print()  # for new line after traversal

# Execute main function
main()
