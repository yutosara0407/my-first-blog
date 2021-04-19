from django import forms
from .models import Member, Circle


class SearchForm(forms.Form):
    member = forms.ModelChoiceField(
        queryset=Member.objects, label='メンバー', required=False)

    circle = forms.ModelChoiceField(
        queryset=Circle.objects, label='サークル', required=False) 