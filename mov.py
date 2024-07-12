import msvcrt
def can_move(grid):
    if any(0 in row for row in grid):
        return True
    for row in range(4):
        for col in range(4):
            if (col < 3 and grid[row][col] == grid[row][col + 1]) or (row < 3 and grid[row][col] == grid[row + 1][col]):
                return True
    return False

def compress(grid):
    new_grid = [[0 for _ in range(4)] for _ in range(4)]
    for row in range(4):
        pos = 0
        for col in range(4):
            if grid[row][col] != 0:
                new_grid[row][pos] = grid[row][col]
                pos += 1
    return new_grid

def merge(grid):
    score = 0
    for row in range(4):
        for col in range(3):
            if grid[row][col] == grid[row][col + 1] and grid[row][col] != 0:
                grid[row][col] *= 2
                grid[row][col + 1] = 0
                score += grid[row][col]
    return score

def reverse(grid):
    return [row[::-1] for row in grid]

def transpose(grid):
    return [list(row) for row in zip(*grid)]

def move_left(grid):
    grid = compress(grid)
    score = merge(grid)
    grid = compress(grid)
    return grid, score

def move_right(grid):
    grid = reverse(grid)
    grid, score = move_left(grid)
    grid = reverse(grid)
    return grid, score

def move_up(grid):
    grid = transpose(grid)
    grid, score = move_left(grid)
    grid = transpose(grid)
    return grid, score

def move_down(grid):
    grid = transpose(grid)
    grid, score = move_right(grid)
    grid = transpose(grid)
    return grid, score
def get_move():
    while True:
        print("Enter move (W/A/S/D): ", end='', flush=True)
        key = msvcrt.getch().decode().upper()
        if key in ['W', 'A', 'S', 'D', 'K']:
            return key
        else:
            print("\nInvalid move. Please enter W, A, S, or D. Press K to end game.")