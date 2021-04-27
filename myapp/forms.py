from django import forms
from .models import Member, Circle, MemberImage
from PIL import Image


class SearchForm(forms.Form):
    member = forms.ModelChoiceField(
        queryset=Member.objects, label='メンバー', required=False)

    circle = forms.ModelChoiceField(
        queryset=Circle.objects, label='サークル', required=False) 

class MemberImageForm(forms.ModelForm):
    class Meta:
        model = MemberImage
        fields = ('member_image',)

class UpLoadMemberImageForm(forms.Form):
    member_image = forms.ImageField(required=True)