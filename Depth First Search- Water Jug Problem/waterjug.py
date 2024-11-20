GOAL = (2, 0)
CAPACITY_4 = 4
CAPACITY_3 = 3

def water_jug_dfs(state, visited=None):
    if visited is None:
        visited = set()
    if state == GOAL:
        print("Solution found:", state)
        return True
    if state in visited:
        return False
    visited.add(state)
    x, y = state
    next_states = [
        (CAPACITY_4, y),
        (x, CAPACITY_3),
        (0, y),
        (x, 0),
        (min(x + y, CAPACITY_4), max(0, y - (CAPACITY_4 - x))),
        (max(0, x - (CAPACITY_3 - y)), min(x + y, CAPACITY_3)),
    ]
    for next_state in next_states:
        if next_state not in visited:
            if water_jug_dfs(next_state, visited):
                print("Step:", next_state)
                return True
    return False

initial_state = (0, 0)
print("Solving Water Jug Problem using DFS:")
water_jug_dfs(initial_state)
