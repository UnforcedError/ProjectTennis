from django.contrib import admin

from.models import Player
# Register your models here.
class PlayerAdmin(admin.ModelAdmin):
    """
    Customized Admin page for creating Player profiles
    """
    list_display = ('surname', 'club', 'age')

    fieldsets = [
        ('Name',            {'fields': ['forename', 'surname'], }),
        ('Date of Birth',   {'fields': ['dob'], }),
        ('Club',            {'fields': ['club'], })
    ]

admin.site.register(Player, PlayerAdmin)