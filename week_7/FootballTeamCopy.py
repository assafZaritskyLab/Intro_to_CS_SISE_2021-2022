import copy

from week_7.DefensePlayer import DefensePlayer
from week_7.OffensePlayer import OffensePlayer


class FootballTeam:
    """
    This class represents a Football Team
    """

    def __init__(self, players):
        """
        Constructor.
        :param players: list - list of Football Players objects
        """
        self.__players = players

    def get_team(self):
        """
        method that return a copy of the players list
        """
        # return self.__players
        return copy.copy(self.__players)


p1 = DefensePlayer('Janis Griffin', 15, 6.2)
p2 = OffensePlayer('John Smith', 22, 7)
team = FootballTeam([p1, p2])

team.get_team()[0].name = 'hacker 2'
list = team.get_team()
for player in team.get_team():
    print(player.name)





