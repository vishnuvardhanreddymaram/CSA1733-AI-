from collections import deque

def is_valid(m, c):
    return (0 <= m <= 3 and 0 <= c <= 3 and 
            (m == 0 or m >= c) and 
            (3 - m == 0 or 3 - m >= 3 - c))

def bfs():
    start = (3, 3, 1)
    goal = (0, 0, 0)
    moves = [(1,0), (2,0), (0,1), (0,2), (1,1)]
    queue = deque([(start, [start])])
    visited = set()

    while queue:
        (m, c, b), path = queue.popleft()
        if (m, c, b) in visited: continue
        visited.add((m, c, b))

        if (m, c, b) == goal:
            return path

        for dm, dc in moves:
            if b:
                new = (m - dm, c - dc, 0)
            else:
                new = (m + dm, c + dc, 1)

            if is_valid(*new[:2]):
                queue.append((new, path + [new]))

    return None

# Run
solution = bfs()
for i, (m, c, b) in enumerate(solution):
    print(f"Step {i}: M={m}, C={c}, Boat on {'left' if b else 'right'}")