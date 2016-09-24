from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Fieldset, MultiField, Div
from django import forms
from django.core.urlresolvers import reverse
from django.forms.models import formset_factory

from .models import Player


class SimpleForm(forms.Form):
    username = forms.CharField(label='Username', required=True)
    password = forms.CharField(label='Password', required=True, widget=forms.PasswordInput)
    remember = forms.BooleanField(label='Remember me?')

    helper = FormHelper()
    helper.form_method = 'POST'
    helper.add_input(Submit('login', 'login', css_class='btn-primary'))





class PlayerForm(forms.Form):
    """
    Architecture of a form for entering a new player
    """
    forename = forms.CharField(label='Player\'s Forename', max_length=100)
    surname = forms.CharField(label='Player\'s Surname', max_length=100)
    dob = forms.DateField(widget=forms.SelectDateWidget)
    club = forms.CharField(label='Club')


class AddMatch(forms.Form):
    """
    Architecture for a form to enter a new Match
    """
    player1 = forms.ModelChoiceField(queryset=Player.objects.all().order_by('forename'),
                                     empty_label='choose a player',
                                     to_field_name='id')

    player2 = forms.ModelChoiceField(queryset=Player.objects.all().order_by('forename'),
                                     empty_label='choose a player',
                                     to_field_name='id')
    # Players' names
    # player1_forename = forms.CharField(label='Player\'s Forename', max_length=100)
    # player2_forename = forms.CharField(label='Player\'s Forename', max_length=100)
    # player1_surname = forms.CharField(label='Player\'s Forename', max_length=100)
    # player2_surname = forms.CharField(label='Player\'s Forename', max_length=100)

    # Set1
    set1p1_score = forms.IntegerField(max_value=25, initial=0)
    set1p2_score = forms.IntegerField(max_value=25, initial=0)

    # set 2
    set2p1_score = forms.IntegerField(max_value=25, initial=0, required=False)
    set2p2_score = forms.IntegerField(max_value=25, initial=0, required=False)

    # set 3
    set3p1_score = forms.IntegerField(max_value=25, initial=0, required=False)
    set3p2_score = forms.IntegerField(max_value=25, initial=0, required=False)

    def __init__(self, *args, **kwargs):
        super(AddMatch, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'POST'
        self.helper.form_action = reverse('TennisApp:match_processing')
        self.helper.layout = Layout(
            Fieldset(
                'Players participating',
                'player1',
                'player2',
                # Fieldset(
                #     'Player 1',
                #     'player1',
                #     'player1_forename',
                #     'player1_surname'
                # ),
                # Fieldset(
                #     'Player 2',
                #     'player2_forename',
                #     'player2_surname'
                # ),
                css_class='match-set'
            ),
            Fieldset(
                'Scoring information',
                Fieldset(
                    '1st Set',
                    'set1p1_score',
                    'set1p2_score',
                    css_class='match-set'
                ),
                Fieldset(
                    '2nd Set',
                    'set2p1_score',
                    'set2p2_score',
                    css_class='match-set'
                ),
                Fieldset(
                    '3rd Set',
                    'set3p1_score',
                    'set3p2_score',
                    css_class='match-set'
                )
            )
        )
        self.helper.add_input(Submit('submit', 'Submit'))

        # def check_objects(self, object, surname):
        #     try:
        #         object_db = object.objects.get(surname)
        #     except object.DoesNotExist:
        #         msg = 'The object does not exist'
        #     else:
        #         return object_db


        # def clean(self):
        #     cleaned_data = super(AddMatch, self).clean()
        #     player_1 = cleaned_data.get('player1_surname')
        #     player_2 = cleaned_data.get('player2_surname')
        #
        #     object1_db = check_objects(Player, player_1)
        #     object2_db = check_objects(Player, player_2)







class ExampleForm(forms.Form):

    # two option radio group to choose whether or not one likes this page
    like_website = forms.TypedChoiceField(
        label='Do you like the Website',
        choices=((1, 'YES'), (2, 'NO')),
        coerce= lambda x: bool(int(x)),
        widget=forms.RadioSelect,
        initial=1,
        required=True
    )

    # Textfield to enter ones favourite food
    favourite_food = forms.CharField(
        label='What is your favourite food?',
        max_length=80,
        required=True
    )

    # Textfield to enter ones favourite color
    favourite_color = forms.CharField(
        label='What is your favourite color?',
        max_length=80,
        required=True
    )

    # integerfield for favourite integer number
    favourite_number = forms.IntegerField(
        label='Favourite Number',
        required=False
    )

    # unrequired field for notes
    notes = forms.CharField(
        label='Additional notes or feedback?',
        required=False
    )

    def __init__(self, *args, **kwargs):
        super(ExampleForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            MultiField(
                'Tell us your name thoughts!',
                Div(
                    'like_website',
                    'favourite_food',
                    css_class='special-fields'
                ),
                'favourite_color',
                'favourite_food',
                'notes'
            )
        )

ExampleFormset = formset_factory(ExampleForm, extra=3)


class ExampleFormsetHelper(FormHelper):
    def __init__(self, *args, **kwargs):
        super(ExampleFormsetHelper, self).__init__(*args, **kwargs)
        self.form_method = 'POST'
        self.layout = Layout(
            'favourite_color',
            'favourite_food'
        )

        self.render_required_fields = True
