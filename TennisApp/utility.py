from .models import Player, Match, Score, PlayerStats


# Players = Enum('Player1', 'Player2')


def create_playerstats(id):
    score = Score.objects.get(id=id)
    match = Match.objects.get(id=score.match_id)

    sets = [score.score_set1, score.score_set2, score.score_set3]
    print(sets)

    setscorep1 = 0
    setscorep2 = 0
    points = []

    for scores in sets:
        print(scores)
        score_list = scores.split(sep=':')
        points.extend(score_list)

    print(points)
    for i in range(0, len(points), 2):
        if points[i] < points[i+1]:
            setscorep2 += 1
        elif points[i] > points[i+1]:
            setscorep1 += 1


    player2_winner = setscorep2 > setscorep1

    if player2_winner:
        # update player1
        try:
            playerstats1 = PlayerStats.objects.get(player_id=match.player1_id)
            playerstats1.losses += 1

        except PlayerStats.DoesNotExist:
            playerstats1 = PlayerStats.objects.create(player=match.player1, wins=0, losses=1)

        # update player2
        try:
            playerstats2 = PlayerStats.objects.get(player_id=match.player2_id)
            playerstats2.wins += 1

        except PlayerStats.DoesNotExist:
            playerstats2 = PlayerStats.objects.create(player=match.player2, wins=1, losses=0)

    elif not player2_winner:
        # update player1
        try:
            playerstats1 = PlayerStats.objects.get(player_id=match.player1_id)
            playerstats1.wins += 1

        except PlayerStats.DoesNotExist:
            playerstats1 = PlayerStats.objects.create(player=match.player1, wins=1, losses=0)

        # update player2
        try:
            playerstats2 = PlayerStats.objects.get(player_id=match.player2_id)
            playerstats2.losses += 1

        except PlayerStats.DoesNotExist:
            playerstats2 = PlayerStats.objects.create(player=match.player2, wins=0, losses=1)



    playerstats1.save()
    playerstats2.save()

def create_table():
    # get Player statistics
    playerstats = PlayerStats.objects.all()

    #sort stats by the number of wins
    # if numbers are equal use number of losses
    # if the is even two players own the same spot in the table
    playerstats_sorted = sorted(playerstats, key = lambda x: (x.wins, -x.losses))


    # the table is a 2D-list
    table = []
    for stats in playerstats_sorted:
        table.append(stats.to_list())

    return table


def get_matches_with_player(player):
    all_matches = []
    all_matches.extend(Match.objects.get(player1_id=player.id))
    all_matches.extend(Match.objects.get(player2_id=player.id))

    return all_matches

def get_match_record(player1, player2):
    """
    returns the match record of the two players against each other
    :param player1: a Player object
    :param player2: a Player object
    :return: tuple with int of the overallstandings and a string representing it
    """
    all_matches = get_matches_with_player(player1)
    wins_player1 = 0
    wins_player2 = 0

    for match in all_matches:
        if match.player1_id == player1.id and match.player2_id == player2.id:
            score = Score.objects.get(match_id=match.id)
            if score.winner() == Players.Player1:
                wins_player1 += 1
            elif score.winner() == Players.Player2:
                wins_player2 += 1

        elif match.player2_id == player1.id and match.player1_id == player2.id:
            score = Score.objects.get(match_id=match.id)
            if score.winner() == Players.Player1:
                wins_player1 += 1
            elif score.winner() == Players.Player2:
                wins_player2 += 1

        return (wins_player1 - wins_player2, '{0}:{1}'.format(wins_player1, wins_player2)
                )


def refresh_statistics(winner, looser):
    """
    This function takes the winner as an input and adds one win to the respective winner and one loose to the looser
    :param winner: object of the victorious player
    :param looser: object of the defeated player
    """
    winner_db = Player.objects.get(id=winner.id)


def create_score(post, match_id):
    """
    Creates a score object from a POST object containing the relevant information
    :param match_id: match_id of the match the score belongs to
    :param post: POST containing information about at least the score of 1 set and the match object this score belongs to
    :return: nothing, saves score directly to the Database
    """
    # creating score strings
    score_set1 = '{0}:{1}'.format(post.getlist('set1p1_score')[0], post.getlist('set1p2_score')[0])
    score_set2 = '{0}:{1}'.format(post.getlist('set2p1_score')[0], post.getlist('set2p2_score')[0])
    score_set3 = '{0}:{1}'.format(post.getlist('set3p1_score')[0], post.getlist('set3p2_score')[0])
    score = Score.objects.create(match=Match.objects.get(id=match_id),
                                 score_set1=score_set1,
                                 score_set2=score_set2,
                                 score_set3=score_set3
                                 )
    score.save()



# THIS FUNCTION IS NOT NEEDED BUT MAY BE USEFUL IN THE FURTHER DEVELOPMENT
# FS
#
# def ordering_playerstats(player1, player2):
#     # the player with mor
#     if player1.wins > player2.wins:
#         return True
#     elif player1.wins == player2.wins:
#         if player1.losses < player2.losses:
#             return True
#         elif player1.losses == player2.losses:
#             score = get_match_record(player1, player2)
#             win_diff = score[0]
#             if win_diff > 0:
#                 return True
#             elif win_diff == 0:
#                 # shall indicate that the two player are equally good
#                 return None
#             else:
#                 return False

