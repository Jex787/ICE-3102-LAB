#include<stdio.h>

int ary[10][10], visited[10], n, cost = 0;

int findNextCity(int city) {
    int i, minCost = 9999, nextCity = -1;
    
    for(i = 0; i < n; i++) {
        if(ary[city][i] != 0 && !visited[i] && ary[city][i] < minCost) {
            minCost = ary[city][i];
            nextCity = i;
        }
    }
    
    if(nextCity != -1) {
        visited[nextCity] = 1;
        cost += minCost;
    }
    
    return nextCity;
}

void tsp(int startCity) {
    int city = startCity;
    visited[city] = 1;
    printf("%d-->", city + 1);  // 1-based indexing
    
    while(1) {
        city = findNextCity(city);
        if(city == -1) break;  // No more cities to visit
        printf("%d-->", city + 1);  // 1-based indexing
    }
    
    printf("%d\n", startCity + 1);  // Return to start city
    cost += ary[city][startCity];  // Add the return cost
}

int main() {
    int i, j, startCity;
    
    printf("Enter the number of nodes (cities): ");
    scanf("%d", &n);
    
    printf("Enter the Cost Matrix (0 for no direct path):\n");
    for(i = 0; i < n; i++) {
        for(j = 0; j < n; j++) {
            scanf("%d", &ary[i][j]);
        }
    }
    
    printf("Enter the starting city (1 to %d): ", n);
    scanf("%d", &startCity);
    startCity--;  // Convert to 0-based index
    
    tsp(startCity);
    printf("Minimum cost is: %d\n", cost);
    
    return 0;
}
