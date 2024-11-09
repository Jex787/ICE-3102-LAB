def take_input():
    n = int(input("Enter the number of nodes: "))
    print("Enter the cost matrix:")
    cost_matrix = [list(map(int, input().split())) for _ in range(n)]
    return n, cost_matrix

def find_min_cost_path(city, n, cost_matrix, visited):
    print(f"{city + 1} ---> ", end="")
    visited[city] = True
    min_distance, next_city = float('inf'), -1

    # Find the nearest unvisited city
    for i in range(n):
        if cost_matrix[city][i] and not visited[i] and cost_matrix[city][i] < min_distance:
            min_distance, next_city = cost_matrix[city][i], i

    if next_city == -1:
        print("1")
        return cost_matrix[city][0]  # Return to starting city

    return min_distance + find_min_cost_path(next_city, n, cost_matrix, visited)

# Main program
n, cost_matrix = take_input()
print("\nThe Path is:")
total_cost = find_min_cost_path(0, n, cost_matrix, [False] * n)
print(f"\n\nMinimum cost is {total_cost}")

