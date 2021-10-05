
class FootballPlayer:
    """
    This class represents a football player.
    """

    def __init__(self, name, salary, performance):
        """
        Constructor.
        :param name: string - the player name
        :param salary: int - salary in M$
        :param performance: float - player's performance
        """
        self.name = name
        self.salary = salary
        self.performance = float(performance)

    def __repr__(self):
        """
        repr overload
        """
        return f"Name: {self.name}\n" \
               f"Salary: {self.salary}M $\n" \
               f"Performance: {self.performance}"

# p = FootballPlayer('Tom Brady', 20, 7)
# print(p)
