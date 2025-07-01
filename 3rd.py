from collections import deque

def is_goal(state, goal):
    return goal in state

def get_next_states(state, capacities):
    (a, b) = state
    (cap_a, cap_b) = capacities
    next_states = set()

    # Fill Jug A
    next_states.add((cap_a, b))

    # Fill Jug B
    next_states.add((a, cap_b))

    # Empty Jug A
    next_states.add((0, b))

    # Empty Jug B
    next_states.add((a, 0))

    # Pour A → B
    pour = min(a, cap_b - b)
    next_states.add((a - pour, b + pour))

    # Pour B → A
    pour = min(b, cap_a - a)
    next_states.add((a + pour, b - pour))

    return next_states

def bfs_water_jug(cap_a, cap_b, goal):
    visited = set()
    queue = deque()
    start = (0, 0)
    queue.append((start, [start]))

    while queue:
        current_state, path = queue.popleft()

        if current_state in visited:
            continue
        visited.add(current_state)

        if is_goal(current_state, goal):
            return path

        for next_state in get_next_states(current_state, (cap_a, cap_b)):
            if next_state not in visited:
                queue.append((next_state, path + [next_state]))

    return None

# Define the jugs and goal
jug1 = 4  # capacity of jug 1
jug2 = 3  # capacity of jug 2
goal = 2  # target amount

solution = bfs_water_jug(jug1, jug2, goal)

# Print the solution steps
if solution:
    print("Steps to reach the goal:")
    for step in solution:
        print(f"Jug1: {step[0]}L, Jug2: {step[1]}L")
else:
    print("No solution found.")