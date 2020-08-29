from django import forms
from .models import Enquirer


class EnquirerForm(forms.ModelForm):
    class Meta:
        model = Enquirer
        fields = (
            'default_full_name', 'default_phone_number', 'default_email',
            'subject', 'question')

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
