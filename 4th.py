import itertools

def solve_cryptarithmetic():
    # Unique characters in the equation
    letters = 'SENDMORY'
    digits = range(10)

    # Generate all permutations of digits for 8 letters
    for perm in itertools.permutations(digits, len(letters)):
        mapping = dict(zip(letters, perm))

        # Skip if 'S' or 'M' is 0 because numbers can't start with 0
        if mapping['S'] == 0 or mapping['M'] == 0:
            continue

        # Build the actual numbers from letters
        send = 1000*mapping['S'] + 100*mapping['E'] + 10*mapping['N'] + mapping['D']
        more = 1000*mapping['M'] + 100*mapping['O'] + 10*mapping['R'] + mapping['E']
        money = 10000*mapping['M'] + 1000*mapping['O'] + 100*mapping['N'] + 10*mapping['E'] + mapping['Y']

        if send + more == money:
            print(f"SEND: {send}")
            print(f"MORE: {more}")
            print(f"MONEY: {money}")
            print("Mapping:", mapping)
            return

    print("No solution found.")

# Run the solver
solve_cryptarithmetic()