import heapq

# Define the goal state
goal_state = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 0]]

# Get the (x, y) position of a value in a state
def find_position(state, value):
    for i in range(3):
        for j in range(3):
            if state[i][j] == value:
                return i, j

# Manhattan distance heuristic
def manhattan(state):
    distance = 0
    for i in range(3):
        for j in range(3):
            val = state[i][j]
            if val != 0:
                goal_x, goal_y = find_position(goal_state, val)
                distance += abs(i - goal_x) + abs(j - goal_y)
    return distance

# Convert list of lists to a tuple (hashable)
def to_tuple(state):
    return tuple([tuple(row) for row in state])

# Get all possible moves from current state
def get_neighbors(state):
    neighbors = []
    x, y = find_position(state, 0)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # up, down, left, right

    for dx, dy in directions:
        new_x, new_y = x + dx, y + dy
        if 0 <= new_x < 3 and 0 <= new_y < 3:
            new_state = [row[:] for row in state]  # deep copy
            # Swap 0 with adjacent tile
            new_state[x][y], new_state[new_x][new_y] = new_state[new_x][new_y], new_state[x][y]
            neighbors.append(new_state)
    return neighbors

# A* Search
def solve(start_state):
    visited = set()
    pq = []
    heapq.heappush(pq, (manhattan(start_state), 0, start_state, []))

    while pq:
        est_total, cost_so_far, current_state, path = heapq.heappop(pq)
        state_tuple = to_tuple(current_state)

        if state_tuple in visited:
            continue
        visited.add(state_tuple)

        if current_state == goal_state:
            return path + [current_state]

        for neighbor in get_neighbors(current_state):
            if to_tuple(neighbor) not in visited:
                heapq.heappush(pq, (cost_so_far + 1 + manhattan(neighbor),
                                    cost_so_far + 1,
                                    neighbor,
                                    path + [current_state]))
    return None

# Utility function to print the puzzle
def print_path(path):
    for step, state in enumerate(path):
        print(f"Step {step}:")
        for row in state:
            print(row)
        print()

# Example usage
start_state = [[1, 2, 3],
               [5, 0, 6],
               [4, 7, 8]]

solution_path = solve(start_state)

if solution_path:
    print_path(solution_path)
    print(f"Total moves: {len(solution_path) - 1}")
else:
    print("No solution found.")