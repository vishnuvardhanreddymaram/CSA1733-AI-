from collections import deque

def vacuum_cleaner():
    # Initial state: (vacuum_location, RoomA_status, RoomB_status)
    start = ('B', 'Dirty', 'Dirty')
    goal = ('B', 'Clean', 'Clean')
    
    queue = deque([(start, [])])
    visited = set()

    while queue:
        (loc, A, B), path = queue.popleft()
        state = (loc, A, B)

        if state in visited:
            continue
        visited.add(state)

        if (A, B) == ('Clean', 'Clean'):
            return path + [state]

        actions = []

        # Suck dirt
        if loc == 'A' and A == 'Dirty':
            actions.append(('Suck', ('A', 'Clean', B)))
        elif loc == 'B' and B == 'Dirty':
            actions.append(('Suck', ('B', A, 'Clean')))

        # Move
        if loc == 'A':
            actions.append(('Move Right', ('B', A, B)))
        else:
            actions.append(('Move Left', ('A', A, B)))

        for action, new_state in actions:
            queue.append((new_state, path + [state]))

# Run the simulation
solution = vacuum_cleaner()
for i, state in enumerate(solution):
    loc, A, B = state
    print(f"Step {i}: Vacuum at {loc}, Room A: {A}, Room B: {B}")