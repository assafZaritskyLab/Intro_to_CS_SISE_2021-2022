from week_7.FootballPlayer import FootballPlayer


class OffensePlayer(FootballPlayer):
    """
    This class represents an offense player - inherite FootballPlayer
    """

    def __init__(self, name, salary, performance, yards=0):
        """
        Constructor.
        :param name: string - the player name
        :param salary: int - salary in M$
        :param performance: float - player's performance
        """
        FootballPlayer.__init__(self, name, salary, performance)
        self.total_yards = yards


    def __repr__(self):
        """
        repr overload
        """
        res = FootballPlayer.__repr__(self)
        return res + '\n' + f'Total Yards: {self.total_yards}'

    def run_yards(self, yards):
        """
        Method that let the player run.
        :param yards: int - amount of yards that the player has ran.
        """
        self.total_yards += yards


# p2 = OffensePlayer('John Smith', 22, 7)
# p2.run_yards(1)
# p2.run_yards(3)
# print(p2)