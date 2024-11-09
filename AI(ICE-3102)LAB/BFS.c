#include<stdio.h>

int a[20][20], visited[20], n;

void bfs(int v) {
    int queue[20], front = 0, rear = 0;
    visited[v] = 1;  // Mark the starting vertex as visited
    queue[rear++] = v;  // Enqueue the starting vertex
    
    while(front < rear) {  // While the queue is not empty
        int node = queue[front++];  // Dequeue a vertex from the front of the queue
        printf("%d\t", node);  // Print the current node
        
        // Check all adjacent vertices
        for(int i = 1; i <= n; i++) {
            if(a[node][i] == 1 && !visited[i]) {  // If there's an edge and the node is unvisited
                visited[i] = 1;  // Mark the node as visited
                queue[rear++] = i;  // Enqueue the node
            }
        }
    }
}

int main() {
    int v;
    
    // Input number of vertices
    printf("\nEnter the number of vertices: ");
    scanf("%d", &n);
    
    // Input adjacency matrix
    printf("\nEnter graph data in matrix form:\n");
    for(int i = 1; i <= n; i++) {
        for(int j = 1; j <= n; j++) {
            scanf("%d", &a[i][j]);
        }
    }

    // Input starting vertex
    printf("\nEnter the starting vertex: ");
    scanf("%d", &v);
    
    // Call BFS to print reachable nodes
    printf("\nThe nodes which are reachable are:\n");
    bfs(v);
    
    return 0;
}
