from django import forms
from .models import Jumper


class JumperProfileForm(forms.ModelForm):
    class Meta:
        model = Jumper
        fields = '__all__'
        

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'jumper_name': 'Name',
            'jumper_dob': 'Date of Birth',
            
            
        }