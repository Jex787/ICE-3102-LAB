#include <stdio.h>

// Recursive function to solve Tower of Hanoi problem
void towerOfHanoi(int n, char source, char helper, char destination) {
    if (n == 1) {
        printf("Move disk 1 from %c to %c\n", source, destination);
        return;
    }
    // Move n-1 disks from source to helper
    towerOfHanoi(n - 1, source, destination, helper);
    // Move nth disk from source to destination
    printf("Move disk %d from %c to %c\n", n, source, destination);
    // Move n-1 disks from helper to destination
    towerOfHanoi(n - 1, helper, source, destination);
}

int main() {
    int n;
    printf("Enter the number of disks: ");
    scanf("%d", &n);
    printf("Steps to solve Tower of Hanoi for %d disks:\n", n);
    towerOfHanoi(n, 'A', 'B', 'C'); // A, B, C are names of rods
    return 0;
}