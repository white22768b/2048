import os
import stat
import random

def initialize_grid():
    grid = [[0 for _ in range(4)] for _ in range(4)]
    add_new_tile(grid)
    add_new_tile(grid)
    return grid

def add_new_tile(grid):
    if any(0 in row for row in grid):
        row, col = random.choice([(r, c) for r in range(4) for c in range(4) if grid[r][c] == 0])
        grid[row][col] = random.choice([2, 4])

def display_scores():
    scores = stat.read_scores()
    print("High scores and previous 5 scores:")
    for game_info, score_info, time_info in scores:
        print(f"{game_info}, {score_info}, Played at: {time_info}")

def print_grid(grid):
    for row in grid:
        print('+----' * 4 + '+')
        print(''.join(f'|{num if num > 0 else "":4}' for num in row) + '|')
    print('+----' * 4 + '+')
    
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def contains_2048_tile(grid):
    for row in grid:
        if 2048 in row:
            return True
    return False
