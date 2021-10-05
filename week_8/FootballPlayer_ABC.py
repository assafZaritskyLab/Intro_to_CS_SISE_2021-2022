from abc import ABC, abstractmethod


class FootballPlayer(ABC):

    def __init__(self, name, salary, performance):
        self.name = name
        self.salary = salary
        self.performance = float(performance)

    @abstractmethod
    def play(self, num):
        pass

    def __repr__(self):
        return f"Name: {self.name}\n" \
               f"Salary: {self.salary}M $\n" \
               f"Performance: {self.performance}"


# player = FootballPlayer('a', 1, 1)
# player.play()


class OffensePlayer(FootballPlayer):

    def __init__(self, name, salary, performance):
        super().__init__(name, salary, performance)
        # FootballPlayer.__init__(self, name, salary, performance)
        self.total_yards = 0

    def play(self, num):
        self.total_yards += num

    def get_total_yards(self):
        return self.get_total_yards

    def __repr__(self):
        res = super().__repr__()  # todo super()  Multiple inheritance
        # res = FootballPlayer.__repr__(self)
        return f'{res}\nTotal Yards: {self.total_yards}'


class DefensePlayer(FootballPlayer):

    def __init__(self, name, salary, performance):
        super().__init__(name, salary, performance)
        self.total_tackles = 0

    def play(self):
        self.total_tackles += 1

    def __repr__(self):
        res = super().__repr__()
        return f'{res}\nTotal Tackles: {self.total_tackles}'


off_player = OffensePlayer('Player1', 3, 9.7)
# def_player = DefensePlayer('Player2', 2, 6.3)
off_player.play(5)
# off_player.play(10)
# def_player.play()
# def_player.play()
# print(off_player)
# print(20 * '=')
# print(def_player)

