from django import forms
from .models import Enquirer

class EnquirerForm(forms.ModelForm):
    class Meta:
        model = Enquirer
        fields = '__all__'

        

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)