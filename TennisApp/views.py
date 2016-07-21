from django.shortcuts import render
from django import forms
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from .models import Match
from .forms import  PlayerForm
# Create your views here.


def add_match(request):
    """
    Adds a match to the statistics
    """
    print(request.POST)
    return render(request, 'tennisapp/add_match.html')




def show_post(request):
    """
    Just testing stuff
    """
    try:
        set1 = request.POST.getlist('set1')
        set2 = request.POST.getlist('set2')
        set3 = request.POST.getlist('set3')
        score_set1 = '{0}:{1}'.format(set1[0], set1[1])
        score_set1 = '{0}:{1}'.format(set2[0], set2[1])
        score_set1 = '{0}:{1}'.format(set3[0], set3[1])
        print(set1)
        print(set2)
        print(set3)
        Match.objects.create()
    except:
        set1_1 = 12
        print('excepted:')
        print(request.POST)
    return render(request, 'tennisapp/test.html', {'set1': set1, })

def get_name(request):
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
    return render(request, 'tennisapp/formsTest.html', {'form': form.as_p()})
