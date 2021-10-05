class Football_Player:
    def __init__(self, name, salary, performance_func=None):
        self.name = name
        self.salary = salary
        self.performance_func = performance_func


class Offense_Player(Football_Player):
    def __init__(self, name, cost, performance_func=None):
        Football_Player.__init__(self, name, cost,
                                 performance_func)
        self.total_yards_gained = 0

    def run_yards(self, yards):
        self.total_yards_gained += yards


def choose_players(players, team_motivation, num_def, num_off, max_salary):
    mot_level = 2
    return choose_players_helper(players, num_def, num_off, max_salary, 0, mot_level)


def choose_players_helper(players, num_def, num_off, max_salary, sum_qual, mot_level):
    if len(players) == 0:
        if num_def == 0 and num_off == 0 and max_salary >= 0:
            return sum_qual
        else:
            return 0
    if num_def < 0 or num_off < 0 or max_salary < 0:
        return 0
    dont_choose_curr = choose_players_helper(players[1:], num_def, num_off,
                                             max_salary, sum_qual, mot_level)
    new_sum_qual = sum_qual + players[0].get_performance(mot_level)
    new_max_sal = max_salary - players[0].cost
    if isinstance(players[0], Offense_Player):
        choose_curr = choose_players_helper(players[1:],
                                            num_def, num_off - 1, new_max_sal,
                                            new_sum_qual, mot_level)
    else:
        choose_curr = choose_players_helper(players[1:], num_def - 1,
                                            num_off, new_max_sal, new_sum_qual, mot_level)
    return max(choose_curr, dont_choose_curr)


