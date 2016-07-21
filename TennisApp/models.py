import datetime

from django.db import models
from django.utils import timezone

# Create your models here.

#class for player
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



#class for matches
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
    #matches = wins + losses
