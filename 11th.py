neighbors = {
    'WA': ['NT', 'SA'],
    'NT': ['WA', 'SA', 'Q'],
    'SA': ['WA', 'NT', 'Q', 'NSW', 'V'],
    'Q': ['NT', 'SA', 'NSW'],
    'NSW': ['SA', 'Q', 'V'],
    'V': ['SA', 'NSW'],
    'T': []  # Tasmania is isolated
}

# Colors available
colors = ['Red', 'Green', 'Blue']

# To store the assignment of colors
assignment = {}

def is_valid(state, color):
    """Check if assigning color to state is valid"""
    for neighbor in neighbors[state]:
        if neighbor in assignment and assignment[neighbor] == color:
            return False
    return True

def backtrack():
    """Recursive backtracking function"""
    if len(assignment) == len(neighbors):
        return True  # All regions assigned

    unassigned = [state for state in neighbors if state not in assignment]
    current = unassigned[0]

    for color in colors:
        if is_valid(current, color):
            assignment[current] = color
            if backtrack():
                return True
            del assignment[current]

    return False  # No valid color found

# Run the algorithm
if backtrack():
    print("Color Assignment:")
    for state in assignment:
        print(f"{state} → {assignment[state]}")
else:
    print("No valid coloring found.")