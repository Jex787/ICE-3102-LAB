#include<stdio.h>

void DFS(int);
int G[10][10], visited[10], n;

int main() {
    int i, j, start_vertex;
    
    // Take input for number of vertices
    printf("Enter number of vertices: ");
    scanf("%d", &n);
    
    printf("\nEnter adjacency matrix of the graph:\n");
    // Input adjacency matrix
    for(i = 0; i < n; i++)
        for(j = 0; j < n; j++)
            scanf("%d", &G[i][j]);
    
    // Initialize the visited array to 0 (unvisited)
    for(i = 0; i < n; i++)
        visited[i] = 0;

    // Ask the user for the starting vertex
    printf("\nEnter the starting vertex: ");
    scanf("%d", &start_vertex);
    
    // Print title before DFS traversal output
    printf("\nThe DFS traversal is:\n");
    
    // Start DFS from the user-selected starting vertex
    DFS(start_vertex);
    return 0;
}

void DFS(int i) {
    int j;
    printf("%d\n", i);  // Print the visited vertex
    visited[i] = 1;  // Mark the current vertex as visited
    
    // Recursively visit all adjacent vertices
    for(j = 0; j < n; j++) {
        // If vertex j is unvisited and connected to vertex i
        if(!visited[j] && G[i][j] == 1) {
            DFS(j);  // Call DFS recursively on vertex j
        }
    }
}
