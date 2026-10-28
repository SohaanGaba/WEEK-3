
import random

def heuristic(board, n):
    conflicts = 0
    for i in range(n):
        for j in range(i + 1, n):
            if board[i] == board[j] or abs(board[i] - board[j]) == abs(i - j):
                conflicts += 1
    return conflicts

def hill_climbing(n):
    board = [random.randint(0, n - 1) for _ in range(n)]

    while True:
        h = heuristic(board, n)
        if h == 0:
            return board

        best_board = board[:]
        best_h = h

        for col in range(n):
            for row in range(n):
                if board[col] != row:
                    new_board = board[:]
                    new_board[col] = row
                    new_h = heuristic(new_board, n)

                    if new_h < best_h:
                        best_h = new_h
                        best_board = new_board

        if best_h >= h:
            board = [random.randint(0, n - 1) for _ in range(n)]
        else:
            board = best_board

def display(board, n):
    for row in range(n):
        print(" ".join("Q" if board[col] == row else "." for col in range(n)))

n = int(input("Enter number of queens: "))
board = hill_climbing(n)
print("Solution:")
display(board, n)
