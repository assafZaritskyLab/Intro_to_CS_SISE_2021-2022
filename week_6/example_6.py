## Example 4: Maze solver

# %%

def is_valid(grid, neighbor):  # neighbor[0]=row index, neighbor[1]=col index
    return 0 <= neighbor[0] < len(grid) and \
           0 <= neighbor[1] < len(grid[neighbor[0]]) \
           and (grid[neighbor[0]][neighbor[1]] == 1 or grid[neighbor[0]][neighbor[1]] == 2)


def solve_maze_rec(grid, initial_point, goal_point, solution_path):
    grid[initial_point[0]][initial_point[1]] = 3  # mark as a visited
    if initial_point == goal_point:  # solution found
        solution_path.insert(0, goal_point)  # 0 = index
        return True
    row = initial_point[0]
    col = initial_point[1]
    if is_valid(grid, (row - 1, col)) and solve_maze_rec(grid, (row - 1, col), goal_point, solution_path):  # Down
        solution_path.insert(0, (row - 1, col))
        return True
    if is_valid(grid, (row + 1, col)) and solve_maze_rec(grid, (row + 1, col), goal_point, solution_path):  # Up
        solution_path.insert(0, (row + 1, col))
        return True
    if is_valid(grid, (row, col - 1)) and solve_maze_rec(grid, (row, col - 1), goal_point, solution_path):  # Right
        solution_path.insert(0, (row, col - 1))
        return True
    if is_valid(grid, (row, col + 1)) and solve_maze_rec(grid, (row, col + 1), goal_point, solution_path):  # Left
        solution_path.insert(0, (row, col + 1))
        return True
    return False


def solve_maze(grid, initial_point, goal_point):
    solution = []
    b = solve_maze_rec(grid, initial_point, goal_point, solution)
    print(b, solution)


# %%

n_sol = [[1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1],
         [1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 1],
         [0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0],
         [1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1],
         [1, 0, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1],
         [1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1],
         [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 2]]
print("With no solution:")
print(solve_maze(n_sol, (0, 2), (7, 12)))
for i in n_sol:
    print(i)


y_sol = [[1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1],
         [1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 1],
         [0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0],
         [1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1],
         [1, 0, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1],
         [1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1],
         [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2]]

print("With solution:")
solve_maze(y_sol, (0, 2), (7, 12))
for i in y_sol:
    print(i)
