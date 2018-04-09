from django import forms
from .models import Place

# Creates a new form for entering data into Place model
class NewPlaceForm(forms.ModelForm):
    class Meta:
        model = Place
        fields = ('name', 'visited')

# Creates a new form for entering a review and a date visited
class VisitedForm(forms.ModelForm):
    class Meta:
        model = Place
        fields = ('text', 'visited_date')