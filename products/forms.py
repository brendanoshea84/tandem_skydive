from django import forms
from .models import Jumper


class JumperProfileForm(forms.ModelForm):
    class Meta:
        model = Jumper
        fields = '__all__'

        

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)
        
        