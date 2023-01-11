from django import forms

class MoviesForm(forms.Form):
    name = forms.CharField(max_length=100)
    type = forms.CharField(max_length=100)
    duration = forms.FloatField()

class StudioForm(forms.Form):
    name = forms.CharField(max_length=100)

class DirectorForm(forms.Form):
    name = forms.CharField(max_length=100)
    films = forms.FloatField()

