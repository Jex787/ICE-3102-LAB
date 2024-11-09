# Python recursive function to solve Tower of Hanoi puzzle
def tower_of_hanoi(n, from_rod, to_rod, aux_rod):
    # Base case: if only 1 disk, move it directly
    if n == 1:
        print(f"Move disk 1 from rod {from_rod} to rod {to_rod}")
        return

    # Move n-1 disks from from_rod to aux_rod
    tower_of_hanoi(n - 1, from_rod, aux_rod, to_rod)
    # Move nth disk from from_rod to to_rod
    print(f"Move disk {n} from rod {from_rod} to rod {to_rod}")
    # Move n-1 disks from aux_rod to to_rod
    tower_of_hanoi(n - 1, aux_rod, to_rod, from_rod)

# Take number of disks as input from the user
try:
    n = int(input("Enter the number of disks: "))
    if n <= 0:
        print("Number of disks must be a positive integer.")
    else:
        # Calling the function with rods labeled 'A', 'C', and 'B'
        tower_of_hanoi(n, 'A', 'C', 'B')
except ValueError:
    print("Please enter a valid integer.")
