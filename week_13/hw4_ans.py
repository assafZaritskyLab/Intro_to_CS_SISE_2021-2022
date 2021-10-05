"""
PART 1
"""


# Q1
def fibonacci_chars(n, k):
    def fibonacci_chars_rec(n):
        if n == 0:
            return "a"
        if n == 1:
            return "bc"
        return "{}{}".format(fibonacci_chars_rec(n - 2), fibonacci_chars_rec(n - 1))

    return fibonacci_chars_rec(n)[k]


# print(fibonacci_chars(n=10, k=8))

# Q2
def drainage_basins(elavation_ridge):
    def drainage_basins_rec(elavation_ridge, ctr):
        if ctr == len(elavation_ridge) - 1:
            if elavation_ridge[ctr] < elavation_ridge[ctr - 1]:
                return [ctr]
            else:
                return []
        elif ctr == 0 and elavation_ridge[ctr] < elavation_ridge[ctr + 1]:
            return [ctr] + drainage_basins_rec(elavation_ridge, ctr + 1)
        elif elavation_ridge[ctr] < elavation_ridge[ctr - 1] and \
                elavation_ridge[ctr] < elavation_ridge[ctr + 1]:
            return [ctr] + drainage_basins_rec(elavation_ridge, ctr + 1)
        else:
            return drainage_basins_rec(elavation_ridge, ctr + 1)

    return drainage_basins_rec(elavation_ridge, 0)


"""
PART B
"""


def is_legit_track(grid, i1, j1, i2, j2, current_weight):
    if i2 < 0 or j2 < 0 or i2 >= len(grid) or j2 >= len(grid[0]):
        return False
    if (i1 == i2 + 1 and j1 == j2) or (i1 == i2 - 1 and j1 == j2) or \
            (i1 == i2 and j1 == j2 + 1) or (i1 == i2 and j1 == j2 - 1):
        if current_weight + grid[i2][j2] < 2 * grid[i2][j2]:
            return True
    return False


def get_number_legit_tracks_rec(grid, i1, j1, current_weight):
    if len(grid) - 1 == i1 and len(grid[0]) - 1 == j1:
        return 1
    num_of_paths = 0
    if is_legit_track(grid, i1, j1, i1 + 1, j1, current_weight + grid[i1][j1]):
        num_of_paths += get_number_legit_tracks_rec(grid, i1 + 1, j1, grid[i1][j1] + current_weight)
    if is_legit_track(grid, i1, j1, i1, j1 + 1, current_weight + grid[i1][j1]):
        num_of_paths += get_number_legit_tracks_rec(grid, i1, j1 + 1, grid[i1][j1] + current_weight)
    if is_legit_track(grid, i1, j1, i1 - 1, j1, current_weight + grid[i1][j1]):
        num_of_paths += get_number_legit_tracks_rec(grid, i1 - 1, j1, grid[i1][j1] + current_weight)
    if is_legit_track(grid, i1, j1, i1, j1 - 1, current_weight + grid[i1][j1]):
        num_of_paths += get_number_legit_tracks_rec(grid, i1, j1 - 1, grid[i1][j1] + current_weight)
    return num_of_paths


def get_number_legit_tracks(grid, i1, j1):
    return get_number_legit_tracks_rec(grid, i1, j1, 0)


"""
PART C
"""


# regular knapsack
# with memoization
def get_least_expensive(with_fl, without_fl):
    if with_fl[0] >= without_fl[0]:
        return with_fl
    if with_fl[0] < without_fl[0]:
        return without_fl


def get_flowers_to_plant_rec(possible_flowers, budget_left, fl_idx, memo_array):
    if budget_left == 0 or fl_idx < 0:
        return (0, budget_left)
    if memo_array[budget_left - 1][fl_idx] is not None:
        return memo_array[budget_left - 1][fl_idx]
    if possible_flowers[fl_idx][2] > budget_left:
        return get_flowers_to_plant_rec(possible_flowers,
                                        budget_left,
                                        fl_idx - 1, memo_array)

    with_fl = get_flowers_to_plant_rec(possible_flowers,
                                       budget_left - possible_flowers[fl_idx][2],
                                       fl_idx - 1, memo_array)
    with_fl = with_fl[0] + possible_flowers[fl_idx][1], with_fl[1]
    without_fl = get_flowers_to_plant_rec(possible_flowers,
                                          budget_left,
                                          fl_idx - 1, memo_array)
    memo_array[budget_left - 1][fl_idx] = get_least_expensive(with_fl, without_fl)
    return memo_array[budget_left - 1][fl_idx]


def optimize_flowers_selection(flowers, budget):
    if budget == 0:
        return 0, 0
    memo_array = [[None for j in range(len(flowers))] for i in range(budget)]
    return get_flowers_to_plant_rec(flowers, budget, len(memo_array[0]) - 1, memo_array)


def get_plants_to_buy_faster(flowers, budget):
    return optimize_flowers_selection(flowers, budget)
