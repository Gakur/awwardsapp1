from .models import Projects,Rates,Comments,Profile
from django import forms

class RateForm(forms.ModelForm):
    class Meta:
        model=Rates
        exclude=['user','project']


class PostForm(forms.ModelForm):
    class Meta:
        model=Projects
        exclude=['user','design','usability','content']
