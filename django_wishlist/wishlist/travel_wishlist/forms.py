from django import forms
from .models import Place

# Creates a new form for entering data into Place model
class NewPlaceForm(forms.ModelForm):
    class Meta:
        model = Place
        fields = ('name', 'visited')