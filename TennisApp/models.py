from enum import Enum

from django.db import models
from django.utils import timezone

Players = Enum('Player1', 'Player2')

# Create your models here.


# class for player
class Player(models.Model):
    """
    Representing a player
    """
    # name of the player
    forename = models.CharField(max_length=100)
    surname = models.CharField(max_length=100, default='Doe')
    # Date of Birth 6 age
    dob = models.DateField('Date of Birth')
    # today = timezone.now()
    # age = (today.year - dob.year) - ((today.month, today.day) < (dob.month, dob.day))

    # club the player is competing for
    club = models.CharField(max_length=200)

    def age(self):
        """

        :return: age of the player
        """
        today = timezone.now()
        dob = self.dob
        return (today.year - dob.year) - ((today.month, today.day) < (dob.month, dob.day))



# class for matches
class Match(models.Model):
    """
    A Model class as a representation for Tennis matches
    """

    # players participating in this match
    player1 = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='player1')
    player2 = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='player2')

    # Court auf dem gespielt wurde
    court = models.CharField(max_length=200)

    # date of the match
    date = models.DateField('Date of the Match')


# a model representing the score of a match
class Score(models.Model):
    """
    Score of a match
    """
    # every score belongs to exactly one match
    match = models.ForeignKey(Match, on_delete=models.CASCADE)

    # scores of each set
    score_set1 = models.CharField(max_length=10)
    score_set2 = models.CharField(max_length=10)
    score_set3 = models.CharField(max_length=10)

    def to_int_list(self):
        string_list = self.to_list()
        integer_list = []
        for result in string_list:
            temp_list = result.split(sep=':')
            integer_list.append([int(item) for item in temp_list])

        return integer_list

    def to_list(self):
        return [self.score_set1, self. score_set2, self.score_set3]

    def winner(self):
        """
        returns the winner of the match
        :return: 1: player1 won, 2:player2 won
        """
        saldo = 0
        sets_list = self.to_int_list()
        for index in range(0, len(sets_list), step=2):
            if sets_list[index] > sets_list[index + 1]:
                saldo += 1
            else:
                saldo -= 1

        if saldo > 0:
            return Players.Player1
        else:
            return Players.Player2


class PlayerStats(models.Model):
    """
    Model holding some of the interesting statistics data
    """

    # player the statistics data belongs to
    player = models.ForeignKey(Player, on_delete=models.CASCADE)

    # number of wins
    wins = models.IntegerField(default=0)

    # number of losses
    losses = models.IntegerField(default=0)

    # total number of matches played
    def matches(self):
        return self.wins + self.losses

    # returning stats as a list
    def to_list(self):
        return [self.player.forename, self.player.surname, self.wins, self.losses, self.wins / (self.losses + self.wins)]
