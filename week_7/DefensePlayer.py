from week_7.FootballPlayer import FootballPlayer


class DefensePlayer(FootballPlayer):
    """
    This class represents an defense player - inherite FootballPlayer
    """

    def __init__(self, name, salary, performance):
        """
        Constructor.
        :param name: string - the player name
        :param salary: int - salary in M$
        :param performance: float - player's performance
        """
        FootballPlayer.__init__(self, name, salary, performance)
        self.total_tackles = 0


    def __repr__(self):
        """
        repr overload
        """
        res = FootballPlayer.__repr__(self)
        return res + '\n' + f'Total Tackles: {self.total_tackles}'

    def tackle(self):
        """
        a function that describes a tackle.
        """
        self.total_tackles += 1


p1 = DefensePlayer('Janis Griffin', 15, 6.2)
p1.tackle()
p1.tackle()
print(p1)