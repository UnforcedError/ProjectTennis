from django import forms

from .models import Player


class PlayerForm(forms.ModelForm):
    """
    Architecture of a form for entering a new player
    """

    class Meta:
        model = Player
        fields = ('forename', 'surname', 'dob', 'club')

    def __init__(self, *args, **kwargs):
        form = super(PlayerForm, self).__init__(*args, **kwargs)
        for visible in form.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'


class AddMatch(forms.Form):
    """
    Architecture for a form to enter a new Match
    """
    player1_name = forms.CharField(label='Player\'s Name', max_length=100)
    player2_name = forms.CharField(label='Player\'s Name', max_length=100)

    # Set1
    set1p1_score = forms.IntegerField(max_value=25)
    set1p2_score = forms.IntegerField(max_value=25)

    # set 2
    set2p1_score = forms.IntegerField(max_value=25)
    set2p2_score = forms.IntegerField(max_value=25)

    # set 3
    set3p1_score = forms.IntegerField(max_value=25)
    set3p2_score = forms.IntegerField(max_value=25)