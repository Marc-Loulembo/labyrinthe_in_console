

import random
from queue import PriorityQueue

# Initializing my maze
def create_maze(size=5, num_walls=5):
    if size < 4 or num_walls >= size * size:
        return None
    maze = [["." for _ in range(size)] for _ in range(size)]

    # I place my E input and my O output
    maze[0][0] = 'E'
    maze[0][size - 1] = 'O'

    # I use a for loop to randomly place my walls, and the dots represent the empty spaces.
    for _ in range(num_walls):
        x, y = random.randint(0, size - 1), random.randint(0, size - 1)
        while maze[y][x] != "." or (x == 0 and y == 0) or (x == size - 1 and y == size - 1):
            x, y = random.randint(0, size - 1), random.randint(0, size - 1)
        maze[y][x] = "W"

    # I return my maze function
    return maze

def fill_maze(maze):
    size = len(maze)
    max_value = size * size  # Maximum value for moves

    for n in range(1, max_value):  # Loop to give the number of required moves
        for i in range(size):
            for j in range(size):
                if maze[i][j] == 'E':
                    # Check and mark the cells around the starting point E
                    if j + 1 < size and maze[i][j + 1] != 'W':
                        maze[i][j + 1] = str(n)  # Convert to string
                    if i + 1 < size and maze[i + 1][j] != 'W':
                        maze[i + 1][j] = str(n)  # Convert to string

        for i in range(size):
            for j in range(size):
                if maze[i][j] == str(n):
                    # Check and mark the cells around n
                    if j + 1 < size and maze[i][j + 1] != 'W' and maze[i][j + 1] == '.':
                        maze[i][j + 1] = str(n + 1)  # Convert to string
                    if j - 1 >= 0 and maze[i][j - 1] != 'W' and maze[i][j - 1] == '.':
                        maze[i][j - 1] = str(n + 1)  
                    if i + 1 < size and maze[i + 1][j] != 'W' and maze[i + 1][j] == '.':
                        maze[i + 1][j] = str(n + 1)  
                    if i - 1 >= 0 and maze[i - 1][j] != 'W' and maze[i - 1][j] == '.':
                        maze[i - 1][j] = str(n + 1)  

# Function to display my maze
def display_labyrinthe(maze):
    for row in maze:
        print(" ".join(row))

# I create a function for my solved maze
def solve_maze(maze):
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    start = (0, 0)
    end = (0, len(maze[0]) - 1)  # Exit top right

    # I calculate a heuristic value for each cell based on its distance from the output.
    def heuristic(node):
        x, y = node
        return abs(x - end[0]) + abs(y - end[1])

    # I use a priority queue (PriorityQueue) to explore cells in order of priority.
    pq = PriorityQueue()
    pq.put((0, start))
    came_from = {}
    cost_so_far = {start: 0}
    path_found = False

    # I explore the labyrinth and find the shortest way from the entrance to the exit.
    while not pq.empty():
        _, current = pq.get()

        if current == end:
            path_found = True
            break

        for dx, dy in directions:
            new_x, new_y = current[0] + dx, current[1] + dy

            if 0 <= new_x < len(maze) and 0 <= new_y < len(maze[0]) and maze[new_x][new_y] != "W":
                new_cost = cost_so_far[current] + 1
                if (new_x, new_y) not in cost_so_far or new_cost < cost_so_far[(new_x, new_y)]:
                    cost_so_far[(new_x, new_y)] = new_cost
                    priority = new_cost + heuristic((new_x, new_y))
                    pq.put((priority, (new_x, new_y)))
                    came_from[(new_x, new_y)] = current

    if path_found:
        # Reconstruct and mark the path
        current = end
        while current != start:
            x, y = current
            maze[x][y] = "*"  # the "*" represents the distance covered
            current = came_from[current]

# Creating the maze
maze = create_maze(5, 5)

# I display the generated maze
print("generated maze :")
display_labyrinthe(maze)

# Filled maze
fill_maze(maze)
print("maze filled :")
display_labyrinthe(maze)

# labyrinth solved
solve_maze(maze)
# I display the solved maze
print("\nMaze solved :")
display_labyrinthe(maze)
