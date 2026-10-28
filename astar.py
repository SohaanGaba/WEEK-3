
import heapq

def heuristic(state, goal):
    distance = 0
    for i in range(9):
        if state[i] != 0:
            j = goal.index(state[i])
            distance += abs(i // 3 - j // 3) + abs(i % 3 - j % 3)
    return distance

def astar(start, goal):
    pq = []
    heapq.heappush(pq, (heuristic(start, goal), 0, start))
    parent = {tuple(start): None}
    cost = {tuple(start): 0}

    while pq:
        f, g, state = heapq.heappop(pq)

        if state == goal:
            path = []
            current = tuple(goal)
            while current is not None:
                path.append(list(current))
                current = parent[current]
            path.reverse()

            print("Solution found in", len(path) - 1, "moves")
            for s in path:
                print(s[:3])
                print(s[3:6])
                print(s[6:])
                print()
            return

        zero = state.index(0)
        for move in [-3, 3, -1, 1]:
            new_pos = zero + move

            if new_pos < 0 or new_pos >= 9:
                continue
            if move == -1 and zero % 3 == 0:
                continue
            if move == 1 and zero % 3 == 2:
                continue

            new_state = state[:]
            new_state[zero], new_state[new_pos] = new_state[new_pos], new_state[zero]
            key = tuple(new_state)
            new_cost = g + 1

            if key not in cost or new_cost < cost[key]:
                cost[key] = new_cost
                parent[key] = tuple(state)
                heapq.heappush(pq, (new_cost + heuristic(new_state, goal), new_cost, new_state))

    print("No solution found")

start = [1, 2, 3, 4, 0, 6, 7, 5, 8]
goal = [1, 2, 3, 4, 5, 6, 7, 8, 0]

astar(start, goal)
