from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.utils import timezone

from .forms import  AddMatch, PlayerForm, ExampleForm, ExampleFormset, ExampleFormsetHelper
from .models import Match, Player, Score, PlayerStats
from .utility import create_playerstats, create_table, refresh_stats


# Create your views here.


def add_match(request):
    """
    Adds a match to the statistics
    """
    # if this is a POST request we need to process the data from the form
    print(request.method)
    if request.method == 'POST':
        # create a form and populate it with data from the request
        form = AddMatch(request.POST)
        if form.is_valid():


            # refreshing stats according to form information
            refresh_stats(request)

            # redirecting to table_view
            return HttpResponseRedirect(reverse('TennisApp:table_view'))

    else:
        form = AddMatch()

    # print(form.as_p())
    return render(request, 'tennisapp/add_match.html', {'form': form})






def add_player(request):
    """
    Add a new player to the Database
    """
    # if this is a POST request we need to process the data from the form
    if request.method == 'POST':
        # create a form and populate it with data from the request
        form = PlayerForm(request.POST)
        if form.is_valid():
            print('data manipulated')
          #   return HttpResponseRedirect(reverse('TennisApp:add_match'))

    else:
        form = PlayerForm()

    print(form.as_p())
    return render(request, 'tennisapp/add_match.html', {'form': form})


def show_table(request):
    """
    showing the the standings of the players
    :param players: http request
    :return:
    """


    # TODO complete table_view
    print(request.POST)

    table = create_table()

    table_strings = []
    sublist_strings = []
    for sublist in table:
        for item in sublist:
            sublist_strings.append(str(item))
        table_strings.append(sublist_strings)
        # print(table_strings)
        sublist_strings = []
    table_strings.reverse()
    # print(table_strings)
    head = ['Forename', 'Surname', 'Wins', 'Losses', 'Win-Ratio']
    return render(request, 'tennisapp/table_form.html', {'head': head,
                                                         'table_string': table_strings})

def process_new_player(request):
    # TODO create method that inserts the new player into the database and checks if it already exists


    return HttpResponseRedirect(reverse('TennisApp:table_view'))



def show_post(request):
    """
    Just testing stuff
    """
    try:
        player1_name = request.POST.getlist('player1')[0]
        player2_name = request.POST.getlist('player2')[0]

    except IndexError:
        print('The used index does not exist')


    # creating player object from the database
    try:
        player1 = Player.objects.get(forename=player1_name)
    except Player.DoesNotExist:
        print('No Player named{0}'.format(player1_name))
        print(request.POST)

    try:
        player2 = Player.objects.get(forename=player2_name)
    except Player.DoesNotExist:
        print('No Player named{0}'.format(player1_name))


    # creating the match
    match = Match.objects.create(player1=player1, player2=player2, court='TCBW', date=timezone.now())
    match.save()

    # creating score strings
    score_set1 = '{0}:{1}'.format(request.POST.getlist('set1p1_score')[0], request.POST.getlist('set1p2_score')[0])
    score_set2 = '{0}:{1}'.format(request.POST.getlist('set2p1_score')[0], request.POST.getlist('set2p2_score')[0])
    score_set3 = '{0}:{1}'.format(request.POST.getlist('set3p1_score')[0], request.POST.getlist('set3p2_score')[0])
    score = Score.objects.create(match=match, score_set1=score_set1, score_set2=score_set2, score_set3=score_set3)
    score.save()

    create_playerstats(score.id)

    print(PlayerStats.objects.get(player_id=match.player1_id))

    return render(request, 'tennisapp/test.html', {'player1': PlayerStats.objects.all()[0].wins, })



def get_name(request):
    # if this is a POST request we need to process the data from the form
    if request.method == 'POST':
        # create a form and populate it with data from the request
        form = AddMatch(request.POST)
        if form.is_valid():
            print('data manipulated')
          #   return HttpResponseRedirect(reverse('TennisApp:add_match'))

    else:
        form = AddMatch()

    print(form.as_p())
    return render(request, 'tennisapp/add_match.html', {'form': form})


def crispy(request):
    # if this is a POST request we need to process the data from the form
    formset = ExampleFormset
    helper = ExampleFormsetHelper()

    return render(request, 'tennisapp/formsTest.html', {'formset': formset, 'helper': helper})


def inbox(request, template_name):
    example_form = ExampleForm()
    redirect_url = request.GET.get('next')

