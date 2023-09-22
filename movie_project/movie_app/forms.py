from django import forms

from movie_app.models import Movies


class Movieform(forms.ModelForm):
    class Meta:
        model = Movies
        fields = ['name', 'desc', 'year', 'img']
